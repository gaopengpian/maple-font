from source.py.feature import ast
from source.py.feature.shared.clazz import digit, uppercase


def get_upper_lookup():
    pre = ast.clazz(cls=[digit, uppercase])
    dbls = "germandbls"
    dbls_calt = f"{dbls}.calt"
    return [
        ast.subst(pre, ":", pre, ast.gly(":", ".case")),
        ast.lookup(
            "uppercaseSharpS",
            "",
            [
                ast.subst([uppercase, uppercase], dbls, None, dbls_calt),
                ast.subst(None, dbls, uppercase, dbls_calt),
            ],
        ),
    ]
