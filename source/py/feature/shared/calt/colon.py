from source.py.feature import ast


def get_lookup():
    return [
        ast.subst_list_liga(
            "::",
            ignores=[
                ast.ignore(":", ":", ":"),
                ast.ignore(None, ":", [":", ast.clazz(["=", ":"])]),
            ],
        ),
        ast.subst_list_liga(
            ":::",
            ignores=[
                ast.ignore(":", ":", [":", ":"]),
                ast.ignore(None, ":", [":", ":", ":"]),
            ],
        ),
        ast.subst_list_liga(
            ":?",
            ignores=[
                ast.ignore(":", ":", "?"),
                ast.ignore(None, ":", ["?", ast.clazz(["?", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            ":?>",
            ignores=[
                ast.ignore(":", ":", ["?", ">"]),
                ast.ignore(None, ":", ["?", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            ":=",
            ignores=[
                ast.ignore(ast.clazz(["=", ":"]), ":", "="),
                ast.ignore(None, ":", ["=", ast.clazz(["=", ":"])]),
            ],
        ),
        ast.subst_list_liga(
            "=:",
            ignores=[
                ast.ignore(ast.clazz(["=", ":"]), "=", ":"),
                ast.ignore("=", ":", ast.clazz(["=", ":"])),
            ],
        ),
        ast.subst_list_liga(
            ":=:",
            ignores=[
                ast.ignore(ast.clazz(["=", ":", "<", ">", "?"]), "=", ["=", ":"]),
                ast.ignore(None, ":", ["=", ":", ast.clazz(["=", ":", "<", ">", "?"])]),
            ],
        ),
        ast.subst_list_liga(
            "=:=",
            ignores=[
                ast.ignore("=", "=", [":", "="]),
                ast.ignore(["(", "?", "="], ":", "="),
                ast.ignore(None, "=", [":", "=", "="]),
            ],
        ),
        ast.subst_list_liga(
            "<:",
            ignores=[
                ast.ignore("<", "<", ":"),
                ast.ignore(None, "<", [":", ast.clazz(["<", ":", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            ":>",
            ignores=[
                ast.ignore(ast.clazz([":", "<", ">"]), ":", ">"),
                ast.ignore(None, ":", [">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            ":<",
            ignores=[
                ast.ignore(ast.clazz([":", "<"]), ":", "<"),
                ast.ignore(None, ":", ["<", ast.clazz(["<", "/", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "<:<",  # scala / haskell
            ignores=[
                ast.ignore("<", "<", [":", "<"]),
                ast.ignore(None, "<", [":", "<", "<"]),
            ],
        ),
        ast.subst_list_liga(
            ">:>",  # scala / haskell
            ignores=[
                ast.ignore(">", ">", [":", ">"]),
                ast.ignore(None, ">", [":", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "::=",
            ignores=[
                ast.ignore(":", ":", [":", "="]),
                ast.ignore(None, ":", [":", "=", "="]),
            ],
        ),
    ]
