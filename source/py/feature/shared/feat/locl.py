from copy import deepcopy
import source.py.feature.ast as ast

rule_0 = ast.subst(None, "i", None, "idotaccent")

locl_0 = ast.lookup(
    "locl_latin_0",
    [
        ast.script("latn"),
        ast.lang("AZE"),
        deepcopy(rule_0),
        ast.lang("CRT"),
        deepcopy(rule_0),
        ast.lang("KAZ"),
        deepcopy(rule_0),
        ast.lang("TAT"),
        deepcopy(rule_0),
        ast.lang("TRK"),
        deepcopy(rule_0),
    ],
)

rule_1 = [
    ast.subst(None, f"{p}cedilla", None, f"{p}commaaccent")
    for p in ["S", "s", "T", "t"]
]

locl_1 = ast.lookup(
    "locl_latin_1",
    [
        ast.script("latn"),
        ast.lang("ROM"),
        *deepcopy(rule_1),
        ast.lang("MOL"),
        *deepcopy(rule_1),
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
