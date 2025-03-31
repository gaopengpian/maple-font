from collections.abc import Sequence


class Line:
    def __init__(self, text: str, level=0) -> None:
        self.text = text
        self.level = level

    def indent(self) -> "Line":
        return Line(self.text, self.level + 1 if self.text else 0)


class Clazz:
    def __init__(self, name: str, glyphs: list[str], cls: "list[Clazz]" = []) -> None:
        self.name = name
        self.glyphs = glyphs
        self.cls = cls

    def ref(self) -> str:
        return f"@{self.name}"

    def state(self) -> Line:
        return Line(f"{self.ref()} = {clazz([*self.glyphs, *self.cls])};")


__punctuation_map = {
    "{": "braceleft",
    "}": "braceright",
    "[": "bracketleft",
    "]": "bracketright",
    "(": "parenleft",
    ")": "parenright",
    "<": "less",
    ">": "greater",
    ".": "period",
    ",": "comma",
    "-": "hyphen",
    "_": "underscore",
    "=": "equal",
    "+": "plus",
    ":": "colon",
    ";": "semicolon",
    "?": "question",
    "!": "exclam",
    "@": "at",
    "#": "numbersign",
    "$": "dollar",
    "%": "percent",
    "^": "asciicircum",
    "&": "ampersand",
    "*": "asterisk",
    "'": "quotesingle",
    '"': "quotedbl",
    "/": "slash",
    "\\": "backslash",
    "|": "bar",
    "`": "grave",
    "~": "asciitilde",
}

total_punctuations = __punctuation_map.keys()


def __gly(g: str | Clazz | Sequence[str | Clazz] | None) -> str:
    if not g:
        return ""
    if isinstance(g, list):
        return " ".join([__gly(_) for _ in g])
    if isinstance(g, Clazz):
        return g.ref()
    if not isinstance(g, str):
        raise TypeError(f"{g}({type(g)}) is invalid for __gly")
    if g in total_punctuations:
        return __punctuation_map[g]
    return g


def __prefix(data: str | Clazz | Sequence[str | Clazz] | None) -> str:
    if data:
        return __gly(data) + " "
    return ""


def __suffix(data: str | Clazz | Sequence[str | Clazz] | None) -> str:
    if data:
        return " " + __gly(data)
    return ""


def __subst(source: str, target: str) -> Line:
    return Line(f"sub {source} by {target};")


SPC = "SPC"


def gly(g: str | list[str], suffix: str = "", overwrite=False):
    """
    Normalize glyph name.

    If no suffix and ``len(g) > 1``, suffix is ``".liga"``;
    else suffix is ``""``

    >>> gly("_")
    "underline"
    >>> gly("++")
    "plus_plus.liga"
    >>> gly("--", ".suffix")
    "hyphen_hyphen.liga.suffix"
    >>> gly("--", ".suffix", True)
    "hyphen_hyphen.suffix"
    """
    if len(g) > 1:
        suf = suffix if overwrite else (".liga" + suffix)
        return "_".join(map(__gly, list(g))) + suf
    return __gly(g) + suffix


def create(cls: list[Clazz], content: list[Line], indent=2) -> str:
    _idt = indent * " "
    lines: list[Line] = []

    for line in [c.state() for c in cls] + content:
        if line.text.startswith("#") or (
            line.text.startswith("feature ") and line.text.endswith("{")
        ):
            lines.append(Line(""))
        lines.append(line)

    return "".join([("\n" + _idt * c.level + c.text) for c in lines])[1:]


def feature(tag: str, content: Sequence[Line | list[Line]]) -> list[Line]:
    """Generate a feature block with indented content.
    This function creates a feature block with the specified tag and content,
    formatting it according to the OpenType feature file syntax.

    >>> feature("liga", [subst("a", "b", "c", "d")])
    [
        Line("feature liga {"),
        Line("sub a b' c by d"),
        Line("} liga;")
    ]
    """
    target = []
    for c in content:
        if isinstance(c, list):
            for i in c:
                target.append(i.indent())
        else:
            target.append(c.indent())

    return [Line(f"feature {tag} {{"), *target, Line(f"}} {tag};")]


def cv(id: int, name: str, content: list[Line]) -> list[Line]:
    """
    Generate Character Variants (cv) OpenType feature.
    Raises:
        TypeError: If id is not between 1 and 99.
    Example:
        >>> cv(1, "Alternate a", [Line("sub a by a.alt;")])
        [
            Line("feature cv01 {"),
            Line("cvParameters {"),
            Line("FeatUILabelNameID {", 1),
            Line('name "Alternate a";', 2),
            Line("};", 1),
            Line("sub a by a.alt"),
            Line("};"),
        ]
    """
    if id < 1 or id > 99:
        raise TypeError(
            f"id should > 0 and < 100 in Character Variants, current is {id}"
        )

    param = [
        Line("cvParameters {"),
        Line("FeatUILabelNameID {", 1),
        Line(f'name "{name}";', 2),
        Line("};", 1),
        Line("};"),
    ]
    return feature(f"cv{id:02d}", [*param, *content])


def ss(id: int, name: str, content: Sequence[Line | list[Line]]) -> list[Line]:
    """
    Creates stylistic set (ss) OpenType feature.
    Raises:
        TypeError: If the ID is not between 1 and 20
    Example:
        >>> ss(1, "Stylistic Set 1", [Line("sub a by a.ss01;")])
        [
            Line("feature ss01 {"),
            Line("featureNames {", 1),
            Line('name "Stylistic Set 1";', 2),
            Line("};", 1),
            Line("sub a by a.ss01;", 1),
            Line("};")
        ]
    """
    if id < 1 or id > 20:
        raise TypeError(f"id should > 0 and < 21 in Stylistic Sets, current is {id}")

    param = [
        Line("featureNames {"),
        Line(f'name "{name}";', 1),
        Line("};"),
    ]
    return feature(f"ss{id:02d}", [*param, *content])


def langsys_list(config: list[list[str]]) -> list[Line]:
    return [Line(f"languagesystem {script} {lang};") for script, lang in config]


def lang(lang: str) -> Line:
    return Line(f"language {lang};")


def script(script: str) -> Line:
    return Line(f"script {script};")


def lookup(name: str, desc: str | None, content: list[Line]) -> list[Line]:
    """
    Generate lookup table.

    >>> lookup("example", "Replace a with b", [Line("sub a by b;")])
    [
        Line("# Replace a with b"),
        Line("lookup example {"),
        Line("sub a by b;"),
        Line("} example;")
    ]
    """
    arr = []

    if desc:
        arr.append(Line(f"# {desc}"))

    arr.append(Line(f"lookup {name} {{"))

    for c in content:
        arr.append(c.indent())

    arr.append(Line(f"}} {name};"))
    return arr


def subst(
    prefix: str | Clazz | Sequence[str | Clazz] | None,
    glyph: str | Clazz,
    suffix: str | Clazz | Sequence[str | Clazz] | None,
    replace: str | Clazz,
) -> Line:
    """
    Generate substitution line.

    >>> subst(["a"], "b", "-", "d")
    [
        Line("sub a b' hyphen by d;")
    ]
    """
    return __subst(
        f"{__prefix(prefix)}{__gly(glyph)}'{__suffix(suffix)}", f"{__gly(replace)}"
    )


def subst_list_map(
    glyphs: list[str],
    source_suffix: str = "",
    target_suffix: str = "",
) -> list[Line]:
    """
    Generate substitution lines for a list of glyphs with a specified suffix.

    >>> subst_list_map(["Q", "all", "{{"], target_suffix=".cv01")
    [
        Line("sub Q by Q.cv01;"),
        Line("sub all by all.cv01;"),
        Line("sub braceleft_braceleft.liga by braceleft_braceleft.liga.cv01;")
    ]
    """
    result = []
    for g in glyphs:
        _g = gly(list(g)) if g[0] in total_punctuations else g
        result.append(__subst(f"{_g}{source_suffix}", f"{_g}{target_suffix}"))

    return result


def subst_list_liga(
    source: str | list[str],
    target: str | None = None,
    lookup_name: str | None = None,
    surround: list[list[Sequence[str | Clazz]]] = [],
    ignores: list[Line] | None = None,
):
    """
    Generate substitution lines for target ligature.

    Default ``target`` is ``gly(source)``

    Default ``lookup_name`` is ``target``

    Args:
        source: The glyphs to form the ligature (e.g., "!=" or ["!", "="]).
        target: The ligature glyph name; defaults to gly(source).
        lookup_name: Name of the lookup block; defaults to target.
        surround: List of [prefix, suffix] pairs specifying contexts for substitution.
            Each prefix/suffix is ``Sequence[str | Clazz]``.
            If empty, generates basic substitution rules without context.
        ignores: List of ignore rules to include in the lookup.

    Returns:
        list[Line]: Lines forming a lookup block with substitution rules.

    Examples:
        >>> subst_list_liga("!=")
        [
            Line("lookup exclam_equal.liga {"),
            Line("sub exclam' equal by SPC;"),
            Line("sub SPC equal' by exclam_equal.liga;"),
            Line("} lookup exclam_equal.liga;")
        ]
        >>> subst_list_liga("!=", surround=[[["a","b"], "c"], [cls, ["a","c"]]])
        [
            Line("lookup exclam_equal.liga {"),
            Line("sub a b exclam' equal c by SPC;"),
            Line("sub @cls exclam' equal a c by SPC;"),
            Line("sub a b SPC equal' c by exclam_equal.liga;"),
            Line("sub @cls SPC equal' a c by exclam_equal.liga;"),
            Line("} lookup exclam_equal.liga;")
        ]
    """
    source_arr = list(source)
    if not target:
        target = gly(source)
    if not lookup_name:
        lookup_name = target
    if ignores is None:
        ignores = []

    def to_list(item):
        if item is None:
            return []
        elif isinstance(item, (str, Clazz)):
            return [item]
        else:
            return list(item)

    subst_rules = []
    if not surround:
        surround = [[[], []]]

    for prfx, sfx in surround:
        prfx_list = to_list(prfx)
        sfx_list = to_list(sfx)
        n = len(source_arr)

        for i in range(n - 1):
            subst_prefix = prfx_list + [SPC] * i
            subst_suffix = source_arr[i + 1 :] + sfx_list
            subst_rules.append(subst(subst_prefix, source_arr[i], subst_suffix, SPC))

        subst_prefix = prfx_list + [SPC] * (n - 1)
        subst_rules.append(subst(subst_prefix, source_arr[-1], sfx_list, target))

    return lookup(
        lookup_name,
        f"Ligature rules for {source if isinstance(source, str) else lookup_name}",
        ignores + subst_rules[::],
    )


def ignore(
    prefix: str | Clazz | Sequence[str | Clazz] | None,
    glyph: str,
    suffix: str | Clazz | Sequence[str | Clazz] | None,
) -> Line:
    """
    Generate ignore rule.

    >>> ignore("{", "b", ["c", "d"])
    Line("ignore sub braceleft b' c d;")
    >>> ignore("_ _", "b", cls)
    Line("ignore sub underscore underscore b' @cls;")
    """
    return Line(f"ignore sub {__prefix(prefix)}{__gly(glyph)}'{__suffix(suffix)};")


def clazz(glyphs: Sequence[str | Clazz] = []) -> str:
    """
    Generate inline class.

    >>> ignore(["a", "+", "@"], [cls])
    "[@cls a plus at]"
    """
    return "[" + " ".join([__gly(g) for g in glyphs]) + "]"
