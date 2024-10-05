import csv, sqlite3
from sql.createTable import addInfo

base = 'calling.db'
sourceFile = 'base.csv'

def createTable():
    con = sqlite3.connect(base)
    cur = con.cursor()
    try:cur.executescript(addInfo)
    except sqlite3.DatabaseError as ex:print(f"Error: {ex}")
    else:print("Успешный запрос к Базе Данных...")

def writeData(email, username, domain):
    writeResult = f"""\
            INSERT INTO users (email, name, domain, status)
            VALUES ('{email}', '{username}', '{domain}', 'OK')
            """
    con = sqlite3.connect(base)
    cur = con.cursor()
    try:cur.execute(writeResult)
    except sqlite3.DatabaseError as ex:print(f"Error: {ex}")
    else:
        print(f'Данные записаны: {email}')
        con.commit()
    cur.close()
    con.close()

   
