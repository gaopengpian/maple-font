import source.py.feature.ast as ast
import source.py.feature.shared.lang as lang
import source.py.feature.regular.clazz as regular_clazz
import source.py.feature.regular.feature as regular_feat
import source.py.feature.italic.clazz as italic_clazz
import source.py.feature.italic.feature as italic_feat


def generate_fea_string(italic: bool):
    cls = italic_clazz.class_list if italic else regular_clazz.class_list
    feat = italic_feat.feature_list if italic else regular_feat.feature_list
    return ast.create(cls, [*lang.lang_list, *feat])


def generate_fea_string_cn():
    return ast.create([], regular_feat.basic_features_cn)
