import sqlite3
from sqlite3 import Error
import json


def create_connection(db_file):
    newConn = None
    try:
        newConn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        return newConn


def create_table(create_table_sql):
    try:
        conn = create_connection("./opslot.db")
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


def create_password(password):
    conn = create_connection("./opslot.db")
    sql = ''' INSERT INTO passwords(user_id,username,password)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, password)
    conn.commit()
    conn.close()
    return {"result": True}


def update_password(username, password, id, user_id):
    conn = create_connection("./opslot.db")
    sql = ''' UPDATE passwords SET username="%s", password="%s" WHERE id="%s" AND user_id="%s"''' % (
        username, password, id, user_id)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return {"result": True}


def get_passwords(user_id):
    conn = create_connection("./opslot.db")
    sql = ''' SELECT * FROM passwords WHERE user_id="%s"''' % (user_id)
    cur = conn.cursor()
    rows = cur.execute(sql).fetchall()
    conn.commit()
    conn.close()
    return json.dumps(rows)


def delete_password(id):
    print('Deleting password: %s' % (id))
    conn = create_connection("./opslot.db")
    sql = ''' DELETE FROM passwords WHERE id="%s"''' % (id)
    cur = conn.cursor()
    rows = cur.execute(sql)
    conn.commit()
    conn.close()
    return {"result": True}
