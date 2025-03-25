import source.py.feature.ast as ast

cv01_subst = ast.subst_list_map(
    [
        "Q",
        "&",
        "& &",
        "& & &",
        "@",
        "~ @",
        "$",
        "%",
        "= >",
        "< = =",
        "= = >",
        "< = >",
        "< = = >",
        "< = <",
        "> = >",
        "< = |",
        "| = >",
        "< - |",
        "| - >",
        "< -",
        "- >",
        "< - -",
        "- - >",
        "< - <",
        "> - >",
        "< - >",
        "< ! - -",
        "< # - -",
        "xml_empty_comment.liga",  # <!---->
    ],
    target_suffix=".cv01",
)

cv01 = ast.cv(1, "Normalize Special Symbols", cv01_subst)