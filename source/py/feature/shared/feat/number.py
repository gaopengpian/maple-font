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

_number_list_numr = [f"{n}.numr" for n in _number_list]
_number_list_dnom = [f"{n}.dnom" for n in _number_list]

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
    ast.subst(ast.clazz(_number_list), ast.clazz(["A", "a"]), None, "ordfeminine"),
    ast.subst(ast.clazz(_number_list), ast.clazz(["O", "o"]), None, "ordmasculine"),
]
frac = [
    *ast.lookup("FRAC", [ast.subst(None, "/", None, "fraction")]),
    *ast.lookup(
        "UP",
        [ast.subst(None, ast.clazz(_number_list), None, ast.clazz(_number_list_numr))],
    ),
    *ast.lookup(
        "DOWN",
        [
            ast.subst(
                "fraction", ast.clazz(_number_list), None, ast.clazz(_number_list_numr)
            ),
            ast.subst(
                ast.clazz(_number_list_dnom),
                ast.clazz(_number_list_numr),
                None,
                ast.clazz(_number_list_dnom),
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
