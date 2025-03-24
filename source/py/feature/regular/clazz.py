import source.py.feature.utils as fea
from source.py.feature.shared.clazz import (
    total_list
)


cls_a = fea.def_clazz("A", ["A", "a", "a.cv02"])
cls_b = fea.def_clazz("B", ["B", "b"])
cls_c = fea.def_clazz("C", ["C", "c"])
cls_d = fea.def_clazz("D", ["D", "d"])
cls_e = fea.def_clazz("E", ["E", "e"])
cls_f = fea.def_clazz("F", ["F", "f"])
cls_g = fea.def_clazz("G", ["G", "g"])
cls_h = fea.def_clazz("H", ["H", "h"])
cls_i = fea.def_clazz("I", ["I", "i", "i.cv03"])
cls_j = fea.def_clazz("J", ["J", "j"])
cls_k = fea.def_clazz("K", ["K", "k"])
cls_l = fea.def_clazz("L", ["L", "l", "l.cv04"])
cls_m = fea.def_clazz("M", ["M", "m"])
cls_n = fea.def_clazz("N", ["N", "n"])
cls_o = fea.def_clazz("O", ["O", "o"])
cls_p = fea.def_clazz("P", ["P", "p"])
cls_q = fea.def_clazz("Q", ["Q", "q", "Q.cv01"])
cls_r = fea.def_clazz("R", ["R", "r"])
cls_s = fea.def_clazz("S", ["S", "s"])
cls_t = fea.def_clazz("T", ["T", "t"])
cls_u = fea.def_clazz("U", ["U", "u"])
cls_v = fea.def_clazz("V", ["V", "v"])
cls_w = fea.def_clazz("W", ["W", "w"])
cls_x = fea.def_clazz("X", ["X", "x"])
cls_y = fea.def_clazz("Y", ["Y", "y"])
cls_z = fea.def_clazz("Z", ["Z", "z"])
hex_letter = fea.def_clazz("HexLetter", [], [cls_a, cls_b, cls_c, cls_d, cls_e, cls_f])

list = [
    *total_list,
    cls_a,
    cls_b,
    cls_c,
    cls_d,
    cls_e,
    cls_f,
    cls_g,
    cls_h,
    cls_i,
    cls_j,
    cls_k,
    cls_l,
    cls_m,
    cls_n,
    cls_o,
    cls_p,
    cls_q,
    cls_r,
    cls_s,
    cls_t,
    cls_u,
    cls_v,
    cls_w,
    cls_x,
    cls_y,
    cls_z,
    hex_letter,
]
