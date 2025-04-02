import source.py.feature.ast as ast
from source.py.feature.shared.ccmp import ccmp_features, ccmp_features_cn
from source.py.feature.shared.number import number_features
from source.py.feature.shared.locl import locl_features, locl_features_cn


aalt_features = ast.feature(
    "aalt",
    [
        ast.use_feature("calt"),
        ast.use_feature("locl"),
        ast.use_feature("subs"),
        ast.use_feature("sinf"),
        ast.use_feature("sups"),
        ast.use_feature("frac"),
        ast.use_feature("ordn"),
        ast.use_feature("case"),
        ast.use_feature("zero"),
    ],
)

case_features = ast.feature(
    "case",
    ast.subst_map(
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
        target_suffix=".case",
    ),
)


base_features = [
    *aalt_features,
    *number_features,
    *case_features,
    *ccmp_features,
    *locl_features,
]

base_features_cn = [
    *aalt_features,
    *number_features,
    *case_features,
    *ccmp_features_cn,
    *locl_features_cn,
]
