from collections.abc import Sequence
from fontTools.feaLib import ast as ast
from fontTools.feaLib.parser import Parser
from io import StringIO

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

glyph_dict_keys = list(glyph_dict.keys())


def to_glyph_name(short: str):
    if short in glyph_dict_keys:
        return glyph_dict[short]
    if short[0] in glyph_dict_keys:
        return glyph_dict[short[0]] + short[1:]
    return short


def glyph(
    g: str
    | ast.GlyphClassDefinition
    | ast.GlyphClass
    | Sequence[str | ast.GlyphClassDefinition | ast.GlyphClass],
):
    if isinstance(g, list):
        return ast.GlyphClass([glyph(x) for x in g])
    if isinstance(g, ast.GlyphClassDefinition):
        return ast.GlyphClassName(g)
    if isinstance(g, ast.GlyphClass):
        return g
    if isinstance(g, str):
        return ast.GlyphName(to_glyph_name(g))

    raise TypeError(f"Unexpected type for glyph: {type(g)}")


def clazz(glyphs: str | list[str]):
    _glyphs = glyphs if isinstance(glyphs, list) else glyphs.split(" ")
    return ast.GlyphClass([ast.GlyphName(to_glyph_name(g)) for g in _glyphs])


def def_clazz(
    name: str,
    glyphs: list[str],
    classes: list[ast.GlyphClassDefinition] | None = None,
):
    # No need to use `to_glyph_name` here, as the glyphs in
    # class definition are rarely reused, so just assert
    # that they are already in the target name.
    g = ast.GlyphClass([ast.GlyphName(to_glyph_name(glyph)) for glyph in glyphs])
    if classes:
        for d in classes:
            g.add_class(ast.GlyphClassName(d))
    return ast.GlyphClassDefinition(
        name=name,
        glyphs=g,
    )


def parse_glyphs_array(
    data: str
    | ast.GlyphClassDefinition
    | ast.GlyphClass
    | Sequence[str | ast.GlyphClassDefinition | ast.GlyphClass]
    | None,
):
    if isinstance(data, list):
        return [glyph(g) for g in data]
    if data:
        return [glyph(data)]
    return []


def ignore(
    prefix: str
    | ast.GlyphClassDefinition
    | ast.GlyphClass
    | Sequence[str | ast.GlyphClassDefinition | ast.GlyphClass]
    | None,
    glyphs: str | ast.GlyphClassDefinition | ast.GlyphClass | None,
    suffix: str
    | ast.GlyphClassDefinition
    | ast.GlyphClass
    | Sequence[str | ast.GlyphClassDefinition | ast.GlyphClass]
    | None,
):
    if not glyphs:
        raise Exception(f"glyphs cannot be none, prefix={prefix}, suffix={suffix}")
    return ast.IgnoreSubstStatement(
        chainContexts=[
            (
                parse_glyphs_array(
                    prefix.split(" ") if isinstance(prefix, str) else prefix
                ),
                parse_glyphs_array(
                    glyphs.split(" ") if isinstance(glyphs, str) else glyphs
                ),
                parse_glyphs_array(
                    suffix.split(" ") if isinstance(suffix, str) else suffix
                ),
            )
        ]
    )


def subst(
    prefix: str
    | ast.GlyphClass
    | ast.GlyphClassDefinition
    | Sequence[str | ast.GlyphClassDefinition]
    | None,
    source: str
    | ast.GlyphClass
    | ast.GlyphClassDefinition,
    suffix: str
    | ast.GlyphClass
    | ast.GlyphClassDefinition
    | Sequence[str | ast.GlyphClassDefinition]
    | None,
    target: str | ast.GlyphClass | ast.GlyphClassDefinition,
):
    return ast.SingleSubstStatement(
        glyphs=[glyph(source)],
        replace=[glyph(target)],
        prefix=parse_glyphs_array(prefix),
        suffix=parse_glyphs_array(suffix),
        forceChain=False,
    )


def subst_list(
    glyphs: list[str],
    ext: str,
):
    """
    Generate list of ``sub {glyph} by {glyph}{ext};``

    Built-in convert process:
        convert ``#`` to ``numbersign``

        convert ``# #`` to ``numbersign_numbersign.liga``
    """

    def parse_liga_name(name: str):
        if " " in name:
            return "_".join(map(to_glyph_name, name.split(" "))) + ".liga"
        return to_glyph_name(name)

    result = []
    for g in glyphs:
        parsed_name = parse_liga_name(g)
        result.append(subst(
            source=parsed_name,
            target=f"{parsed_name}{ext}",
            prefix=None,
            suffix=None,
        ))

    return result


def name_by_glyphs(source: list[str]):
    return "_".join(map(to_glyph_name, source)) + ".liga"


def liga_base(
    source: list[str],
    target: str | None = None,
    ignores: list[ast.IgnoreSubstStatement] | None = None,
):
    """
    Generate substitutions for ligature
    """
    if not target:
        target = name_by_glyphs(source)

    # use default param value will cache previous data
    # so manually setup default value here
    if not ignores:
        ignores = []

    subst_rules = []
    initial_prefix_len = len(source) - 1
    prefix_pool = ["SPC"] * initial_prefix_len

    subst_rules.append(
        subst(
            source=source[-1],
            target=target,
            prefix=prefix_pool,
            suffix=None,
        )
    )

    for i in range(1, len(source)):
        prefix_len = len(source) - i - 1
        prefix = prefix_pool[:prefix_len]
        current = source[prefix_len]
        suffix = source[prefix_len + 1 :]
        val = subst(source=current, target="SPC", prefix=prefix, suffix=suffix)
        subst_rules.append(val)

    final_rules = ignores
    final_rules.extend(subst_rules[::-1])
    return final_rules


def liga(
    source: str,
    target: str | None = None,
    name: str | None = None,
    ignores: list[Sequence[str | ast.GlyphClassDefinition | ast.GlyphClass | None]]
    | None = None,
):
    """
    Generate substitutions for ligature with lookup
    """
    if not name:
        name = name_by_glyphs(source.split(" "))
    if not target:
        target = name

    return def_lookup(
        name,
        liga_base(
            source.split(" "),
            target,
            [ignore(conf[0], conf[1], conf[2]) for conf in (ignores or [])],
        ),
    )


def def_lookup(
    name: str,
    config: Sequence[
        ast.SingleSubstStatement
        | ast.IgnoreSubstStatement
        | ast.LanguageStatement
        | ast.ScriptStatement
        | ast.LigatureSubstStatement
    ]
    | None = None,
):
    lookup = ast.LookupBlock(name=name)
    if config:
        lookup.statements.extend(config)
    return lookup


def use_feature(name: str):
    return ast.FeatureReferenceStatement(name)


def def_feature(
    name: str,
    config: Sequence[
        ast.LookupBlock
        | ast.SingleSubstStatement
        | ast.FeatureReferenceStatement
        | ast.NestedBlock
    ],
):
    block = ast.FeatureBlock(name=name)
    if config:
        block.statements.extend(config)
    return block


def def_cv(
    id: int, desc: str, config: Sequence[ast.LookupBlock | ast.SingleSubstStatement]
) -> ast.FeatureBlock:
    if id < 1 or id > 99:
        raise TypeError(f"id should > 0 and < 100, current is {id}")

    tag = f"cv{id:02d}"
    io = StringIO(
        "feature "
        + tag
        + '{cvParameters{FeatUILabelNameID{name "'
        + desc
        + '";};};}'
        + tag
        + ";"
    )
    result: ast.FeatureBlock = Parser(io).parse().statements[0]
    result.statements.extend(config)
    return result

def def_ss(
    id: int, desc: str, config: Sequence[ast.LookupBlock | ast.SingleSubstStatement]
) -> ast.FeatureBlock:
    if id < 1 or id > 20:
        raise TypeError(f"id should > 0 and < 21, current is {id}")

    tag = f"ss{id:02d}"
    io = StringIO(
        "feature "
        + tag
        + '{featureNames{name "'
        + desc
        + '";};}'
        + tag
        + ";"
    )
    result: ast.FeatureBlock = Parser(io).parse().statements[0]
    result.statements.extend(config)
    return result


def use_script(script: str):
    return ast.ScriptStatement(script)


def use_lang(lang: str):
    return ast.LanguageStatement(f"{lang:4}")


def def_lang(script: str, lang: str):
    return ast.LanguageSystemStatement(script, lang)


def create(
    class_list: list[ast.GlyphClassDefinition] | dict[str, ast.GlyphClassDefinition],
    lang_list: list[ast.LanguageSystemStatement],
    feature_list: list[ast.FeatureBlock],
):
    fea_file = ast.FeatureFile()
    if isinstance(class_list, dict):
        class_list = list(class_list.values())
    fea_file.statements.extend(class_list)
    fea_file.statements.extend(lang_list)
    fea_file.statements.extend(feature_list)
    return fea_file


def create_classes(config: dict[str, list[str]]):
    return {i: def_clazz(name=i, glyphs=config[i]) for i in config.keys()}


def create_features(
    config: dict[
        str,
        Sequence[
            ast.LookupBlock | ast.SingleSubstStatement | ast.FeatureReferenceStatement
        ],
    ],
):
    return [def_feature(name=n, config=config[n]) for n in config.keys()]


def create_languages(
    config: list[list[str]],
):
    return [def_lang(item[0], item[1]) for item in config]
