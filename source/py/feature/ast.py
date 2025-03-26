from collections.abc import Sequence


class Line:
    def __init__(self, text: str, level=0) -> None:
        self.text = text
        self.level = level

    def indent(self):
        self.level += 1


class Clazz:
    def __init__(self, name: str, glyphs: list[str], cls: "list[Clazz]" = []) -> None:
        self.name = name
        self.glyphs = glyphs
        self.cls = cls

    def ref(self) -> str:
        return f"@{self.name}"

    def state(self) -> Line:
        return Line(f"{self.ref()} = {clazz(self.glyphs, self.cls)};")


__glyph_map = {
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


def __gly(g: str | Clazz | Sequence[str | Clazz] | None) -> str:
    if not g:
        return ""
    if isinstance(g, list):
        return " ".join([__gly(_) for _ in g])
    if isinstance(g, Clazz):
        return g.ref()
    if not isinstance(g, str):
        raise TypeError(f"{g}({type(g)}) is invalid for __gly")
    if g in __glyph_map.keys():
        return __glyph_map[g]
    return g


def gly(g: str, suffix: str | None = None):
    """
    Normalize glyph name.

    If no suffix and ``g`` has ``" "``, suffix is ``".liga"``

    >>> gly("_")
    "underline"
    >>> gly("++")
    "plus_plus.liga"
    >>> gly("--", ".suffix")
    "hyphen_hyphen.suffix"
    """
    if len(g) > 1:
        return "_".join(map(__gly, list(g))) + (suffix if suffix is not None else ".liga")
    return __gly(g) + (suffix if suffix is not None else "")


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


def create(cls: list[Clazz], content: list[Line], indent=2) -> str:
    _idt = indent * " "
    return _idt.join(
        [
            ("\n" + _idt * c.level + c.text)
            for c in ([c.state() for c in cls] + content)
        ],
    )


def feature(tag: str, content: Sequence[Line | list[Line]]) -> list[Line]:
    target = []
    for c in content:
        if isinstance(c, list):
            for i in c:
                i.indent()
                target.append(i)
        else:
            c.indent()
            target.append(c)

    return [Line(f"feature {tag} {{"), *target, Line(f"}} {tag};")]


def cv(id: int, name: str, content: list[Line]) -> list[Line]:
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


def lookup(name: str, content: list[Line]) -> list[Line]:
    for c in content:
        c.indent()
    return [Line(f"lookup {name} {{"), *content, Line(f"}} {name};")]


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

    >>> subst_list_map(["Q", "{ {"], target_suffix=".cv01")
    [
        Line("sub Q by Q.cv01;"),
        Line("sub braceleft_braceleft.liga by braceleft_braceleft.liga.cv01;")
    ]
    """
    result = []
    for g in glyphs:
        result.append(__subst(f"{g}{source_suffix}", f"{g}{target_suffix}"))

    return result


def subst_list_liga(
    source: str,
    target: str | None = None,
    lookup_name: str | None = None,
    ignores: list[Line] | None = None,
):
    """
    Generate substitution lines for target ligature.

    Default ``target`` is ``gly(source)``

    Default ``lookup_name`` is ``target``

    >>> sub_list_liga("!=")
    [
        Line("lookup exclam_equal.liga {"),
        Line("sub exclam' equal by SPC;"),
        Line("sub SPC equal' by exclam_equal.liga;"),
        Line("} lookup exclam_equal.liga;"),
    ]
    """
    source_arr = list(source)

    if not target:
        target = gly(source)

    if not lookup_name:
        lookup_name = target
    # use default param value will cache previous data
    # so manually setup default value here
    if not ignores:
        ignores = []

    subst_rules = []
    initial_prefix_len = len(source_arr) - 1
    prefix_pool = ["SPC"] * initial_prefix_len

    subst_rules.append(
        subst(
            prefix_pool,
            source[-1],
            None,
            target,
        )
    )

    for i in range(1, len(source_arr)):
        prefix_len = len(source_arr) - i - 1
        prefix = prefix_pool[:prefix_len]
        current = source_arr[prefix_len]
        suffix = source_arr[prefix_len + 1 :]
        val = subst(prefix, current, suffix, "SPC")
        subst_rules.append(val)

    final_rules = ignores
    final_rules.extend(subst_rules[::-1])
    return lookup(lookup_name, final_rules)


def ignore(
    prefix: Sequence[str | Clazz] | None,
    glyph: str,
    suffix: Sequence[str | Clazz] | None,
) -> Line:
    """
    Generate ignore line.

    >>> ignore("{", "b", ["c", "d"])
    Line("ignore sub braceleft b' c d;")
    >>> ignore("_ _", "b", cls)
    Line("ignore sub underscore underscore b' @cls;")
    """
    return Line(f"ignore sub {__prefix(prefix)}{__gly(glyph)}'{__suffix(suffix)};")


def clazz(glyphs: list[str], cls: list[Clazz] = []) -> str:
    """
    Generate inline class.

    >>> ignore(["a", "+", "@"], [cls])
    "[@cls a plus at]"
    """
    _content = [c.ref() for c in cls]
    for g in glyphs:
        _content.append(__gly(g))
    return "[" + " ".join(_content) + "]"
