import source.py.feature.ast as ast
from source.py.feature.shared import basic_features
from source.py.feature.shared.cv import cv01, cv02, cv03, cv04
from source.py.feature.shared.ss import ss01, ss02, ss03, ss04, ss05, ss07, ss08

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
    *ss01.ss01,
    *ss02.ss02,
    *ss03.ss03,
    *ss04.ss04,
    *ss05.ss05,
    *ss07.ss07,
    *ss08.ss08,
]
