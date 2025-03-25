import source.py.feature.utils as fea

cv01_subst = fea.subst_list(
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
    ".cv01",
)

cv01 = fea.def_cv(1, "Normalize Special Symbols", cv01_subst)