import source.py.feature.utils as fea
from source.py.feature.shared.feat.basic import basic_features

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
