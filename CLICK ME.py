import random
from latex_builder import makeLatex
import arithmitic
import operator
import gmail
import os

def read_emails(path_to_emails: str):
    with open(path_to_emails, "r") as f:
       output = [(line.strip()).split()[0] for line in f]
    return output

def convert_today_to_yesterday(pdf_list):
    for pdf in pdf_list:
        try:
            os.remove(pdf.replace("Daily", "Yesterdaily"))
        except:
            pass
        try:
            os.rename(pdf, pdf.replace("Daily", "Yesterdaily"))
        except:
            pass

################################################################-DAD HERE-#############################################################################
def daily_dozen_pdf():
    makeLatex(
        "Daily Dozen",
        "Daily Dozen",
        [
            lambda: arithmitic.operator( 
                operator.add, "+", 1, 10000, decimal_places=0, horizontal=False
            ),
            lambda: arithmitic.operator(
                operator.sub, "-", 1, 10000, decimal_places=0, horizontal=False
            ),
            lambda: arithmitic.operator(
                operator.mul, "\\times", 2, 1000, decimal_places=0, horizontal=False
            ),
            # lambda: arithmitic.power(0, 5, decimal_places=0),
            # lambda: arithmitic.divide(1, 10, mode="mixed"),
            # lambda: arithmitic.divide(1, 10, mode="remainder"),
            lambda: arithmitic.dec_divide(1, 10, decimal_places=random.randint(0,3), divisor_magnitude=random.randint(0, 4)),
        ],
        horizontal_no=4,
        vertical_no=3,
    ).build_pdf()
#######################################################################################################################################################


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


#email_list = read_emails("./emails.txt")
convert_today_to_yesterday(
    ["./PDFs/Daily Dozen Questions.pdf", "./PDFs/Daily Dozen Solutions.pdf"]
)
daily_dozen_pdf()
print('Done!')
#compose_email(email_list)
