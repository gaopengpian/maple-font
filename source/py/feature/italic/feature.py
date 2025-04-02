import source.py.feature.ast as ast
from source.py.feature.italic.clazz import hex_letter, cls_letters_list
from source.py.feature.shared import base_features
from source.py.feature.shared.calt import get_calt_italic
from source.py.feature.shared.cv import (
    cv01,
    cv04,
    cv31,
    cv32,
    cv33,
    cv34,
    cv35,
    cv36,
    cv37,
    cv96,
    cv97,
    cv98,
    cv99,
)
from source.py.feature.shared.ss import ss01, ss02, ss03, ss04, ss05, ss06, ss07, ss08

calt = ast.feature(
    "calt",
    get_calt_italic(cls_letters_list, hex_letter),
)

cv_list = [
    *cv01.cv01_feat_italic,
    *cv04.cv04_feat_italic,
    *cv31.cv31_feat_italic,
    *cv32.cv32_feat_italic,
    *cv33.cv33_feat_italic,
    *cv34.cv34_feat_italic,
    *cv35.cv35_feat_italic,
    *cv36.cv36_feat_italic,
    *cv37.cv37_feat_italic,
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
    *ss06.ss06_feat,
    *ss07.ss07_feat,
    *ss08.ss08_feat,
]

feature_list = [
    *base_features,
    *calt,
    *cv_list,
    *ss_list,
]

feature_list_cn = [
    *base_features,
    *calt,
    *cv_list,
    *ss_list,
]