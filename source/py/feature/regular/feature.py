import source.py.feature.ast as ast
from source.py.feature.shared.feat.basic import basic_features
from source.py.feature.shared.feat.cv.cv01 import cv01

calt = ast.feature(
    "calt",
    [
        *ast.subst_list_liga(
            "{{",
            ignores=[
                ast.ignore("{", "{", "{"),
                ast.ignore(None, "{", ast.clazz(["{", "!", "-"])),
            ],
        ),
        *ast.subst_list_liga(
            "{{--",
            ignores=[
                ast.ignore(
                    "{ { -",
                    "-",
                    "-",
                ),
                ast.ignore(
                    "{",
                    "{",
                    "- - -",
                ),
            ],
        ),
    ],
)
list = [*basic_features, *calt, *cv01]
