from source.py.feature import ast


# todo))
def get_asciitilde_lookup():
    return [
        ast.subst_list_liga("<~"),
        ast.subst_list_liga("~>"),
        ast.subst_list_liga("~~"),
        ast.subst_list_liga("<~>"),
        ast.subst_list_liga("<~~"),
        ast.subst_list_liga("~~>"),
        ast.subst_list_liga("-~"),
        ast.subst_list_liga("~-"),
        ast.subst_list_liga("~@"),
    ]
