from source.py.feature import ast


def get_lookup():
    return [
        ast.subst_list_liga(
            "[|",
            ignores=[
                ast.ignore("[", "[", "|"),
                ast.ignore(None, "[", ["|", "]"]),
            ],
        ),
        ast.subst_list_liga(
            "|]",
            ignores=[
                ast.ignore("[", "|", "]"),
                ast.ignore(None, "|", ["]", "]"]),
            ],
        ),
        ast.subst_list_liga(
            "!!",
            ignores=[
                ast.ignore("!", "!", "!"),
                ast.ignore(None, "!", ["!", "!"]),
                ast.ignore(["(", "?"], "!", "!"),
                ast.ignore(["(", "?", "<"], "!", "!"),
            ],
        ),
        ast.subst_list_liga(
            "||",
            ignores=[
                ast.ignore(ast.clazz(["|", "["]), "|", "|"),
                ast.ignore(None, "|", ["|", ast.clazz(["|", "]"])]),
            ],
        ),
        ast.subst_list_liga(
            "??",
            ignores=[
                ast.ignore("?", "?", "?"),
                ast.ignore(None, "?", ["?", "?"]),
            ],
        ),
        ast.subst_list_liga(
            "???",
            ignores=[
                ast.ignore("?", "?", ["?", "?"]),
                ast.ignore(None, "?", ["?", "?", "?"]),
            ],
        ),
        ast.subst_list_liga(
            "&&",
            ignores=[
                ast.ignore("&", "&", "&"),
                ast.ignore(None, "&", ["&", "&"]),
            ],
        ),
        ast.subst_list_liga(
            "&&&",
            ignores=[
                ast.ignore("&", "&", ["&", "&"]),
                ast.ignore(None, "&", ["&", "&", "&"]),
            ],
        ),
        ast.subst_list_liga(
            "//",
            ignores=[
                ast.ignore("/", "/", "/"),
                ast.ignore(None, "/", ["/", ast.clazz(["/", "="])]),
            ],
        ),
        ast.subst_list_liga(
            "///",
            ignores=[
                ast.ignore("/", "/", ["/", "/"]),
                ast.ignore(None, "/", ["/", "/", "/"]),
            ],
        ),
        ast.subst_list_liga(
            "/*",
            ignores=[
                ast.ignore(ast.clazz(["/", "*"]), "/", "*"),
                ast.ignore(None, "/", ["*", ast.clazz(["/", "*", "."])]),
            ],
        ),
        ast.subst_list_liga(
            "/**",
            ignores=[
                ast.ignore(ast.clazz(["/", "*"]), "/", ["*", "*"]),
                ast.ignore(None, "/", ["*", "*", ast.clazz(["/", "*", "."])]),
            ],
        ),
        ast.subst_list_liga(
            "*/",
            ignores=[
                ast.ignore(ast.clazz(["/", "*", "."]), "*", "/"),
                ast.ignore(None, "*", ["/", ast.clazz(["/", "*"])]),
            ],
        ),
        ast.subst_list_liga(
            "++",
            ignores=[
                ast.ignore(ast.clazz(["+", ":"]), "+", "+"),
                ast.ignore(None, "+", ["+", ast.clazz(["+", ":"])]),
            ],
        ),
        ast.subst_list_liga(
            "+++",
            ignores=[
                ast.ignore("+", "+", ["+", "+"]),
                ast.ignore(None, "+", ["+", "+", "+"]),
            ],
        ),
        ast.subst_list_liga(
            "--",
            ignores=[
                ast.ignore("<", "-", ["-", ">"]),
                ast.ignore(
                    ["(", "?", "<", "!"],
                    "-",
                    "-",
                ),
                ast.ignore(
                    ast.clazz(["<", "-"]),
                    "-",
                    "-",
                ),
                ast.ignore(None, "-", ["-", "-"]),
            ],
        ),
        ast.subst_list_liga(
            "---",
            ignores=[
                ast.ignore("<", "-", ["-", "-", ">"]),
                ast.ignore("-", "-", ["-", "-"]),
                ast.ignore(None, "-", ["-", "-", "-"]),
            ],
        ),
        ast.subst_list_liga(
            ";;",
            ignores=[
                ast.ignore(";", ";", ";"),
                ast.ignore(None, ":", [":", ":"]),
            ],
        ),
        ast.subst_list_liga(
            ";;;",
            ignores=[
                ast.ignore(";", ";", [";", ";"]),
                ast.ignore(None, ";", [";", ";", ";"]),
            ],
        ),
        ast.subst_list_liga(
            "..",
            ignores=[
                ast.ignore(".", ".", "."),
                ast.ignore(None, ".", [".", ast.clazz([".", "<", "?"])]),
            ],
        ),
        ast.subst_list_liga(
            "...",
            ignores=[
                ast.ignore(".", ".", [".", "."]),
                ast.ignore(None, ".", [".", ".", ast.clazz([".", "<", "?"])]),
            ],
        ),
        ast.subst_list_liga(
            ".?",  # Zig
            ignores=[
                ast.ignore(".", ".", "?"),
                ast.ignore(None, ".", ["?", "?"]),
            ],
        ),
        ast.subst_list_liga(
            "?:",
            ignores=[
                ast.ignore("?", "?", ":"),
                ast.ignore(None, "?", [":", ast.clazz([".", "="])]),
            ],
        ),
        ast.subst_list_liga(
            "?.",  # TypeScript / Rust
            ignores=[
                ast.ignore("?", "?", "."),
                ast.ignore(None, "?", [".", "."]),
            ],
        ),
        ast.subst_list_liga(
            "..<",  # Swift
            ignores=[
                ast.ignore(".", ".", [".", "<"]),
                ast.ignore(None, ".", [".", "<", ast.clazz(["<", "/", ">"])]),
            ],
        ),
        ast.subst_list_liga(
            ".=",  # Swift
            ignores=[
                ast.ignore(".", ".", "="),
                ast.ignore(None, ".", ["=", "="]),
            ],
        ),
    ]
