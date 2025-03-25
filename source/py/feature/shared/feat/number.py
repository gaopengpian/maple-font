import source.py.feature.utils as fea

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

zero = fea.subst_list(
    ["zero", "zero.dnom", "zero.numr", "zeroinferior", "zerosuperior"], ".zero"
)

sinf = fea.subst_list(_number_list, "inferior")
sups = fea.subst_list(_number_list, "superior")
numr = fea.subst_list(_number_list, ".numr")
dnom = fea.subst_list(_number_list, ".dnom")
ordn = [
    fea.subst(fea.clazz(_number_list), fea.clazz("A a"), None, "ordfeminine"),
    fea.subst(fea.clazz(_number_list), fea.clazz("O o"), None, "ordmasculine"),
]
frac = [
    fea.def_lookup("FRAC", [fea.subst(None, "/", None, "fraction")]),
    fea.def_lookup(
        "UP",
        [fea.subst(None, fea.clazz(_number_list), None, fea.clazz(_number_list_numr))],
    ),
    fea.def_lookup(
        "DOWN",
        [
            fea.subst(
                "fraction", fea.clazz(_number_list), None, fea.clazz(_number_list_numr)
            ),
            fea.subst(
                fea.clazz(_number_list_dnom),
                fea.clazz(_number_list_numr),
                None,
                fea.clazz(_number_list_dnom),
            ),
        ],
    ),
]

number_features: dict[
    str, fea.Sequence[fea.ast.SingleSubstStatement | fea.ast.LookupBlock]
] = {
    "zero": zero,
    "sinf": sinf,
    "subs": sinf,
    "sups": sups,
    "numr": numr,
    "dnom": dnom,
    "frac": frac,
    "ordn": ordn,
}
