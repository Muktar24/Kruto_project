import sqlite3

db_connection = sqlite3.connect("main_db.db")
cursor_execute = db_connection.cursor()
cursor_execute.execute("DROP TABLE IF EXISTS userer")

cursor_execute.execute('''
CREATE TABLE userer(
user_id integer primary key,
user_name text not null,
email text unique not null)
''')

users = [
    ("1","aminu_iliyasu", "iliyasuaminu50@gmail.com"),
    ("2","iliyasu_aminu", "xioleb@tr.pte.hu")
]
cursor_execute.executemany("INSERT INTO userer(user_id, user_name, email) values(?, ?, ?)", users)

print(cursor_execute.fetchall())

print()
print()