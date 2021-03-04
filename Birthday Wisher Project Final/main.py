
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "00010847f@gmail.com"
MY_PASSWORD = "61251526"

# getting today's day and month
now = dt.datetime.now()
day = now.day
month = now.month

# reading birthdays data from csv file then converting it to dictionaries of list
data = pandas.read_csv("./birthdays.csv")
birthdays_list = data.to_dict(orient="records")
print(birthdays_list)
for birthday in birthdays_list:
    print(birthday)
    if birthday["day"] == day and birthday["month"] == month:
        # getting the letter template then inserting name into it
        random_letter_index = random.randint(1, 3)
        with open(f"./letter_templates/letter_{random_letter_index}.txt", "r") as letter:
            letter_content = letter.read()
        # ready to send letter
        name = birthday["name"]
        ready_letter = letter_content.replace("[NAME]", name)
        # connecting to the SMTP host and sending the letter
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="fayyoz01@outlook.com",
                                msg=f"Subject: Happy Birthday\n\n {ready_letter}")
