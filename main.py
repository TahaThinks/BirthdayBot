import smtplib
from passwords import *
import datetime as dt
from random import choice


def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                            msg=f"Subject:Quote of the Day\n\n{message}\n\n\n Taha Ahmed Hussein")


# Get Day of the Week
tuesday = 1
now = dt.datetime.now()
day_of_week = now.weekday()

# Get Quote
with open("quotes.txt") as file:
    lines = file.readlines()

if day_of_week == tuesday:
    send_mail(choice(lines))
else:
    pass
