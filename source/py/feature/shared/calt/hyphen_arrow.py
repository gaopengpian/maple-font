from source.py.feature import ast
from source.py.feature.shared.clazz import digit


def get_lookup():
    return [
        ast.subst_list_liga(
            "<!--",
            banner=[
                ast.ignore("<", "<", ["!", "-", "-"]),
                ast.ignore(["(", "?"], "<", ["!", "-", "-"]),
                ast.ignore(None, "<", ["!", "-", "-", "-"]),
            ],
        ),
        ast.subst_list_liga(
            "<#--",
            banner=[
                ast.ignore("<", "<", ["#", "-", "-"]),
                ast.ignore(None, "<", ["#", "-", "-", "-"]),
            ],
        ),
        ast.subst_list_liga("<!---->", target="xml_empty_comment.liga"),
        ast.subst_list_liga(
            "<->",
            banner=[
                ast.ignore("<", "<", ["-", ">"]),
                ast.ignore(None, "<", ["-", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "->",
            banner=[
                ast.ignore(ast.clazz(["-", "<", ">", "|", "+"]), "-", ">"),
                ast.ignore(None, "-", [">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "<-",
            banner=[
                ast.ignore(
                    None, "<", ["-", ast.clazz(["-", "<", ">", "|", "+", "/", digit])]
                ),
                ast.ignore("<", "<", "-"),
            ],
        ),
        ast.subst_list_liga(
            "-->",
            banner=[
                ast.ignore("-", "-", ["-", ">"]),
                ast.ignore(None, "-", ["-", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "<--",
            banner=[
                ast.ignore("<", "<", ["-", "-"]),
                ast.ignore(None, "<", ["-", "-", "-"]),
            ],
        ),
        ast.subst_list_liga(
            "<-<",
            banner=[
                ast.ignore("<", "<", ["-", "<"]),
                ast.ignore(None, "<", ["-", "<", "<"]),
            ],
        ),
        ast.subst_list_liga(
            ">->",
            banner=[
                ast.ignore(">", ">", ["-", ">"]),
                ast.ignore(None, ">", ["-", ">", ">"]),
            ],
        ),
        ast.subst_list_liga(
            "<-|",
            banner=[
                ast.ignore("<", "<", ["-", "|"]),
                ast.ignore(None, "<", ["-", "|", "|"]),
            ],
        ),
        ast.subst_list_liga(
            "|->",
            banner=[
                ast.ignore("|", "|", ["-", ">"]),
                ast.ignore(None, "|", ["-", ">", ">"]),
            ],
        ),
    ]
