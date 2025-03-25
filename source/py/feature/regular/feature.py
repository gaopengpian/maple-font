import source.py.feature.utils as fea
from source.py.feature.shared.feat.basic import basic_features
from source.py.feature.shared.feat.cv.cv01 import cv01

calt = [
    fea.liga(
        "{ {",
        ignores=[
            ["{", "{", "{"],
            [None, "{", fea.clazz("{ ! -")],
        ],
    ),
    fea.liga(
        "{ { - -",
        ignores=[
            [
                "{ { -",
                "-",
                "-",
            ],
            [
                "{",
                "{",
                "- - -",
            ],
        ],
    ),
]
list = fea.create_features({
    **basic_features,
    "calt": calt
})
list.append(cv01)