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


glyph_dict = {
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

glyph_dict_keys = glyph_dict.keys()


def __gly(g: str | Clazz | Sequence[str | Clazz] | None) -> str:
    if not g:
        return ""
    if isinstance(g, list):
        return " ".join([__gly(_) for _ in g])
    if isinstance(g, Clazz):
        return g.ref()
    if not isinstance(g, str):
        raise TypeError(f"{g}({type(g)}) is invalid for __gly")
    if g in glyph_dict_keys:
        return glyph_dict[g]
    return g

def __arr(data: Sequence[str | Clazz]):
    if isinstance(data, str) and " " in data:
        return data.split(" ")
    return data


def __prefix(data: Sequence[str | Clazz] | None) -> str:
    if data:
        return __gly(__arr(data)) + " "
    return ""


def __suffix(data: Sequence[str | Clazz] | None) -> str:
    if data:
        return " " + __gly(__arr(data))
    return ""


def __subst(source: str, target: str) -> Line:
    return Line(f"sub {source} by {target};")


def create(content: list[Line], indent=2) -> str:
    _idt = indent * " "
    return _idt.join([("\n" + _idt * c.level + c.text) for c in content])


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


def feature_use(tag: str) -> Line:
    return Line(f"feature {tag};")


def cv(id: int, name: str, content: list[Line]) -> list[Line]:
    if id < 1 or id > 99:
        raise TypeError(
            f"id should > 0 and < 100 in Character Variants, current is {id}"
        )

    param = [
        Line("cvParameters {"),
        Line("FeatUILabelNameID {", 1),
        Line(f'name "{name}"', 2),
        Line("};", 1),
        Line("};"),
    ]
    return feature(f"cv{id:02d}", [*param, *content])


def ss(id: int, name: str, content: list[Line]) -> list[Line]:
    if id < 1 or id > 20:
        raise TypeError(f"id should > 0 and < 21 in Stylistic Sets, current is {id}")

    param = [
        Line("featureNames {"),
        Line(f'name "{name}"', 1),
        Line("};"),
    ]
    return feature(f"ss{id:02d}", [*param, *content])


def langsys_list(config: list[list[str]]) -> list[Line]:
    return [Line(f"languagesystem {script} {lang};") for script, lang in config]


def lang(lang: str) -> Line:
    return Line(f"language {lang};")


def script(script: str) -> Line:
    return Line(f"script {script};")


def lookup(tag: str, content: list[Line]) -> list[Line]:
    for c in content:
        c.indent()
    return [Line(f"lookup {tag} {{"), *content, Line(f"}} {tag};")]


def subst(
    prefix: Sequence[str | Clazz] | None,
    glyph: str,
    suffix: Sequence[str | Clazz] | None,
    replace: str,
) -> Line:
    return __subst(
        f"{__prefix(prefix)}{__gly(glyph)}'{__suffix(suffix)}", f"{__gly(replace)}"
    )


def subst_list_map(glyphs: list[str], replace_suffix: str) -> list[Line]:
    result = []
    for g in glyphs:
        if " " in g:
            _g = "_".join(map(__gly, g.split(" "))) + ".liga"
        else:
            _g = __gly(g)
        result.append(__subst(_g, f"{_g}{replace_suffix}"))

    return result


def subst_list_liga(
    source: str,
    target: str | None = None,
    ignores: list[Line] | None = None,
):
    """
    Generate substitutions for ligature
    """
    source_arr = list(source)

    if not target:
        target = __gly("_".join(map(__gly, source_arr)))

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
    return final_rules


def ignore(
    prefix: Sequence[str | Clazz] | None,
    glyph: str,
    suffix: Sequence[str | Clazz] | None,
) -> Line:
    return Line(f"ignore sub {__prefix(prefix)}{__gly(glyph)}'{__suffix(suffix)};")


def clazz(glyphs: list[str], cls: list[Clazz] = []) -> str:
    _content = [c.ref() for c in cls]
    for g in glyphs:
        _content.append(__gly(g))
    return "[" + " ".join(_content) + "]"
