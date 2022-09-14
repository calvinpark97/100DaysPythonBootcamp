##################### Extra Hard Starting Project ######################
import datetime as dt
import csv, pandas, smtplib, os, random

PLACEHOLDER = "[NAME]"
my_email= "SECRET EMAIL"
my_password= "SECRET CODE"

# 1. Update the birthdays.csv (add any days)
header = ("name", "email", "year", "month", "day")
calvin_bday = ("Calvin", "SECRET EMAIL", "1997", "03", "13")
lina_bday = ("Lina", "SECRET EMAIL", "1997", "09", "11")
test_bday = ("Test", "SECRET EMAIL", "1997", "09", "11")
test_2_bday = ("Test2", "SECRET EMAIL", "1997", "05", "11")
test_3_bday = ("Test3", "SECRET EMAIL", "1997", "09", "12")
with open("birthdays.csv", "a") as birthday_file:
    writer = csv.writer(birthday_file)
    #Temporarily added birthday and header, probably a better way to add?
    #writer.writerow(header)
    #writer.writerow(test_3_bday)
    #writer.writerow(calvin_bday)
    #writer.writerow(lina_bday)


# 2. Check if today matches a birthday in the birthdays.csv
todays_date = dt.datetime.now()
todays_month = todays_date.month
todays_day = todays_date.day

birthday_df =  pandas.read_csv('birthdays.csv')
birthday_dict = birthday_df.to_dict()
for info in range(len(birthday_dict)):
    if todays_month == birthday_dict["month"][info] and todays_day == birthday_dict["day"][info]:
        name = birthday_dict["name"][info]
        email = birthday_dict["email"][info]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#select a random letter
        letter = random.choice(os.listdir("letter_templates"))
        with open(f"./letter_templates/{letter}", "r") as letter_file:
            letter_content = letter_file.read()
            new_letter = letter_content.replace(PLACEHOLDER, name)

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr="Secret Admirer",
                           to_addrs=email,
                            msg=f"Subject: Happy Birthday\n\n{new_letter}")




