import sqlite3
# 連接到 SQLite 數據庫

# database may be replaced by a parameter
database = 'CoolcatDB'
_dbPath = f'./database/{database}.db'

# region dsd
conn = sqlite3.connect(_dbPath)
cursor = conn.cursor()
# endregion  

# region function
def SearchAll():
    # 執行 SELECT 查詢以選擇所有數據
    cursor.execute("SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName")    

    # 獲取所有選擇的數據行
    rows = cursor.fetchall()
    
    # 打印選擇的數據
    for row in rows:
        print(row)
        
def CreateCar():
    conn = sqlite3.connect(_dbPath)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO BlackCar (CarName, Finished, PlannedDate) VALUES ('CarA', 'N', '2024-04-01')")
    conn.commit()
    conn.close()

def JoinCar():  
    conn = sqlite3.connect(_dbPath)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO BlackCarPassenger (CarName, JoinNumber, PlayerName) VALUES ('CarA', 1, 'Player1')")
    conn.commit()
    conn.close()
# endregion

# 關閉連接
conn.close()