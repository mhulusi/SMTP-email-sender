import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
import random
import string
from time import sleep
def generate_random_variable():
    return ''.join(random.choice(string.ascii_letters) for _ in range(5))
logo = """
$$\   $$\           $$\                     $$\  
$$ |  $$ |          $$ |                    \__|
$$ |  $$ |$$\   $$\ $$ |$$\   $$\  $$$$$$$\ $$\ 
$$$$$$$$ |$$ |  $$ |$$ |$$ |  $$ |$$  _____|$$ |
$$  __$$ |$$ |  $$ |$$ |$$ |  $$ |\$$$$$$\  $$ |
$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ | \____$$\ $$ |
$$ |  $$ |\$$$$$$  |$$ |\$$$$$$  |$$$$$$$  |$$ |
\__|  \__| \______/ \__| \______/ \_______/ \__|                                                                                                                                                                                                                                                                 
"""

print(logo)
print('Hulusi SMTP e-mail sender 1.0')
print('github: mhulusi')
print()
sender_email = input("Enter sender email: ")
pw = input("Enter password: ")
number = 0
subject = input("Enter subject: ")

with open("mails.txt", "r") as file:
    mail_list = file.read().splitlines()

port_number = int(input("Enter port number: "))
smtp_host = input("Enter smtp host: ")

server = smtplib.SMTP(smtp_host, port_number)
server.starttls()
server.login(sender_email, pw)
print("Login successful")

for line in mail_list:
    username, rec_mail = line.split(":")

    with open("draft.txt", "r") as template_file:
        template_content = template_file.read()

    html_content = template_content.replace("{username}", username)

    html_content = html_content.replace("C", rec_mail.strip())

    for i in range(1, 999):
        random_variable_name = f"{{random_variable{i}}}"
        random_variable_value = generate_random_variable()
        html_content = html_content.replace(random_variable_name, random_variable_value)

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = rec_mail.strip()
    message["Subject"] = subject
    message["Date"] = formatdate(localtime=True)
    message["Message-Id"] = make_msgid()
    message.attach(MIMEText(html_content, "html"))

    server.sendmail(sender_email, rec_mail, message.as_string())
    number += 1
    print(f"Email has been sent!: {rec_mail} ({number})" )
    sleep(1)

server.quit()
