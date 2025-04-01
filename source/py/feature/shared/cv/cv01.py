import source.py.feature.ast as ast


def cv01_subst():
    return ast.subst_list_map(
        [
            "Q",
            "&",
            "&&",
            "&&&",
            "@",
            "~@",
            "$",
            "%",
            "=>",
            "<==",
            "==>",
            "<=>",
            "<==>",
            "<=<",
            ">=>",
            "<=|",
            "|=>",
            "<-|",
            "|->",
            "<-",
            "->",
            "<--",
            "-->",
            "<-<",
            ">->",
            "<->",
            "<!--",
            "<#--",
            "xml_empty_comment.liga", # <!---->
        ],
        target_suffix=".cv01",
    )

cv01_name = "Normalize Special Symbols"
cv01_feat_regular = ast.cv(1, cv01_name, cv01_subst())
cv01_feat_italic = ast.cv(1, cv01_name, cv01_subst())