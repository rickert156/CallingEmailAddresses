import sqlite3

base = 'calling.db'

def output():
    con = sqlite3.connect(base)
    cur = con.cursor()
    sql = """\
        SELECT * FROM users
        """
    try:
        cur.execute(sql)
        for id_user, email, name, domain, status, date in cur:print(f"Email: {email} | Name: {name} | Domain: {domain} | Status: {status} | Date: {date}")
    except sqlite3.DatabaseError as ex:print(f"Error: {ex}")
    else:print("Успех")

    cur.close()
    con.close()

#output()
