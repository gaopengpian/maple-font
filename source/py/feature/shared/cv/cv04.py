from source.py.feature import ast


cv04_base = [
    "l",
    "lacute",
    "lcaron",
    "lcommaaccent",
    "ldot",
    "lslash",
    "one",
    "one.dnom",
    "one.numr",
    "oneinferior",
    "onesuperior",
]

cv04_subst = ast.subst_list_map(
    cv04_base,
    target_suffix=".cv04",
)

cv04_subst_i = ast.subst_list_map(
    [
        *cv04_base,
        ast.gly("C l"),
        ast.gly("a l"),
        ast.gly("c l"),
        ast.gly("e l"),
        ast.gly("i l"),
        ast.gly("l l"),
        ast.gly("t l"),
        ast.gly("u l"),
        ast.gly("x l"),
        ast.gly("a l l"),
        ast.gly("e l l"),
        ast.gly("i l l"),
        ast.gly("u l l"),
    ],
    target_suffix=".cv04",
)

cv04_name = "Alternative l"
cv04_feat_regular = ast.cv(4, cv04_name, cv04_subst)
cv04_feat_italic = ast.cv(4, cv04_name, cv04_subst_i)
