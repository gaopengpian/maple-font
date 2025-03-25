import source.py.feature.ast as ast
from source.py.feature.shared.feat.number import number_features
from source.py.feature.shared.feat.locl import locl_features

def use_feat(tag: str):
    return ast.Line(f"feature {tag};")


aalt_features = ast.feature(
    "aalt",
    [
        use_feat("calt"),
        use_feat("locl"),
        use_feat("subs"),
        use_feat("sinf"),
        use_feat("sups"),
        use_feat("frac"),
        use_feat("ordn"),
        use_feat("case"),
        use_feat("zero"),
    ],
)

case_features = ast.feature(
    "case",
    ast.subst_list_map(
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


basic_features: list[ast.Line] = [
    *aalt_features,
    *number_features,
    *case_features,
    *locl_features,
]
