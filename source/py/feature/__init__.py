import source.py.feature.utils as fea
import source.py.feature.shared.lang as lang
import source.py.feature.regular.clazz as clazz
import source.py.feature.regular.feature as feat


def generate_feature_file():
    return fea.create(
        class_list=clazz.list,
        lang_list=lang.list,
        feature_list=feat.list,
    )
