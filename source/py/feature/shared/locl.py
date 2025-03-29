import source.py.feature.ast as ast


i_acc = ast.subst(None, "i", None, "idotaccent")
locl_0 = ast.lookup(
    "locl_latin_0",
    None,
    [
        ast.script("latn"),
        ast.lang("AZE"),
        i_acc,
        ast.lang("CRT"),
        i_acc,
        ast.lang("KAZ"),
        i_acc,
        ast.lang("TAT"),
        i_acc,
        ast.lang("TRK"),
        i_acc,
    ],
)

st_acc = ast.subst_list_map(
    ["S", "s", "T", "t"], source_suffix="cedilla", target_suffix="commaaccent"
)

locl_1 = ast.lookup(
    "locl_latin_1",
    None,
    [
        ast.script("latn"),
        ast.lang("ROM"),
        *st_acc,
        ast.lang("MOL"),
        *st_acc,
    ],
)

glyph_2 = "periodcentered"

locl_2 = ast.lookup(
    "locl_latin_2",
    None,
    [
        ast.script("latn"),
        ast.lang("CAT"),
        ast.subst(["l"], glyph_2, ["l"], f"{glyph_2}.loclCAT"),
        ast.subst(["L"], glyph_2, ["L"], f"{glyph_2}.loclCAT.case"),
    ],
)

locl_3 = ast.lookup(
    "locl_latin_3",
    None,
    [
        ast.script("latn"),
        ast.lang("NLD"),
        ast.subst("ij", "acutecomb", None, "ij_acute"),
        ast.subst("IJ", "acutecomb", None, "IJ_acute"),
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
