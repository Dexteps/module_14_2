import sqlite3

db = sqlite3.connect('database.db')
cursor =  db.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL,
    Age INTEGER,
    Balance INTEGER NOT NULL
    )'''
)
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (Username, Email, Age, Balance) VALUES(?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i*10}', f'1000',))
# cursor.execute('UPDATE Users SET Balance = 500 WHERE Id % 2 != 0')
# for i in range(1, 11, 3):
#     cursor.execute(f'DELETE FROM users WHERE Id == {i}')
# cursor.execute('SELECT * FROM Users WHERE age != 60')
# res = cursor.fetchall()
# for el in res:
#     print(f'Имя: {el[1]}|Почта:{el[2]}|Возраст: {el[3]}|Баланс: {el[4]}')

cursor.execute('DELETE FROM Users WHERE Id == 6')
cursor.execute('SELECT COUNT(*) FROM Users')
cnt = cursor.fetchone()[0]
print(cnt)
cursor.execute('SELECT SUM(Balance) FROM Users')
sum_bal = cursor.fetchone()[0]
print(sum_bal)
print(sum_bal/cnt)

db.commit()
db.close()
