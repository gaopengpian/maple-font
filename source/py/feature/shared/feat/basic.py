import source.py.feature.ast as ast
from source.py.feature.shared.feat.number import number_features
from source.py.feature.shared.feat.locl import locl_features

aalt_features = ast.feature(
    "aalt",
    [
        ast.feature_use("calt"),
        ast.feature_use("locl"),
        ast.feature_use("subs"),
        ast.feature_use("sinf"),
        ast.feature_use("sups"),
        ast.feature_use("frac"),
        ast.feature_use("ordn"),
        ast.feature_use("case"),
        ast.feature_use("zero"),
    ],
)

case_features = ast.feature("case", ast.subst_list_map(
    [
        "colon",
        "periodcentered.loclCAT",
        "dieresiscomb",
        "dotaccentcomb",
        "gravecomb",
        "acutecomb",
        "hungarumlautcomb",
        "circumflexcomb",
        "caroncomb",
        "brevecomb",
        "ringcomb",
        "tildecomb",
        "macroncomb",
        "hookabovecomb",
        "dblgravecomb",
        "commaturnedabovecomb",
        "horncomb",
        "dotbelowcomb",
        "commaaccentcomb",
        "cedillacomb",
        "ogonekcomb",
        "dieresis",
        "dotaccent",
        "grave",
        "acute",
        "hungarumlaut",
        "circumflex",
        "caron",
        "breve",
        "ring",
        "tilde",
        "macron",
        "tonos",
        "brevecomb_acutecomb",
        "brevecomb_gravecomb",
        "brevecomb_hookabovecomb",
        "brevecomb_tildecomb",
        "circumflexcomb_acutecomb",
        "circumflexcomb_gravecomb",
        "circumflexcomb_hookabovecomb",
        "circumflexcomb_tildecomb",
    ],
    ".case",
))


basic_features: list[ast.Line] = [
    *aalt_features,
    *number_features,
    *case_features,
    *locl_features,
]
