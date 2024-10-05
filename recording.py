import csv, sqlite3, time
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
    timeLog = time.strftime("Time: %H-%M-%S  Date: %d/%m/%Y")
    writeResult = f"""\
            INSERT INTO users (email, name, domain, status, date)
            VALUES ('{email}', '{username}', '{domain}', 'OK', '{timeLog}')
            """
    con = sqlite3.connect(base)
    cur = con.cursor()
    try:cur.execute(writeResult)
    except sqlite3.DatabaseError as ex:print(f"Error: {ex}")
    else:con.commit()
    cur.close()
    con.close()

   
