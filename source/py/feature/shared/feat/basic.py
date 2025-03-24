import source.py.feature.utils as fea
from source.py.feature.shared.feat.number import number_features
from source.py.feature.shared.feat.locl import locl_features

aalt_features = [
    fea.use_feature("calt"),
    fea.use_feature("locl"),
    fea.use_feature("subs"),
    fea.use_feature("sinf"),
    fea.use_feature("sups"),
    fea.use_feature("frac"),
    fea.use_feature("ordn"),
    fea.use_feature("case"),
    fea.use_feature("zero"),
]

case_features = fea.subst_list(
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
)


basic_features = {
    "aalt": aalt_features,
    **number_features,
    "case": case_features,
    "locl": locl_features,
}
