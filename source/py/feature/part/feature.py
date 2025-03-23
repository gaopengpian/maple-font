import source.py.feature.part.utils as fea
import source.py.feature.part.clazz as cls  # noqa: F401

aalt = [
    fea.ref_feature("calt"),
    fea.ref_feature("locl"),
    fea.ref_feature("subs"),
    fea.ref_feature("sinf"),
    fea.ref_feature("sups"),
    fea.ref_feature("frac"),
    fea.ref_feature("ordn"),
    fea.ref_feature("case"),
    fea.ref_feature("zero"),
]
zero = [fea.subst("zero", "zero.zero")]
calt = [
    fea.liga(
        "{ {",
        ignore=[
            fea.ignore("{", "{", "{"),
            fea.ignore(None, "{", fea.clazz("{ ! -")),
        ],
    ),
    fea.liga(
        "{ { - -",
        ignore=[
            fea.ignore(
                "{ { -",
                "-",
                "-",
            ),
            fea.ignore(
                "{",
                "{",
                "- - -",
            ),
        ],
    ),
]
list = fea.create_features({"aalt": aalt, "zero": zero, "calt": calt})
