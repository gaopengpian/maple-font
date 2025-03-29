from source.py.feature import ast


def get_brace_lookup():
    return [
        ast.subst_list_liga(
            "{{",
            ignores=[
                ast.ignore("{", "{", "{"),
                ast.ignore(None, "{", ["{", ast.clazz(["{", "!", "-"])]),
            ],
        ),
        ast.subst_list_liga(
            "{|",
            ignores=[
                ast.ignore("{", "{", "|"),
                ast.ignore(None, "{", ["|", ast.clazz(["|", "}"])]),
            ],
        ),
        ast.subst_list_liga(
            "}}",
            ignores=[
                ast.ignore(None, "}", ["}", "}"]),
                ast.ignore(ast.clazz(["}", "-"]), "}", "}"),
            ],
        ),
        ast.subst_list_liga(
            "|}",
            ignores=[
                ast.ignore(None, "|", ["|", "}"]),
                ast.ignore(ast.clazz(["{", "|"]), "|", "}"),
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
        ast.subst_list_liga(
            "--}}",
            ignores=[
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
