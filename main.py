import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "USER_EMAIL"
MY_PASS = "USER_PASSWORD"


now = dt.datetime.now()
current_date = now.day
current_month = now.month
today_tuple = (current_month, current_date)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


def wish_birthday():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=mail,
                            msg="Subject:Happy Birthday!\n\n"
                            f"{contents}")


if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    mail = birthday_person["email"]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    wish_birthday()

else:
    month = dt.datetime.month
    print(f"no birthdays today\n{current_month},{current_date} ")
