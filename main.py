from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, csv
from login import log, pwd
from letter import theme, letter

BASE_FILE = 'base.csv'

def main(number, recipient):
    try:
        msg = MIMEMultipart()
        message = letter

        password = pwd
        msg['From'] = log
        msg['To'] = recipient
        msg['Subject'] = f"{number} {theme}"

        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP_SSL('smtp.hostinger.com', 465)
        except smtplib.SMTPConnectError as e:
            print(f"Ошибка подключения к SMTP-серверу: {e}")
            return

        try:
            server.login(msg['From'], password)
        except smtplib.SMTPAuthenticationError as e:
            print(f"Ошибка авторизации: {e}")
            return

        try:
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Ошибка отправки письма, адрес отклонен: {e}")
        except smtplib.SMTPException as e:
            print(f"Ошибка при отправке письма: {e}")
        finally:
            server.quit()

        print(f"[{number}] Email sent to {msg['To']}")

    except Exception as e:
        print(f"Общая ошибка: {e}")

def readBase():
    with open(BASE_FILE, 'r') as file:
        number=0
        for row in csv.DictReader(file):
            number+=1
            recipient = row['Email']
            main(number, recipient)

readBase()
