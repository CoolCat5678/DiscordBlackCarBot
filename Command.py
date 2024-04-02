import sqlite3

# 連接到 SQLite 數據庫
conn = sqlite3.connect('CoolcatDB.db')
cursor = conn.cursor()

# INSERT INTO BlackCar
cursor.execute("INSERT INTO BlackCar (CarName, Finished, PlannedDate) VALUES ('CarA', 'N', '2024-04-01')")

# INSERT INTO BlackCarPassenger
cursor.execute("INSERT INTO BlackCarPassenger (CarName, JoinNumber, PlayerName) VALUES ('CarA', 1, 'Player1')")

# 提交更改並關閉連接
conn.commit()
conn.close()