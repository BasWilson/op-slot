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
    sql = ''' INSERT INTO passwords(user_id,username,password,website)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, password)
    conn.commit()
    conn.close()
    return {"result": True}


def update_password(username, password, website, id, user_id):
    conn = create_connection("./opslot.db")
    sql = ''' UPDATE passwords SET username="%s", password="%s", website="%s" WHERE id="%s" AND user_id="%s"''' % (
        username, password, website, id, user_id)
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
    cur.execute(sql)
    conn.commit()
    conn.close()
    return {"result": True}


def create_user(user):
    conn = create_connection("./opslot.db")
    sql = ''' INSERT INTO users (email,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    conn.close()
    return {"result": True}


def update_user(email, password, user_id):
    conn = create_connection("./opslot.db")
    sql = ''' UPDATE users SET email="%s", password="%s" WHERE user_id="%s"''' % (
        email, password, user_id)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return {"result": True}


def get_user(user_id):
    conn = create_connection("./opslot.db")
    sql = ''' SELECT email, user_id FROM users WHERE user_id="%s"''' % (
        user_id)
    cur = conn.cursor()
    row = cur.execute(sql).fetchone()
    conn.commit()
    conn.close()
    return json.dumps(row)


def get_user_by_email_and_pass(email, password):
    conn = create_connection("./opslot.db")
    sql = ''' SELECT email, user_id FROM users WHERE email="%s" AND password="%s"''' % (
        email, password)
    cur = conn.cursor()
    row = cur.execute(sql).fetchone()
    conn.commit()
    conn.close()
    if row is None:
        return None
    else:
        return {
            "email": row[0],
            "user_id": row[1]
        }


def delete_user(user_id):
    conn = create_connection("./opslot.db")
    sql = ''' DELETE FROM users WHERE user_id="%s"''' % (user_id)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return {"result": True}
