from source.py.feature import ast


ss01_subst = ast.subst_list_map(
    [
        "==",
        "===",
        "!=",
        "!==",
        "=/=",
    ],
    target_suffix=".ss01",
)

ss01_name = "Broken multiple equals ligatures"
ss01_feat = ast.ss(1, ss01_name, ss01_subst)
