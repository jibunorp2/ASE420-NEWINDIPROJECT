import sqlite3
from datetime import datetime
import datetime

conn = sqlite3.connect('../main.db')

conn.execute('''CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY KEY,
    date DATE,
    start_time TIME,
    end_time TIME,
    task STRING NOT NULL,
    tag TEXT NOT NULL);''')

def create_table():
    conn.execute('''CREATE TABLE IF NOT EXISTS todo(
        id INTEGER PRIMARY KEY,
        date DATE,
        start_time TIME,
        end_time TIME,
        task STRING NOT NULL,
        tag TEXT NOT NULL);''')

def view():
    query = "SELECT * FROM todo;"
    return conn.execute(query)


def drop_table():
    return conn.execute('''DROP TABLE todo''')


def insertdata(date, start_time, end_time, task, tag):
    query = "INSERT INTO todo(date, start_time, end_time, task, tag) VALUES(?, ?, ?, ?, ?);"
    conn.execute(query, (date, start_time, end_time, task, tag,))
    conn.commit()


def deletebytag(tagid):
    query = "DELETE FROM todo WHERE id = ?;"
    conn.execute(query, (tagid,))
    conn.commit()


def updatedata(tagid, newtask):
    query = "UPDATE todo SET task = ? WHERE tag = ?;"
    conn.execute(query, (newtask, tagid))
    conn.commit()


def query_by_tag(tag):
    query = "SELECT * FROM todo WHERE tag = ?;"
    result = conn.execute(query, (tag,))
    return result.fetchall()


def query_by_date(date):
    query = "SELECT * FROM todo WHERE date = ?;"
    result = conn.execute(query, (date,))
    return result.fetchall()


def query_by_task(task):
    query = "SELECT * FROM todo WHERE task = ?;"
    result = conn.execute(query, (task,))
    return result.fetchall()
