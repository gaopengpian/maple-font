import source.py.feature.ast as ast
import source.py.feature.shared.lang as lang
import source.py.feature.regular.clazz as clazz
import source.py.feature.regular.feature as feat


def generate_fea_string():
    return ast.create([*lang.list, *clazz.list, *feat.list])
