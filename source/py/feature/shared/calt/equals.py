from source.py.feature import ast

# todo))
def get_equals_lookup():
    return [
        ast.subst_list_liga("=="),
        ast.subst_list_liga("==="),
        ast.subst_list_liga("!="),
        ast.subst_list_liga("!=="),
        ast.subst_list_liga("=/="),
        ast.subst_list_liga("=!="),
        ast.subst_list_liga("=<="),
        ast.subst_list_liga("=>="),
        ast.subst_list_liga("|="),
        ast.subst_list_liga("||="),
    ]