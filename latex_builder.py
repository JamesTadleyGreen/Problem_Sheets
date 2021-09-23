import builtins
import numpy as np

from pylatex import (
    Document,
    Section,
    Subsection,
    Tabularx,
    Math,
    TikZ,
    Axis,
    Plot,
    Figure,
    Matrix,
    Alignat,
    NoEscape,
    Package,
)
from pylatex.utils import italic
from pylatex.basic import NewPage
import os


class makeLatex:
    def __init__(
        self,
        file_name,
        title,
        builder_function_list: list,
        horizontal_no=4,
        vertical_no=4,
    ) -> None:
        self.file_name = file_name
        self.title = title
        self.builder_function_list = builder_function_list
        self.horizontal_no = horizontal_no
        self.vertical_no = vertical_no

    def single_function_generate_data(self):
        builder_function = self.builder_function_list[0]
        number_of_questions = self.horizontal_no * self.vertical_no
        return zip(*[builder_function() for _ in range(number_of_questions)])

    def single_function_pdf_template(self, data):
        question_list, solution_list = data

        geometry_options = {"tmargin": "1cm", "lmargin": "1cm", "rmargin": "1cm"}
        doc = Document(geometry_options=geometry_options)
        doc.packages.append(Package("xcolor"))

        with doc.create(Section(f"{self.title} Questions", numbering=False)):
            with doc.create(Tabularx("X" * self.horizontal_no, row_height=10)) as table:
                for i in range(self.vertical_no):
                    table.add_row(
                        question_list[
                            i * self.horizontal_no : (i + 1) * self.horizontal_no
                        ]
                    )
                    # table.add_hline()

        doc.append(NewPage())

        with doc.create(Section(f"{self.title} Solutions", numbering=False)):
            with doc.create(Tabularx("X" * self.horizontal_no, row_height=10)) as table:
                for i in range(self.vertical_no):
                    table.add_row(
                        solution_list[
                            i * self.horizontal_no : (i + 1) * self.horizontal_no
                        ]
                    )
                    # table.add_hline()

        doc.generate_pdf(f"PDFs/{self.file_name}", clean_tex=False)

    def build_pdf(self):
        if len(self.builder_function_list) == 1:
            self.single_function_pdf_template(self.single_function_generate_data())
