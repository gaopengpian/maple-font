import source.py.feature.ast as ast
from source.py.feature.regular.clazz import hex_letter, cls_letters_list
from source.py.feature.shared import basic_features, basic_features_cn
from source.py.feature.shared.calt import get_calt_regular
from source.py.feature.shared.cv import cv01, cv02, cv03, cv04, cv96, cv97, cv98, cv99
from source.py.feature.shared.ss import ss01, ss02, ss03, ss04, ss05, ss07, ss08

calt = ast.feature(
    "calt",
    get_calt_regular(cls_letters_list, hex_letter),
)

cv_list = [
    *cv01.cv01_feat_regular,
    *cv02.cv02_feat_regular,
    *cv03.cv03_feat_regular,
    *cv04.cv04_feat_regular,
]

cv_list_cn = [
    *cv96.cv96_feat_cn,
    *cv97.cv97_feat_cn,
    *cv98.cv98_feat_cn,
    *cv99.cv99_feat_cn,
]

ss_list = [
    *ss01.ss01_feat,
    *ss02.ss02_feat,
    *ss03.ss03_feat,
    *ss04.ss04_feat,
    *ss05.ss05_feat,
    *ss07.ss07_feat,
    *ss08.ss08_feat,
]

feature_list = [
    *basic_features,
    *calt,
    *cv_list,
    *ss_list,
]

feature_list_cn = [
    *basic_features_cn,
    *cv_list_cn,
]
