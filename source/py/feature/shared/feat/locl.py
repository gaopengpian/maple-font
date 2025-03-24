import source.py.feature.utils as fea

rule_0 = fea.subst(None, "i", None, "idotaccent")

locl_0 = fea.def_lookup(
    "locl_latin_0",
    [
        fea.use_script("latn"),
        fea.use_lang("AZE"),
        rule_0,
        fea.use_lang("CRT"),
        rule_0,
        fea.use_lang("KAZ"),
        rule_0,
        fea.use_lang("TAT"),
        rule_0,
        fea.use_lang("TRK"),
        rule_0,
    ],
)

rule_1 = [
    fea.subst(None, f"{p}cedilla", None, f"{p}commaaccent")
    for p in ["S", "s", "T", "t"]
]

locl_1 = fea.def_lookup(
    "locl_latin_1",
    [
        fea.use_script("latn"),
        fea.use_lang("ROM"),
        *rule_1,
        fea.use_lang("MOL"),
        *rule_1,
    ],
)

glyph_2 = "periodcentered"

locl_2 = fea.def_lookup(
    "locl_latin_2",
    [
        fea.use_script("latn"),
        fea.use_lang("CAT"),
        fea.subst("l", glyph_2, "l", f"{glyph_2}.loclCAT"),
        fea.subst("L", glyph_2, "L", f"{glyph_2}.loclCAT.case"),
    ],
)

locl_3 = fea.def_lookup(
    "locl_latin_3",
    [
        fea.use_script("latn"),
        fea.use_lang("NLD"),
        fea.ast.LigatureSubstStatement(
            prefix=fea.parse_glyphs_array("ij"),
            glyphs=fea.parse_glyphs_array("acutecomb"),
            suffix=[],
            replacement=fea.glyph("ij_acute"),
            forceChain=False,
        ),
        fea.ast.LigatureSubstStatement(
            prefix=fea.parse_glyphs_array("IJ"),
            glyphs=fea.parse_glyphs_array("acutecomb"),
            suffix=[],
            replacement=fea.glyph("IJ_acute"),
            forceChain=False,
        ),
    ],
)

locl_features = [
    locl_0,
    locl_1,
    locl_2,
    locl_3,
]