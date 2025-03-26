import source.py.feature.ast as ast

cv01_subst = ast.subst_list_map(
    [
        "Q",
        ast.gly("&"),
        ast.gly("&&"),
        ast.gly("&&&"),
        ast.gly("@"),
        ast.gly("~@"),
        ast.gly("$"),
        ast.gly("%"),
        ast.gly("=>"),
        ast.gly("<=="),
        ast.gly("==>"),
        ast.gly("<=>"),
        ast.gly("<==>"),
        ast.gly("<=<"),
        ast.gly(">=>"),
        ast.gly("<=|"),
        ast.gly("|=>"),
        ast.gly("<-|"),
        ast.gly("|->"),
        ast.gly("<-"),
        ast.gly("->"),
        ast.gly("<--"),
        ast.gly("-->"),
        ast.gly("<-<"),
        ast.gly(">->"),
        ast.gly("<->"),
        ast.gly("<!--"),
        ast.gly("<#--"),
        "xml_empty_comment.liga", # <!---->
    ],
    target_suffix=".cv01",
)

cv01_name = "Normalize Special Symbols"
cv01_regular = ast.cv(1, cv01_name, cv01_subst)