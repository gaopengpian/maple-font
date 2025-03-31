import source.py.feature.ast as ast
import source.py.feature.shared.lang as lang
import source.py.feature.regular.clazz as regular_clazz
import source.py.feature.regular.feature as regular_feat
import source.py.feature.italic.clazz as italic_clazz
import source.py.feature.italic.feature as italic_feat


def generate_fea_string(italic: bool):
    if italic:
        return ast.create(
            italic_clazz.class_list, [*lang.lang_list, *italic_feat.feature_list]
        )
    return ast.create(
        regular_clazz.class_list, [*lang.lang_list, *regular_feat.feature_list]
    )
