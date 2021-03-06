from latex_builder import makeLatex
import arithmitic
import operator

# builder = makeLatex(
#     "Addition",
#     "Simple Addition",
#     [
#         lambda: arithmitic.operator(
#             operator.add, "+", -100, 10000, decimal_places=0, horizontal=False
#         )
#     ],
# ).build_pdf()

# builder = makeLatex(
#     "Subtraction",
#     "Simple Subtraction",
#     [
#         lambda: arithmitic.operator(
#             operator.sub, "-", -200, 100, decimal_places=3, horizontal=False
#         )
#     ],
# ).build_pdf()

# builder = makeLatex(
#     "Multiplication",
#     "Simple Multiplication",
#     [
#         lambda: arithmitic.operator(
#             operator.mul, "\\times", -200, 100, decimal_places=3, horizontal=False
#         )
#     ],
# ).build_pdf()

# builder = makeLatex(
#     "Power",
#     "Simple Power",
#     [lambda: arithmitic.power(0, 10, decimal_places=0)],
# ).build_pdf()

# builder = makeLatex(
#     "Divide", "Divide", [lambda: arithmitic.divide(1, 10, mode="mixed")]
# ).build_pdf()

# builder = makeLatex(
#     "Decimal Divide", "Decimal Divide", [lambda: arithmitic.dec_divide(1, 10, 2, 4)]
# ).build_pdf()

builder = makeLatex(
    "Daily Dozen",
    "Daily Dozen",
    [
        lambda: arithmitic.operator(
            operator.add, "+", -100, 10000, decimal_places=0, horizontal=False
        ),
        lambda: arithmitic.operator(
            operator.sub, "-", -100, 10000, decimal_places=0, horizontal=False
        ),
        lambda: arithmitic.operator(
            operator.mul, "\\times", -100, 10000, decimal_places=0, horizontal=False
        ),
        lambda: arithmitic.power(
            0, 5, decimal_places=0
        ),
        lambda: arithmitic.divide(
            1, 10, mode="mixed"
        ),
        lambda: arithmitic.divide(
            1, 10, mode="remainder"
        ),
        lambda: arithmitic.dec_divide(
            1, 10, decimal_places=2, divisor_magnitude=1
        ),
    ],
    horizontal_no=3, vertical_no=4,
).build_pdf()
