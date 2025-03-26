import source.py.feature.ast as ast


def cv32_subst():
    return ast.subst_list_map(["f", ast.gly("f_f")], target_suffix=".cv32")


cv32_italic = ast.cv(32, "Italic f without bottom tail", cv32_subst())
