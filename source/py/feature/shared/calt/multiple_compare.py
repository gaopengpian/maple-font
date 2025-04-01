from source.py.feature import ast
from source.py.feature.shared.clazz import digit


def get_lookup(letter_list: list[ast.Clazz]):
    var = ast.Clazz("Var", ["_", ast.gly("__")], [*letter_list, digit])
    space = ast.Clazz("Space", ["space", "nbspace"])
    leading_symbol_liga = ast.Clazz(
        "LeadingSymbolLiga", [ast.gly("++"), ast.gly("--"), ast.gly("__")]
    )
    symbol_before_greater = ast.Clazz(
        "SymbolBeforeGreater", ["|", "!", "~", "~", "#", "%"]
    )
    number = ast.Clazz("Number", ["+", "-"], [digit])
    eh = ast.Clazz("EH", ["=", "-"])

    surround = [
        [var, [space, ast.SPC, leading_symbol_liga]],
        [var, [ast.SPC, leading_symbol_liga]],
        [var, ast.clazz([var, number])],
        [ast.clazz([space, eh, symbol_before_greater]), None],
        [None, [space, number]],
        [None, ast.clazz(["/", number, eh])],
        ["`", "`"],
    ]

    return [
        ast.subst_list_liga(
            "<<",
            banner=[
                ast.ignore("<", "<", "<"),
                ast.ignore(None, "<", ["<", ast.clazz(["<", "~"])]),
            ],
        ),
        ast.subst_list_liga(
            "<<<",
            banner=[
                ast.ignore("<", "<", ["<", "<"]),
                ast.ignore(None, "<", ["<", "<", "<"]),
            ],
        ),
        var.state(),
        space.state(),
        leading_symbol_liga.state(),
        symbol_before_greater.state(),
        number.state(),
        eh.state(),
        ast.subst_list_liga(
            ">>",
            banner=[
                ast.ignore(None, ">", [">", ">"]),
                ast.ignore(ast.clazz(["<", "/", ">"]), ">", [">"]),
            ],
            surround=surround,
        ),
        ast.subst_list_liga(
            ">>>",
            banner=[
                ast.ignore(">", ">", [">", ">"]),
            ],
            surround=surround,
        ),
    ]
