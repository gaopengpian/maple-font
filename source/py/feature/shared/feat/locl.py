import source.py.feature.ast as ast


locl_0 = ast.lookup(
    "locl_latin_0",
    [
        ast.script("latn"),
        ast.lang("AZE"),
        ast.subst(None, "i", None, "idotaccent"),
        ast.lang("CRT"),
        ast.subst(None, "i", None, "idotaccent"),
        ast.lang("KAZ"),
        ast.subst(None, "i", None, "idotaccent"),
        ast.lang("TAT"),
        ast.subst(None, "i", None, "idotaccent"),
        ast.lang("TRK"),
        ast.subst(None, "i", None, "idotaccent"),
    ],
)

rule_glyphs_1 = ["S", "s", "T", "t"]

locl_1 = ast.lookup(
    "locl_latin_1",
    [
        ast.script("latn"),
        ast.lang("ROM"),
        *ast.subst_list_map(
            rule_glyphs_1, source_suffix="cedilla", target_suffix="commaaccent"
        ),
        ast.lang("MOL"),
        *ast.subst_list_map(
            rule_glyphs_1, source_suffix="cedilla", target_suffix="commaaccent"
        ),
    ],
)

glyph_2 = "periodcentered"

locl_2 = ast.lookup(
    "locl_latin_2",
    [
        ast.script("latn"),
        ast.lang("CAT"),
        ast.subst("l", glyph_2, "l", f"{glyph_2}.loclCAT"),
        ast.subst("L", glyph_2, "L", f"{glyph_2}.loclCAT.case"),
    ],
)

locl_3 = ast.lookup(
    "locl_latin_3",
    [
        ast.script("latn"),
        ast.lang("NLD"),
        ast.__subst("ij acutecomb'", "ij_acute"),
        ast.__subst("IJ acutecomb'", "IJ_acute"),
    ],
)

locl_features = ast.feature(
    "locl",
    [
        locl_0,
        locl_1,
        locl_2,
        locl_3,
    ],
)
