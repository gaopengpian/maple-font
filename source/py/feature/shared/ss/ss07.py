from source.py.feature import ast


ss07_subst = [
    ast.subst_list_liga(
        ">>",
        ignores=[
            ast.ignore(None, ">", ">"),
            ast.ignore(ast.clazz([">", "/", "<"]), ">", ">"),
        ],
    ),
    ast.subst_list_liga(
        ">>>",
        ignores=[
            ast.ignore(None, ">", [">", ">", ">"]),
            ast.ignore(">", ">", [">", ">"]),
        ],
    ),
]

ss07_name = "Break connected strokes between italic letters"
ss07 = ast.ss(7, ss07_name, ss07_subst)
