import source.py.feature.ast as ast


def cv31_subst():
    return ast.subst_list_map(
        [
            "a",
            "aacute",
            "abreve",
            "abreveacute",
            "abrevedotbelow",
            "abrevegrave",
            "abrevehookabove",
            "abrevetilde",
            "acaron",
            "acircumflex",
            "acircumflexacute",
            "acircumflexdotbelow",
            "acircumflexgrave",
            "acircumflexhookabove",
            "acircumflextilde",
            "adieresis",
            "adotbelow",
            "agrave",
            "ahookabove",
            "amacron",
            "aogonek",
            "aring",
            "atilde",
            "a-cy",
            "ordfeminine",
            # Ligature variants
            ast.gly("al"),
            ast.gly("all"),
            ast.gly("al", ".cv04"),
            ast.gly("all", ".cv04"),
        ],
        target_suffix=".cv31",
    )

cv31_italic = ast.cv(31, "Italic a with top arm", cv31_subst())