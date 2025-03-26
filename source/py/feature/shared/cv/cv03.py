import source.py.feature.ast as ast

cv03_subst = ast.subst_list_map(
    [
        "i",
        "iacute",
        "ibreve",
        "icaron",
        "icircumflex",
        "idieresis",
        "idotaccent",
        "idotbelow",
        "idotless",
        "igrave",
        "ihookabove",
        "imacron",
        "iogonek",
        "itilde",
    ],
    target_suffix=".cv03",
)

cv03_name = "Alternative i"
cv03_regular = ast.cv(3, cv03_name, cv03_subst)
