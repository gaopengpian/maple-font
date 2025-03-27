from source.py.feature import ast


def liga_cls(text: str):
    arr = ["["] + [f"@{g.upper()}" for g in list(text)] + ["]"]
    return ast.subst_list_liga(
        arr, target=f"tag_{text}.liga", lookup_name=f"tag_{text}.liga.ss03"
    )


ss03_subst = [
    liga_cls("trace"),
    liga_cls("debug"),
    liga_cls("info"),
    liga_cls("warn"),
    liga_cls("error"),
    liga_cls("fatal"),
    liga_cls("todo"),
    liga_cls("fixme"),
]

ss03_name = "Enable arbitrary tag ligatures"
ss03 = ast.ss(3, ss03_name, ss03_subst)
