import source.py.feature.part.utils as fea
import source.py.feature.part.lang as lang
import source.py.feature.part.clazz as clazz
import source.py.feature.part.feature as feat


def generate_feature_file():
    return fea.create(
        class_list=clazz.list,
        lang_list=lang.list,
        feature_list=feat.list,
    )
