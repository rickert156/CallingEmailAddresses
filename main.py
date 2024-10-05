from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib, csv, os, shutil

from template.letter import theme, letter
from utils.buffer import writeBuffer
from utils.createDir import createDir
from utils.trash import DeleteTrash

ACCOUNT = 'account.csv'
BASE_FILE = 'base.csv'
SENT_DIR = 'Sent'
BUFFER = 'Buffer'

LIMIT_LETTER = 2

def main(number, recipient, log, pwd):
    writeBuffer(recipient, theme, letter)
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
            shutil.move(f'{BUFFER}/{recipient}', f'{SENT_DIR}/{recipient}')
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Ошибка отправки письма, адрес отклонен: {e}")
        except smtplib.SMTPException as e:
            print(f"Ошибка при отправке письма: {e}")
        finally:
            server.quit()
            DeleteTrash()

        print(f"[{number}] {log} => Email sent to {msg['To']}")
        

    except Exception as e:
        print(f"Общая ошибка: {e}")

def readBase():
    with open(ACCOUNT, 'r') as file:
        number_login = 0
        for row in csv.DictReader(file):
            number_login+=1
            login = row['login']
            password = row['password']
            num_rec = 0
            with open(BASE_FILE, 'r') as file2:
                for user in csv.DictReader(file2):
                    recipient = user['Email']
                    if recipient not in os.listdir(f'{SENT_DIR}'):
                        main(number_login, recipient, login, password)
                        num_rec+=1
                        if num_rec == LIMIT_LETTER:break

if __name__ == '__main__':
    createDir()
    readBase()

