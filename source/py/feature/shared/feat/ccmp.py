import source.py.feature.ast as ast
from source.py.feature.shared.clazz import (
    comb_top_acc,
    comb_non_top_acc,
    marks_comb,
    marks_comb_case,
    upper,
)


def comb(config: list[list[str]]) -> list[ast.Line]:
    result = [ast.Line("lookupflag 0;")]
    for conf in config:
        c1, c2 = conf[0], conf[1]
        result.append(ast.__subst(f"{c1}comb {c2}comb", f"{c1}comb_{c2}comb"))
        result.append(
            ast.__subst(f"{c1}comb.case {c2}comb.case", f"{c1}comb_{c2}comb.case")
        )
    return result


ccmp_latin = ast.lookup(
    "ccmp_latin",
    comb(
        [
            ["breve", "acute"],
            ["breve", "grave"],
            ["breve", "hookabove"],
            ["breve", "tilde"],
            ["circumflex", "acute"],
            ["circumflex", "grave"],
            ["circumflex", "hookabove"],
            ["circumflex", "tilde"],
        ]
    ),
)
start_other = ast.clazz(["i", "i-cy", "iogonek", "idotbelow", "j", "je-cy"])
end_other = ast.clazz(
    [
        "idotless",
        "idotless",
        "iogonekdotless",
        "idotbelowdotless",
        "jdotless",
        "jdotless",
    ]
)

ccmp_other = ast.lookup(
    "ccmp_other",
    [
        ast.subst(
            None,
            start_other,
            comb_top_acc,
            end_other,
        ),
        ast.subst(
            None,
            start_other,
            [comb_non_top_acc, comb_top_acc],
            end_other,
        ),
        ast.subst(marks_comb, marks_comb, None, marks_comb_case),
        ast.subst(upper, marks_comb, None, marks_comb_case),
        ast.subst(None, marks_comb, marks_comb_case, marks_comb_case),
        ast.subst(marks_comb, marks_comb_case, None, marks_comb_case),
    ],
)

ccmp_features = ast.feature(
    "ccmp",
    [
        *ccmp_other,
        *ccmp_latin,
        ast.script("latn"),
        ast.Line("lookup ccmp_latin;")
    ],
)
