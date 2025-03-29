from source.py.feature import ast


def upper_tag(text: str):
    return ast.subst_list_liga(
        ["["] + [g.upper() for g in list(text)] + ["]"],
        target=f"badge_{text}.liga",
        lookup_name=f"badge_{text}",
    )


def any_tag(text: str):
    return ast.subst_list_liga(
        [f"@{g.upper()}" for g in list(text)] + [")", ")"],
        target=f"badge_{text}.liga",
        lookup_name=f"badge_{text}_alt",
    )


def get_tag_lookup():
    return [
        upper_tag("trace"),
        upper_tag("debug"),
        upper_tag("info"),
        upper_tag("warn"),
        upper_tag("error"),
        upper_tag("fatal"),
        upper_tag("todo"),
        upper_tag("fixme"),
        any_tag("todo"),
        any_tag("fixme"),
    ]
