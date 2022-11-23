import pandas
import datetime
import random
import smtplib


my_email = "nischal.testmail257@gmail.com"
my_password = "NJ07_Coder"


# TODO 1. Update the birthdays.csv
# Done

# TODO 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
now = datetime.datetime.now()
today = (now.month, now.day)

birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays:
    # TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file:
        data = file.read()
        data = data.replace("[NAME]", birthdays[today][0])

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays[today][1],
            msg=f"Subject:Happy Birthday {birthdays[today][0]}\n\n{data}"
        )
