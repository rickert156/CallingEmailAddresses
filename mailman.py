from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib, csv, os, shutil, time

from templates.letter import theme, letter
from utils.buffer import writeBuffer
from utils.createDir import createDir
from utils.trash import DeleteTrash
from utils.recording import createTable
from utils.recording import writeData

ACCOUNT = 'account.csv'
BASE_FILE = 'NewClutch.csv'
#BASE_FILE = 'users.csv'
SENT_DIR = 'Sent'
BUFFER = 'Buffer'
DIR_ENCODE = 'ENCODE'

LIMIT_LETTER = 300

def main(number, recipient, log, pwd, name, domain):
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
            writeData(recipient, name, domain)
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Ошибка отправки письма, адрес отклонен: {e}")
        except smtplib.SMTPException as e:
            print(f"Ошибка при отправке письма: {e}")
        except UnicodeEncodeError:
            if not os.path.exists(DIR_ENCODE):os.makedirs(DIR_ENCODE)
            with open(f'{DIR_ENCODE}/{recipient}', 'a+') as file:file.write(recipient)
            with open(f'{SENT_DIR}/{recipient}', 'a+') as file:file.write(recipient)
            print('Error encoding')
        finally:
            server.quit()
            DeleteTrash()

        print(f"[ {number} ] {log} => Email sent to {msg['To']}")
        

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
            with open(BASE_FILE, 'r', encoding='utf-8') as file2:
                for user in csv.DictReader(file2):
                    recipient = user['Email']
                    recipient = recipient.encode('utf-8').decode('utf-8')
                    name = user['Name']
                    domain = user['Domain']
                    if recipient not in os.listdir(f'{SENT_DIR}'):
                        main(number_login, recipient, login, password, name, domain)
                        num_rec+=1
                        if num_rec == LIMIT_LETTER:break

if __name__ == '__main__':
    createTable()
    createDir()
    readBase()

