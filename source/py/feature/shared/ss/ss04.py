from source.py.feature import ast


ss04_subst = ast.subst_list_map(
    [
        ast.gly("__"),
        ast.gly("#__"),
    ],
    target_suffix=".ss04",
)

ss04_name = "Broken multiple underscores ligatures"
ss04 = ast.ss(4, ss04_name, ss04_subst)
