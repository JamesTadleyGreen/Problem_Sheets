from latex_builder import makeLatex
import arithmitic
import operator
import gmail
import os


def convert_today_to_yesterday(pdf_list):
    for pdf in pdf_list:
        os.remove(pdf.replace("Daily", "Yesterdaily"))
        os.rename(pdf, pdf.replace("Daily", "Yesterdaily"))


def daily_dozen_pdf():
    makeLatex(
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
            lambda: arithmitic.power(0, 5, decimal_places=0),
            lambda: arithmitic.divide(1, 10, mode="mixed"),
            lambda: arithmitic.divide(1, 10, mode="remainder"),
            lambda: arithmitic.dec_divide(1, 10, decimal_places=2, divisor_magnitude=1),
        ],
        horizontal_no=3,
        vertical_no=4,
    ).build_pdf()


def compose_email(email_list):
    from datetime import datetime, timedelta

    message_string = f"""<p>
        <b>{datetime.today().strftime('%d %B %Y')}</b><br><br>
        Hello and welcome to {datetime.today().strftime('%A')}'s Daily Dozen.<br>
        {(datetime.today() - timedelta(1)).strftime('%A')}'s answers are also attached.</p>
    """

    gm = gmail.Gmail("", "")
    service = gm.credentials()
    message = gm.create_message(
        "jamsterxop@gmail.com",
        email_list,
        "Daily Dozen",
        message_string,
        ["./PDFs/Daily Dozen Questions.pdf", "./PDFs/Yesterdaily Dozen Solutions.pdf"],
        None,
    )
    print(gm.create_draft(service, message, "me"))


convert_today_to_yesterday(
    ["./PDFs/Daily Dozen Questions.pdf", "./PDFs/Daily Dozen Solutions.pdf"]
)
daily_dozen_pdf()
compose_email(["tessgreen25@gmail.com", "roggreeny@gmail.com"])
