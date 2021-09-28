import random
import math
from pylatex import NoEscape
import format


def num_format(a):
    return ("{:,f}".format(a)).rstrip("0").rstrip(".")


def operator(
    operator,
    string_operator: str,
    min_number: int = 0,
    max_number: int = 10,
    decimal_places: int = 0,
    horizontal: bool = True,
):
    a = (
        random.randint(
            min_number * 10 ** decimal_places, max_number * 10 ** decimal_places
        )
        / 10 ** decimal_places
    )
    b = (
        random.randint(
            min_number * 10 ** decimal_places, max_number * 10 ** decimal_places
        )
        / 10 ** decimal_places
    )
    if a < b:
        a, b = b, a
    if horizontal:
        return format.horizontal(
            [num_format(a), num_format(b)],
            [string_operator, ""],
            num_format(round(operator(a, b))),
        )
    return format.vertical(
        [num_format(a), num_format(b)],
        [string_operator, ""],
        num_format(round(operator(a, b))),
    )


def power(min_number: int = 0, max_number: int = 10, decimal_places: int = 0):
    a = (
        random.randint(
            min_number * 10 ** decimal_places, max_number * 10 ** decimal_places
        )
        / 10 ** decimal_places
    )
    b = (
        random.randint(
            min_number * 10 ** decimal_places, max_number * 10 ** decimal_places
        )
        / 10 ** decimal_places
    )
    return NoEscape(f"${num_format(a)} ^{{{num_format(b)}}} =$"), NoEscape(
        f"${num_format(a)} ^{{{num_format(b)}}} = \color{{red}}{num_format(a**b)}$"
    )


def divide(min_number: int = 0, max_number: int = 10, mode: str = "remainder"):
    a = random.randint(min_number, max_number)
    b = random.randint(min_number, max_number)
    if mode == "remainder":
        return format.remainder([a, b], [a // b, a % b])
    elif mode == "mixed":
        return format.mixed_fraction([a, b], [a // b, a % b])
    elif mode == "long":
        return format.long_division([a, b], [a // b, a % b])


def dec_divide(
    min_number: int = 0,
    max_number: int = 10,
    decimal_places: int = 0,
    divisor_magnitude: int = 0,
):
    d = random.randint(2, 12) * 10 ** divisor_magnitude
    a = (
        random.randint(
            min_number * 10 ** decimal_places, max_number * 10 ** decimal_places
        )
        / 10 ** decimal_places
    )
    return format.horizontal(
        [num_format(round(d * a, decimal_places - divisor_magnitude)), num_format(d)],
        ["\div", "="],
        f"{num_format(a)}",
    )
