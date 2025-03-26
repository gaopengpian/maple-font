import source.py.feature.ast as ast

def cv33_subst():
    return ast.subst_list_map(
        [
            "i",
            "iacute",
            "ibreve",
            "icaron",
            "icircumflex",
            "idieresis",
            "idotbelow",
            "idotless",
            "igrave",
            "ihookabove",
            "imacron",
            "iogonek",
            "itilde",
            "j",
            "jcircumflex",
            "jdotless",
            ast.gly("il"),
            ast.gly("ill"),
            ast.gly("il", ".cv04"),
            ast.gly("ill", ".cv04"),
        ],
        target_suffix=".cv33",
    )