# import smtplib
# from passwords import *
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
#                         msg="Subject:Hello\n\nThis is the body of the email.\n Taha Ahmed Hussein")

import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1996 ,month=4 ,day=17)
print(date_of_birth)