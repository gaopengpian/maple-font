from source.py.feature import ast

# todo))
def get_lines_lookup():
    return [
        ast.subst_list_liga("<|||"),
        ast.subst_list_liga("<||"),
        ast.subst_list_liga("<|"),
        ast.subst_list_liga("-|"),
        ast.subst_list_liga("<|>"),
        ast.subst_list_liga("_|_"),
        ast.subst_list_liga("|||>"),
        ast.subst_list_liga("||>"),
        ast.subst_list_liga("|>"),
        ast.subst_list_liga("||-"),
        ast.subst_list_liga("|-"),
    ]