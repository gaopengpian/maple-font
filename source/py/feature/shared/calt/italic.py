from source.py.feature import ast


def get_lookup():
    return [
        ast.subst_list_liga("Cl", ignores=[ast.ignore(None, "C", ["l", "l"])]),
        ast.subst_list_liga("al", ignores=[ast.ignore(None, "a", ["l", "l"])]),
        ast.subst_list_liga("cl", ignores=[ast.ignore(None, "c", ["l", "l"])]),
        ast.subst_list_liga("el", ignores=[ast.ignore(None, "e", ["l", "l"])]),
        ast.subst_list_liga("il", ignores=[ast.ignore(None, "i", ["l", "l"])]),
        ast.subst_list_liga("tl", ignores=[ast.ignore(None, "l", ["l", "l"])]),
        ast.subst_list_liga("ul", ignores=[ast.ignore(None, "u", ["l", "l"])]),
        ast.subst_list_liga("xl", ignores=[ast.ignore(None, "x", ["l", "l"])]),
        ast.subst_list_liga("ff", ignores=[ast.ignore(None, "f", ["f", "f"])]),
        ast.subst_list_liga("tt", ignores=[ast.ignore(None, "t", ["t", "t"])]),
        ast.subst_list_liga("all", ignores=[ast.ignore(None, "a", ["l", "l", "l"])]),
        ast.subst_list_liga("ell", ignores=[ast.ignore(None, "e", ["l", "l", "l"])]),
        ast.subst_list_liga("ill", ignores=[ast.ignore(None, "i", ["l", "l", "l"])]),
        ast.subst_list_liga("ull", ignores=[ast.ignore(None, "u", ["l", "l", "l"])]),
        ast.subst_list_liga(
            "ll",
            ignores=[
                ast.ignore(None, "l", ["l", "l"]),
                ast.ignore(
                    ast.clazz(
                        [
                            "C",
                            "a",
                            "c",
                            "e",
                            "i",
                            "t",
                            "u",
                            "x",
                        ]
                    ),
                    "l",
                    "l",
                ),
            ],
        ),
    ]
