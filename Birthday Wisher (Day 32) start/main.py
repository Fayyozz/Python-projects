import smtplib
import random
import datetime as dt

# CONSTANTS for using smtp
MY_GMAIL = "00010847f@gmail.com"
MY_PASSWORD = "61251526"
TO_EMAIL = "fayyoz01@outlook.com"

# current week day
now = dt.datetime.now()
current_week_day = now.weekday()

# getting the quotes from the file
with open("quotes.txt", "r") as data:
    quotes = data.readlines()
# getting random quote from the quotes list
random_quote = random.choice(quotes)

# sending the quote to the email address if the day matches
if current_week_day == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL, to_addrs=TO_EMAIL,
                            msg=f"Subject: Monday Motivation \n\n  {random_quote}")


