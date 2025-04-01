from source.py.feature import ast


def get_lookup():
    return [
        ast.subst_list_liga(
            "<~",
            header=[
                ast.ignore("<", "<", "~"),
                ast.ignore(None, "<", ["~", ast.clazz(["~", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "~>",
            header=[
                ast.ignore("~", "~", ">"),
                ast.ignore(None, "~", ["~", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "~~",
            header=[
                ast.ignore(ast.clazz(["~", "<"]), "~", "~"),
                ast.ignore(None, "~", ["~", ast.clazz(["~", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "<~>",
            header=[
                ast.ignore("<", "<", ["~", ">"]),
                ast.ignore(None, "<", ["~", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "<~~",
            header=[
                ast.ignore("<", "<", ["~", "~"]),
                ast.ignore(None, "<", ["~", "~", ast.clazz(["~", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "~~>",
            header=[
                ast.ignore(ast.clazz(["~", ">"]), "~", ["~", ">"]),
                ast.ignore(None, "~", ["~", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "-~",
            header=[
                ast.ignore("-", "-", "~"),
                ast.ignore(None, "-", ["~", "~"]),
            ],
        ),
        ast.subst_list_liga(
            "~-",
            header=[
                ast.ignore("~", "~", "-"),
                ast.ignore(None, "~", ["-", "-"]),
            ],
        ),
        ast.subst_list_liga(
            "~@",
            header=[
                ast.ignore("~", "~", "@"),
                ast.ignore(None, "~", ["@", "@"]),
            ],
        ),
    ]
