import sqlite3

# 連接到 SQLite 數據庫
conn = sqlite3.connect('CoolcatDB.db')
cursor = conn.cursor()

# 執行 SELECT 查詢以選擇所有數據
cursor.execute("SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName")

# 獲取所有選擇的數據行
rows = cursor.fetchall()

# 打印選擇的數據
for row in rows:
    print(row)

# 關閉連接
conn.close()