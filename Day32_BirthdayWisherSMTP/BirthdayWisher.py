import smtplib

my_email= "calvinsmtptest@gmail.com"
my_password= "v5vakffen24"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="calvinpark97@gmail.com", msg="Hello")
connection.close()