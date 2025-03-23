import source.py.feature.part.utils as fea

zero = fea.def_clazz("zero", ["zero", "zero.zero"])
digit = fea.def_clazz("Digit", ["one", "two", "three"], [zero])

list = [zero, digit]
