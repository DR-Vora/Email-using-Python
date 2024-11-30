# Email Sender

import smtplib


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email', 'Your Password')
    server.sendmail('Your Email', to, content)
    server.close()


if __name__ == "__main__":
    try:
        content = input("Type your Message \n")
        to = input("Whom to send the Email? , enter there email address\n")
        sendEmail(to, content)
        print("Email has been sent! 😉")
    except Exception as e:
        print(e)
        print("sorry ,Email not sent 😥")
