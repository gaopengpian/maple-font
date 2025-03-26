import source.py.feature.ast as ast

def cv37_subst():
    return ast.subst_list_map(
        [
            "y",
            "yacute",
            "ycircumflex",
            "ydieresis",
            "ydotbelow",
            "ygrave",
            "yhookabove",
            "ymacron",
            "ytilde",
        ],
        target_suffix=".cv37",
    )

cv37_italic = ast.cv(37, "Italic y with straight intersection", cv37_subst())