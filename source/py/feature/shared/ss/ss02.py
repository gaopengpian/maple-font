from source.py.feature import ast


ss02_subst = ast.subst_list_map(
    [
        ast.gly("<="),
        ast.gly(">="),
    ],
    target_suffix=".ss02",
)

ss02_name = "Broken compare and equal ligatures"
ss02_feat = ast.ss(2, ss02_name, ss02_subst)
