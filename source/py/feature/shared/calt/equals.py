from source.py.feature import ast


def get_lookup():
    return [
        ast.subst_list_liga(
            "==",
            banner=[
                ast.ignore("=", "=", "="),
                ast.ignore(["(", "?"], "=", "="),
                ast.ignore(["(", "?", "<"], "=", "="),
                ast.ignore(None, "=", ["=", ast.clazz(["=", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "===",
            banner=[
                ast.ignore("=", "=", ["=", "="]),
                ast.ignore(["(", "?"], "=", ["=", "="]),
                ast.ignore(["(", "?", "<"], "=", ["=", "="]),
                ast.ignore(None, "=", ["=", "=", ast.clazz(["=", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "!=",
            banner=[
                ast.ignore(ast.clazz(["!", "="]), "!", "="),
                ast.ignore(["(", "?"], "!", "="),
                ast.ignore(["(", "?", "<"], "!", "="),
                ast.ignore(None, "!", ["=", "="]),
            ],
        ),
        ast.subst_list_liga(
            "!==",
            banner=[
                ast.ignore(ast.clazz(["!", "="]), "!", ["=", "="]),
                ast.ignore(["(", "?"], "!", ["=", "="]),
                ast.ignore(["(", "?", "<"], "!", ["=", "="]),
                ast.ignore(None, "!", ["=", "="]),
            ],
        ),
        ast.subst_list_liga(
            "=/=",
            banner=[
                ast.ignore("=", "=", ["/", "="]),
                ast.ignore(["(", "?"], "=", ["/", "="]),
                ast.ignore(["(", "?", "<"], "=", ["/", "="]),
                ast.ignore(None, "=", ["/", "=", "="]),
            ],
        ),
        ast.subst_list_liga(
            "=!=",
            banner=[
                ast.ignore("=", "=", ["!", "="]),
                ast.ignore(["(", "?"], "=", ["!", "="]),
                ast.ignore(["(", "?", "<"], "=", ["!", "="]),
                ast.ignore(None, "=", ["!", "=", "="]),
            ],
        ),
        ast.subst_list_liga(
            "=<=",
            banner=[
                ast.ignore(ast.clazz(["=", ">", "<", "|"]), "=", [">", "="]),
                ast.ignore(["(", "?"], "=", [">", "="]),
                ast.ignore(None, "=", [">", "=", ast.clazz(["=", "<", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "=>=",
            banner=[
                ast.ignore(ast.clazz(["=", ">", "<", "|"]), "=", ["<", "="]),
                ast.ignore(["(", "?"], "=", ["<", "="]),
                ast.ignore(None, "=", ["<", "=", ast.clazz(["=", "<", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            "|=",
            banner=[
                ast.ignore("|", "|", "="),
                ast.ignore(None, "|", ["=", ast.clazz([">", "="])]),
            ],
        ),
        ast.subst_list_liga(
            "||=",
            banner=[
                ast.ignore("|", "|", ["|", "="]),
                ast.ignore(None, "|", ["|", "|", "="]),
            ],
        ),
    ]
