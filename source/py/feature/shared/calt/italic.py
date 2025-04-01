from source.py.feature import ast


def get_lookup():
    return [
        ast.subst_list_liga("Cl", header=[ast.ignore(None, "C", ["l", "l"])]),
        ast.subst_list_liga("al", header=[ast.ignore(None, "a", ["l", "l"])]),
        ast.subst_list_liga("cl", header=[ast.ignore(None, "c", ["l", "l"])]),
        ast.subst_list_liga("el", header=[ast.ignore(None, "e", ["l", "l"])]),
        ast.subst_list_liga("il", header=[ast.ignore(None, "i", ["l", "l"])]),
        ast.subst_list_liga("tl", header=[ast.ignore(None, "l", ["l", "l"])]),
        ast.subst_list_liga("ul", header=[ast.ignore(None, "u", ["l", "l"])]),
        ast.subst_list_liga("xl", header=[ast.ignore(None, "x", ["l", "l"])]),
        ast.subst_list_liga("ff", header=[ast.ignore(None, "f", ["f", "f"])]),
        ast.subst_list_liga("tt", header=[ast.ignore(None, "t", ["t", "t"])]),
        ast.subst_list_liga("all", header=[ast.ignore(None, "a", ["l", "l", "l"])]),
        ast.subst_list_liga("ell", header=[ast.ignore(None, "e", ["l", "l", "l"])]),
        ast.subst_list_liga("ill", header=[ast.ignore(None, "i", ["l", "l", "l"])]),
        ast.subst_list_liga("ull", header=[ast.ignore(None, "u", ["l", "l", "l"])]),
        ast.subst_list_liga(
            "ll",
            header=[
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
