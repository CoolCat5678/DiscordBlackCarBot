import sqlite3

# 連接到 SQLite 數據庫
conn = sqlite3.connect('CoolcatDB.db')
cursor = conn.cursor()


# INSERT Command
# INSERT INTO BlackCar
cursor.execute("INSERT INTO BlackCar (CarName, Finished, PlannedDate) VALUES ('CarA', 'N', '2024-04-01')")

# INSERT INTO BlackCarPassenger
cursor.execute("INSERT INTO BlackCarPassenger (CarName, JoinNumber, PlayerName) VALUES ('CarA', 1, 'Player1')")

# SELECT Command
# 執行 SELECT 查詢以選擇所有數據
cursor.execute("SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName")

# 獲取所有選擇的數據行
rows = cursor.fetchall()

# 打印選擇的數據
for row in rows:
    print(row)

# 提交更改並關閉連接
conn.commit()
conn.close()