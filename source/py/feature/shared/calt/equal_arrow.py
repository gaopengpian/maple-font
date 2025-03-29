from source.py.feature import ast

# todo))
def get_equal_lookup():
    return [
        ast.subst_list_liga("<=>"),
        ast.subst_list_liga("<==>"),
        ast.subst_list_liga(">="),
        ast.subst_list_liga("<="),
        ast.subst_list_liga("<=="),
        ast.subst_list_liga("==>"),
        ast.subst_list_liga("=>"),
        ast.subst_list_liga("<=<"),
        ast.subst_list_liga(">=>"),
        ast.subst_list_liga("<=|"),
        ast.subst_list_liga("|=>"),
    ]