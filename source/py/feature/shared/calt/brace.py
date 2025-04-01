from source.py.feature import ast


def get_lookup():
    return [
        ast.subst_list_liga(
            "{{",
            header=[
                ast.ignore("{", "{", "{"),
                ast.ignore(None, "{", ["{", ast.clazz(["{", "!", "-"])]),
            ],
        ),
        ast.subst_list_liga(
            "{|",
            header=[
                ast.ignore("{", "{", "|"),
                ast.ignore(None, "{", ["|", ast.clazz(["|", "}"])]),
            ],
        ),
        ast.subst_list_liga(
            "}}",
            header=[
                ast.ignore(None, "}", ["}", "}"]),
                ast.ignore(ast.clazz(["}", "-"]), "}", "}"),
            ],
        ),
        ast.subst_list_liga(
            "|}",
            header=[
                ast.ignore(None, "|", ["|", "}"]),
                ast.ignore(ast.clazz(["{", "|"]), "|", "}"),
            ],
        ),
        ast.subst_list_liga(
            "{{--",
            header=[
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
        ast.subst_list_liga(
            "--}}",
            header=[
                ast.ignore(
                    "-",
                    "-",
                    ["-", "}", "}"],
                ),
                ast.ignore(
                    None,
                    "-",
                    ["-", "}", "}", "}"],
                ),
            ],
        ),
    ]
