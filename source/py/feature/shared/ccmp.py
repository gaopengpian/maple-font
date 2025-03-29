import source.py.feature.ast as ast
from source.py.feature.shared.clazz import uppercase


comb_top_acc = ast.Clazz(
    "CombiningTopAccents",
    [
        "acutecomb",
        "brevecomb",
        "caroncomb",
        "circumflexcomb",
        "commaturnedabovecomb",
        "dblgravecomb",
        "dieresiscomb",
        "dotaccentcomb",
        "gravecomb",
        "hookabovecomb",
        "hungarumlautcomb",
        "macroncomb",
        "ringcomb",
        "tildecomb",
    ],
)

comb_non_top_acc = ast.Clazz(
    "CombiningNonTopAccents",
    [
        "cedillacomb",
        "dotbelowcomb",
        "ogonekcomb",
        "ringbelowcomb",
        "horncomb",
        "slashlongcomb",
        "slashshortcomb",
        "strokelongcomb",
    ],
)

marks = [
    "dieresiscomb",
    "dotaccentcomb",
    "gravecomb",
    "acutecomb",
    "hungarumlautcomb",
    "circumflexcomb",
    "caroncomb",
    "brevecomb",
    "ringcomb",
    "tildecomb",
    "macroncomb",
    "hookabovecomb",
    "dblgravecomb",
    "commaturnedabovecomb",
    "horncomb",
    "dotbelowcomb",
    "commaaccentcomb",
    "cedillacomb",
    "ogonekcomb",
    "dieresis",
    "dotaccent",
    "acute",
    "hungarumlaut",
    "circumflex",
    "caron",
    "breve",
    "ring",
    "tilde",
    "macron",
    "tonos",
    "brevecomb_acutecomb",
    "brevecomb_gravecomb",
    "brevecomb_hookabovecomb",
    "brevecomb_tildecomb",
    "circumflexcomb_acutecomb",
    "circumflexcomb_gravecomb",
    "circumflexcomb_hookabovecomb",
    "circumflexcomb_tildecomb",
]

marks_comb = ast.Clazz("MarksComb", marks)
marks_comb_case = ast.Clazz("MarksCombCase", [f"{m}.case" for m in marks])


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
    None,
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
    None,
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
        ast.subst(uppercase, marks_comb, None, marks_comb_case),
        ast.subst(None, marks_comb, marks_comb_case, marks_comb_case),
        ast.subst(marks_comb, marks_comb_case, None, marks_comb_case),
    ],
)

ccmp_features = ast.feature(
    "ccmp",
    [
        uppercase.state(),
        comb_top_acc.state(),
        comb_non_top_acc.state(),
        marks_comb.state(),
        marks_comb_case.state(),
        *ccmp_other,
        *ccmp_latin,
        ast.script("latn"),
        ast.Line("lookup ccmp_latin;"),
    ],
)
