import smtplib
from email.mime.text import MIMEText

def sendMail(me, you, msg):
    password = ""
    with open("./password.txt", "r") as f:
        password = f.readline()
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(me, password)
    msg = MIMEText(msg)
    msg['Subject'] = '나이키 드로우 목록'
    smtp.sendmail(me, you, msg.as_string())
    smtp.quit()