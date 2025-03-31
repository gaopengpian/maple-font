from source.py.feature import ast


def get_lookup():
    return [
        ast.subst_list_liga("<>",ignores=[
            ast.ignore('<', '<', '>'),
            ast.ignore(None, '<', ['>', '>']),
        ]),
        ast.subst_list_liga("</",ignores=[
            ast.ignore('<', '<', '/'),
            ast.ignore(None, '<', ['/', '/']),
        ]),
        ast.subst_list_liga("/>",ignores=[
            ast.ignore('/', '/', '>'),
            ast.ignore(None, '/', ['>', '>']),
        ]),
        ast.subst_list_liga("</>",ignores=[
            ast.ignore(['<', '<'], '/', '>'),
            ast.ignore(None, '<', ['/', '>', '>']),
        ]),
        ast.subst_list_liga("<+",ignores=[
            ast.ignore('<', '<', '+'),
            ast.ignore(None, '<', ['+', '+']),
        ]),
        ast.subst_list_liga("+>",ignores=[
            ast.ignore('+', '+', '>'),
            ast.ignore(None, '+', ['>', '>']),
        ]),
        ast.subst_list_liga("<+>",ignores=[
            ast.ignore(['<', '<'], '+', '>'),
            ast.ignore(None, '<', ['+', '>', '>']),
        ]),
        ast.subst_list_liga("<*",ignores=[
            ast.ignore('<', '<', '*'),
            ast.ignore(None, '<', ['*', '*']),
        ]),
        ast.subst_list_liga("*>",ignores=[
            ast.ignore('*', '*', '>'),
            ast.ignore(None, '*', ['>', '>']),
        ]),
        ast.subst_list_liga("<*>",ignores=[
            ast.ignore(['<', '<'], '*', '>'),
            ast.ignore(None, '<', ['*', '>', '>']),
        ]),
    ]