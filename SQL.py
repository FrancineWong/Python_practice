import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')<sqlite3.Cursor object at 0x10f8aa260>

cursor.execute('insert into user (id, name) values (\'1\', \'fannie\')')<sqlite3.Cursor object at 0x10f8aa260>

cursor.rowcount

cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
	L = []
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute('select*from user where score between ? and ?', (low, high))
	values = cursor.fetchall()
	values_sorted = sorted((values, key=lambda i:i[2]))
	for i in values_sorted:
		L.append(i[1])
	return L