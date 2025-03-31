from source.py.feature import ast


def get_lookup():
    esc = ast.Clazz("Escape", list(ast.total_punctuations))
    esc_liga = ast.gly("\\", ".liga")
    return [
        ast.lookup(
            "escape",
            "Thin backslash (\\) to better distingish escape chars",
            [
                ast.ignore(esc_liga, "\\", esc),
                ast.ignore(None, "\\", ["%", "%"]),
                ast.subst(None, "\\", esc, esc_liga),
            ],
        )
    ]
