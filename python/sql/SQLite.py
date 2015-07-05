# -*- coding: utf-8 -*-
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute(r'create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 10)")
cursor.execute(r"insert into user values ('A-002', 'Bdam', 20)")
cursor.execute(r"insert into user values ('A-003', 'Cdam', 30)")
conn.commit()

def forValues(values):
    for value in values:
        i = ''
        for item in value:
            i += str(item) + '\n'
        print(i)
    
def get_score_in(cursor):
    low = input('输入一个最低分： ')
    high = input('输入一个最高分： ')
    cursor.execute(r'select * from user where score between ? and ?', (low, high))
    values = cursor.fetchall()
    forValues(values)
    cursor.close()
    conn.close()

get_score_in(cursor)

