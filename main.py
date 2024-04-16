import smtplib
from passwords import *

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg="Subject:Hello")
connection.close()
