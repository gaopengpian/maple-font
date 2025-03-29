from source.py.feature import ast


# todo))
def get_numbersign_lookup():
    start = "numbersign_start.liga"
    mid = "numbersign_middle.liga"
    end = "numbersign_end.liga"

    return [
        ast.subst_list_liga("__"),
        ast.subst_list_liga("#{"),
        ast.subst_list_liga("#["),
        ast.subst_list_liga("#("),
        ast.subst_list_liga("#?"),
        ast.subst_list_liga("#!"),
        ast.subst_list_liga("#:"),
        ast.subst_list_liga("#="),
        ast.subst_list_liga("#_"),
        ast.subst_list_liga("#__"),
        ast.subst_list_liga("#_("),
        ast.subst_list_liga("##__"),
        ast.subst_list_liga("]#"),
        ast.lookup(
            "numbersigns",
            "Infinity #",
            [
                ast.subst(ast.clazz([start, mid]), "#", "#", mid),
                ast.subst(ast.clazz([start, mid]), "#", None, end),
                ast.subst(None, "#", "#", start),
            ],
        ),
    ]
