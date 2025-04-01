from source.py.feature import ast


def get_lookup():
    return [
        ast.subst_list_liga(
            "<|||",
            header=[
                ast.ignore("<", "<", ["|", "|", "|"]),
                ast.ignore(None, "<", ["|", "|", "|", ast.clazz(["|", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "<||",
            header=[
                ast.ignore("<", "<", ["|", "|"]),
                ast.ignore(None, "<", ["|", "|", ast.clazz(["|", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "<|",
            header=[
                ast.ignore("<", "<", "|"),
                ast.ignore(None, "<", ["|", ast.clazz(["|", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "-|",
            header=[
                ast.ignore(ast.clazz(["-", "<"]), "-", "|"),
                ast.ignore("-", "-", "|"),
            ],
        ),
        ast.subst_list_liga(
            "<|>",
            header=[
                ast.ignore("<", "<", ["|", ">"]),
                ast.ignore(None, "<", ["|", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "_|_",
            header=[
                ast.ignore(ast.clazz(["_", "[", ","]), "_", ["|", "_"]),
                ast.ignore(None, "_", ["|", "_", "_"]),
            ],
        ),
        ast.subst_list_liga(
            "|||>",
            header=[
                ast.ignore("|", "|", ["|", "|", ">"]),
                ast.ignore(None, "|", ["|", "|", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "||>",
            header=[
                ast.ignore(ast.clazz(["-", "<"]), "|", ["|", ">"]),
                ast.ignore(None, "|", ["|", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "|>",
            header=[
                ast.ignore(ast.clazz(["-", "<"]), "|", ">"),
                ast.ignore(None, "|", [">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "||-",
            header=[
                ast.ignore("|", "|", ["-", "-"]),
                ast.ignore(None, "|", ["|", "-", "-"]),
            ],
        ),
        ast.subst_list_liga(
            "|-",
            header=[
                ast.ignore("|", "|", "-"),
                ast.ignore(None, "|", ["-", ast.clazz(["-", ">"])]),
            ],
        ),
    ]
