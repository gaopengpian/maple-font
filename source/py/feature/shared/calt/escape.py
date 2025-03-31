from source.py.feature import ast


def get_lookup():
    escape_cls = ast.Clazz("Escape", list(ast.total_punctuations))
    escape_liga = ast.gly("\\", ".liga")
    return [
        escape_cls.state(),
        ast.lookup(
            "escape",
            "Thin backslash (\\) to better distingish escape chars",
            [
                ast.ignore(escape_liga, "\\", escape_cls),
                ast.ignore(None, "\\", ["%", "%"]),
                ast.subst(None, "\\", escape_cls, escape_liga),
            ],
        )
    ]
