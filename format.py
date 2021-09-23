from pylatex import NoEscape


def horizontal(symbol_list: list, operator_list: list, solution: str):
    question_string = "".join([str(a) + b for a, b in zip(symbol_list, operator_list)])
    solution_string = question_string + " \color{red}" + solution
    return NoEscape(f"${question_string}$"), NoEscape(f"${solution_string}$")


def vertical(symbol_list: list, operator_list: list, solution: str):
    symbol_list = [f"${i}$&" for i in symbol_list]
    operator_list = [f"${i}$" for i in operator_list]
    question_string = "\\\\".join(
        [str(a) + b for a, b in zip(symbol_list, operator_list)]
    )
    question_string = "\\begin{tabular}{rr}" + question_string + "\\\\ \\hline"
    solution_string = question_string + "\color{red}" + f"${solution}$"
    question_string = question_string + "\color{white}" + solution

    return NoEscape(
        f"\\renewcommand{{\\arraystretch}}{{2}}{question_string}\\end{{tabular}}"
    ), NoEscape(
        f"\\renewcommand{{\\arraystretch}}{{2}}{solution_string}\\end{{tabular}}"
    )


def remainder(symbol_list: list, solution_list: list):
    question_string = f"{symbol_list[0]} \\div {symbol_list[1]} = "
    solution_string = (
        question_string
        + f"\\color{{red}}{solution_list[0]} \\textrm{{ r }} {solution_list[1]}"
    )

    return NoEscape(f"${question_string}$"), NoEscape(f"${solution_string}$")


def mixed_fraction(symbol_list: list, solution_list: list): # TODO Simplify the fractions
    question_string = f"{symbol_list[0]} \\div {symbol_list[1]} = "
    if solution_list[1] == 0:
        solution_string = question_string + f"\\color{{red}}{solution_list[0]}"
    else:
        solution_string = (
            question_string
            + f"\\color{{red}}{solution_list[0]} \\frac{{{solution_list[1]}}}{{{symbol_list[1]}}} "
        )

    return NoEscape(f"${question_string}$"), NoEscape(f"${solution_string}$")


def long_division(symbol_list: list, solution_list: list):
    pass # TODO format this