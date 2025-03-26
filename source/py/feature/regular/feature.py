import source.py.feature.ast as ast
from source.py.feature.shared import basic_features
from source.py.feature.shared.cv import cv01, cv02, cv03, cv04

calt = ast.feature(
    "calt",
    [
        ast.subst_list_liga(
            "{{",
            ignores=[
                ast.ignore("{", "{", "{"),
                ast.ignore(None, "{", ["{", ast.clazz(["{", "!", "-"])]),
            ],
        ),
        ast.subst_list_liga(
            "{{--",
            ignores=[
                ast.ignore(
                    ["{", "{", "-"],
                    "-",
                    "-",
                ),
                ast.ignore(
                    "{",
                    "{",
                    ["-", "-", "-"],
                ),
            ],
        ),
    ],
)
list = [
    *basic_features,
    *calt,
    *cv01.cv01_regular,
    *cv02.cv02_regular,
    *cv03.cv03_regular,
    *cv04.cv04_regular,
]
