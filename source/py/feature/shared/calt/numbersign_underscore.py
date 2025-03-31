from source.py.feature import ast


def get_lookup():
    start = "numbersign_start.liga"
    mid = "numbersign_middle.liga"
    end = "numbersign_end.liga"

    return [
        ast.subst_list_liga(
            "__",
            ignores=[
                ast.ignore(ast.clazz(["_", "#"]), "_", "_"),
                ast.ignore(None, "_", ["_", "_"]),
            ],
        ),
        ast.subst_list_liga(
            "#{",
            ignores=[
                ast.ignore("#", "#", "{"),
                ast.ignore(None, "#", ["{", "{"]),
            ],
        ),
        ast.subst_list_liga(
            "#[",
            ignores=[
                ast.ignore("#", "#", "["),
                ast.ignore(None, "#", ["[", "["]),
            ],
        ),
        ast.subst_list_liga(
            "#(",
            ignores=[
                ast.ignore("#", "#", "("),
                ast.ignore(None, "#", ["(", "("]),
            ],
        ),
        ast.subst_list_liga(
            "#?",
            ignores=[
                ast.ignore("#", "#", "?"),
                ast.ignore(None, "#", ["?", "?"]),
            ],
        ),
        ast.subst_list_liga(
            "#!",
            ignores=[
                ast.ignore("#", "#", "!"),
                ast.ignore(None, "#", ["!", "!"]),
            ],
        ),
        ast.subst_list_liga(
            "#:",
            ignores=[
                ast.ignore("#", "#", ":"),
                ast.ignore(None, "#", [":", ":"]),
            ],
        ),
        ast.subst_list_liga(
            "#=",
            ignores=[
                ast.ignore("#", "#", "="),
                ast.ignore(None, "#", ["=", "="]),
            ],
        ),
        ast.subst_list_liga(
            "#_",
            ignores=[
                ast.ignore("#", "#", "_"),
                ast.ignore(None, "#", ["_", "_"]),
            ],
        ),
        ast.subst_list_liga(
            "#__",
            ignores=[
                ast.ignore("#", "#", ["_", "_"]),
                ast.ignore(None, "#", ["_", "_", "_"]),
            ],
        ),
        ast.subst_list_liga(
            "#_(",
            ignores=[
                ast.ignore("#", "#", ["_", "("]),
                ast.ignore(None, "#", ["_", "(", "("]),
            ],
        ),
        ast.lookup(
            ast.gly("##__"),
            None,
            [
                ast.ignore("#", "#", [ast.SPC, ast.SPC, ast.gly("#__")]),
                ast.subst(None, "#", [ast.SPC, ast.SPC, ast.gly("#__")], start),
            ],
        ),
        ast.subst_list_liga(
            "]#",
            ignores=[
                ast.ignore("]", "]", "#"),
                ast.ignore(None, "]", ["#", "#"]),
            ],
        ),
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
