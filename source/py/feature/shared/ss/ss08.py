from source.py.feature import ast


ss08_subst = [
    #
    ast.subst_list_liga(
        "<<-",
        target=ast.gly("<<-", ".ss08", True),
        ignores=[
            ast.ignore("<", "<", ["<", "-"]),
            ast.ignore(None, "<", ["<", "-", "-"]),
        ],
    ),
    ast.subst("SPC", ast.gly("<<"), "-", "SPC"),
    #
    ast.subst_list_liga(
        "<<=",
        target=ast.gly("<<=", ".ss08", True),
        ignores=[
            ast.ignore("<", "<", ["<", "="]),
            ast.ignore(None, "<", ["<", "=", "="]),
        ],
    ),
    ast.subst("SPC", ast.gly("<<"), "=", "SPC"),
    #
    ast.subst_list_liga(
        ">>-",
        target=ast.gly(">>-", ".ss08", True),
        ignores=[
            ast.ignore(">", ">", [">", "-"]),
            ast.ignore(None, ">", [">", "-", "-"]),
        ],
    ),
    ast.subst("SPC", ast.gly(">>"), "-", "SPC"),
    #
    ast.subst_list_liga(
        ">>=",
        target=ast.gly(">>=", ".ss08", True),
        ignores=[
            ast.ignore(">", ">", [">", "="]),
            ast.ignore(None, ">", [">", "=", "="]),
        ],
    ),
    ast.subst("SPC", ast.gly(">>"), "=", "SPC"),
    #
    ast.subst_list_liga(
        "->>",
        target=ast.gly("->>", ".ss08", True),
        ignores=[
            ast.ignore("-", "-", [">", ">"]),
            ast.ignore(None, "-", ["-", ">", ">"]),
        ],
    ),
    ast.subst(None, "-", ["SPC", ast.gly(">>")], "SPC"),
    ast.subst(None, "SPC", ["SPC", ast.gly(">>")], "SPC"),
    #
    ast.subst_list_liga(
        "=>>",
        target=ast.gly("=>>", ".ss08", True),
        ignores=[
            ast.ignore("=", "=", [">", ">"]),
            ast.ignore(None, "=", ["-", ">", ">"]),
        ],
    ),
    ast.subst(None, "=", ["SPC", ast.gly(">>")], "SPC"),
    ast.subst(None, "SPC", ["SPC", ast.gly(">>")], "SPC"),
    #
    ast.subst_list_liga(
        "-<<",
        target=ast.gly("-<<", ".ss08", True),
        ignores=[
            ast.ignore("-", "-", ["<", "<"]),
            ast.ignore(None, "-", ["-", "<", "<"]),
        ],
    ),
    ast.subst(None, "-", ["SPC", ast.gly("<<")], "SPC"),
    ast.subst(None, "SPC", ["SPC", ast.gly("<<")], "SPC"),
    #
    ast.subst_list_liga(
        "=<<",
        target=ast.gly("=<<", ".ss08", True),
        ignores=[
            ast.ignore("=", "=", ["<", "<"]),
            ast.ignore(None, "=", ["=", "<", "<"]),
        ],
    ),
    ast.subst(None, "=", ["SPC", ast.gly("<<")], "SPC"),
    ast.subst(None, "SPC", ["SPC", ast.gly("<<")], "SPC"),
    #
    ast.subst_list_liga(
        ">-",
        target=ast.gly(">-", ".ss08", True),
        ignores=[
            ast.ignore(">", ">", "-"),
            ast.ignore(None, ">", ["-", ast.clazz(["-", ">", "<"])]),
        ],
    ),
    ast.subst_list_liga(
        "-<",
        target=ast.gly("-<", ".ss08", True),
        ignores=[
            ast.ignore(ast.clazz([">", "<", "-"]), "-", "<"),
            ast.ignore(None, "<", ["-", ast.clazz(["<", "/", "?"])]),
        ],
    ),
]

ss08_name = "Double headed arrows and reverse arrows ligatures"
ss08 = ast.ss(8, ss08_name, ss08_subst)
