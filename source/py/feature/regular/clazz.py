import source.py.feature.ast as ast
from source.py.feature.shared.clazz import list


cls_a = ast.Clazz("A", ["A", "a", "a.cv02"])
cls_b = ast.Clazz("B", ["B", "b"])
cls_c = ast.Clazz("C", ["C", "c"])
cls_d = ast.Clazz("D", ["D", "d"])
cls_e = ast.Clazz("E", ["E", "e"])
cls_f = ast.Clazz("F", ["F", "f"])
cls_g = ast.Clazz("G", ["G", "g"])
cls_h = ast.Clazz("H", ["H", "h"])
cls_i = ast.Clazz("I", ["I", "i", "i.cv03"])
cls_j = ast.Clazz("J", ["J", "j"])
cls_k = ast.Clazz("K", ["K", "k"])
cls_l = ast.Clazz("L", ["L", "l", "l.cv04"])
cls_m = ast.Clazz("M", ["M", "m"])
cls_n = ast.Clazz("N", ["N", "n"])
cls_o = ast.Clazz("O", ["O", "o"])
cls_p = ast.Clazz("P", ["P", "p"])
cls_q = ast.Clazz("Q", ["Q", "q", "Q.cv01"])
cls_r = ast.Clazz("R", ["R", "r"])
cls_s = ast.Clazz("S", ["S", "s"])
cls_t = ast.Clazz("T", ["T", "t"])
cls_u = ast.Clazz("U", ["U", "u"])
cls_v = ast.Clazz("V", ["V", "v"])
cls_w = ast.Clazz("W", ["W", "w"])
cls_x = ast.Clazz("X", ["X", "x"])
cls_y = ast.Clazz("Y", ["Y", "y"])
cls_z = ast.Clazz("Z", ["Z", "z"])
hex_letter = ast.Clazz("HexLetter", [], [cls_a, cls_b, cls_c, cls_d, cls_e, cls_f])

list = [c.state() for c in[
    *list,
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
]]
