import source.py.feature.ast as ast

_number_list = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
clazz_number = ast.clazz(_number_list)
clazz_numr = ast.clazz([f"{n}.numr" for n in _number_list])
clazz_dnom = ast.clazz([f"{n}.dnom" for n in _number_list])

zero = ast.subst_list_map(
    ["zero", "zero.dnom", "zero.numr", "zeroinferior", "zerosuperior"], ".zero"
)

sinf = ast.subst_list_map(_number_list, target_suffix="inferior")
# subs is same as sinf, use another instance to correct indent
subs = ast.subst_list_map(_number_list, target_suffix="inferior")
sups = ast.subst_list_map(_number_list, target_suffix="superior")
numr = ast.subst_list_map(_number_list, target_suffix=".numr")
dnom = ast.subst_list_map(_number_list, target_suffix=".dnom")
ordn = [
    ast.subst(clazz_number, ast.clazz(["A", "a"]), None, "ordfeminine"),
    ast.subst(clazz_number, ast.clazz(["O", "o"]), None, "ordmasculine"),
]
frac = [
    *ast.lookup("FRAC", "",[ast.subst(None, "/", None, "fraction")]),
    *ast.lookup(
        "UP",
        None,
        [ast.subst(None, clazz_number, None, clazz_numr)],
    ),
    *ast.lookup(
        "DOWN",
        None,
        [
            ast.subst(
                "fraction", clazz_number, None, clazz_numr
            ),
            ast.subst(
                clazz_dnom,
                clazz_numr,
                None,
                clazz_dnom,
            ),
        ],
    ),
]

number_features = [
    *ast.feature("zero", zero),
    *ast.feature("sinf", sinf),
    *ast.feature("subs", subs),
    *ast.feature("sups", sups),
    *ast.feature("numr", numr),
    *ast.feature("dnom", dnom),
    *ast.feature("frac", frac),
    *ast.feature("ordn", ordn),
]
