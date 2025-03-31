from source.py.feature import ast
from source.py.feature.shared.clazz import normal_separator


def get_lookup():
    return [
        ast.subst_list_liga(
            "<=>",
            ignores=[
                ast.ignore("<", "<", ["=", ">"]),
                ast.ignore(["(", "?"], "<", ["=", ">"]),
                ast.ignore(None, "<", ["=", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "<==>",
            ignores=[
                ast.ignore("<", "<", ["=", "=", ">"]),
                ast.ignore(["(", "?"], "<", ["=", "=", ">"]),
                ast.ignore(None, "<", ["=", "=", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            ">=",
            ignores=[
                ast.ignore(ast.clazz([">", "="]), ">", "="),
                ast.ignore(
                    None, ">", ast.clazz(["<", ">", "=", "?"], [normal_separator])
                ),
            ],
        ),
        ast.subst_list_liga(
            "<=",
            ignores=[
                ast.ignore(None, "<", ast.clazz(["<", ">", "="], [normal_separator])),
                ast.ignore(ast.clazz(["<", "="]), "<", "="),
                ast.ignore(["(", "?"], "<", "="),
            ],
        ),
        ast.subst_list_liga(
            "<==",
            ignores=[
                ast.ignore("<", "<", ["=", "="]),
                ast.ignore(["(", "?"], "<", ["=", "="]),
                ast.ignore(None, "<", ["=", "=", ast.clazz(["=", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "==>",
            ignores=[
                ast.ignore(ast.clazz(["[", "="]), "=", ["=", ">"]),
                ast.ignore(["(", "?", "<"], "=", ["=", ">"]),
                ast.ignore(["(", "?"], "=", ["=", ">"]),
                ast.ignore(None, "=", ["=", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "=>",
            ignores=[
                ast.ignore(ast.clazz(["[", "=", ">", "|"]), "=", ">"),
                ast.ignore(["(", "?", "<"], "=", ">"),
                ast.ignore(["(", "?"], "=", ">"),
                ast.ignore(None, "=", [">", ast.clazz(["=", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "<=<",
            ignores=[
                ast.ignore(ast.clazz(["<", "="]), "<", ["=", "<"]),
                ast.ignore(["(", "?"], "<", ["=", "<"]),
                ast.ignore(None, "<", ["=", "<", ast.clazz(["<", "="])]),
            ],
        ),
        ast.subst_list_liga(
            ">=>",
            ignores=[
                ast.ignore(ast.clazz([">", "="]), ">", ["=", ">"]),
                ast.ignore(None, "=", ["=", ">", ast.clazz([">", "="])]),
            ],
        ),
        ast.subst_list_liga(
            "<=|",
            ignores=[
                ast.ignore("<", "<", ["=", "|"]),
                ast.ignore(["(", "?"], "<", ["=", "|"]),
                ast.ignore(
                    None,
                    "<",
                    ["=", "|", ast.clazz(["<", ">", "="], [normal_separator])],
                ),
            ],
        ),
        ast.subst_list_liga(
            "|=>",
            ignores=[
                ast.ignore(
                    ast.clazz(["<", ">", "="], [normal_separator]), "|", ["=", ">"]
                ),
                ast.ignore(None, "|", ["=", ">", ">"]),
            ],
        ),
    ]
