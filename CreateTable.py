import sqlite3

# 創建或連接到 SQLite 數據庫
conn = sqlite3.connect('CoolcatDB.db')
cursor = conn.cursor()

# 創建 BlackCarTable 表格
cursor.execute('''
CREATE TABLE BlackCar (
    CarName NVARCHAR(15) NOT NULL PRIMARY KEY,
    Finished CHAR(1) DEFAULT 'N' NOT NULL,
    PlannedDate DATETIME
)
''')

# 創建 BlackCarPassenger 表格
cursor.execute('''
CREATE TABLE BlackCarPassenger (
    CarName NVARCHAR(16) NOT NULL,
    JoinNumber INT NOT NULL,
    PlayerName NVARCHAR(16) NOT NULL,
    PRIMARY KEY (CarName, JoinNumber),
    FOREIGN KEY (CarName) REFERENCES BlackCarTable(CarName)
)
''')

# 提交更改並關閉連接
conn.commit()
conn.close()