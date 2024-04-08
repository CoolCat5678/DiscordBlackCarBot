import sqlite3

# 創建或連接到 SQLite 數據庫
conn = sqlite3.connect('./database/CoolcatDB.db')
cursor = conn.cursor()

# 創建 BlackCarTable 表格
cursor.execute('''
CREATE TABLE BlackCar (
    CarName NVARCHAR(16) NOT NULL,
    Month INT NOT NULL,
    Finished CHAR(1) DEFAULT 'N' NOT NULL,
    PlannedDate DATETIME,
    FightTime INT,
    
    PRIMARY KEY (CarName, Month)
)
''')

# 創建 BlackCarPassenger 表格
cursor.execute('''
CREATE TABLE BlackCarPassenger (
    CarName NVARCHAR(16) NOT NULL,
    Month INT NOT NULL,
    JoinNumber INT NOT NULL,
    PlayerName NVARCHAR(16) NOT NULL,
    DiscordID NVARCHAR(18),
    
    PRIMARY KEY (CarName, Month, JoinNumber),
    FOREIGN KEY (CarName, Month) REFERENCES BlackCarTable(CarName, Month)
)
''')

# region test data
# 插入 BlackCarTable 表格的數據
cursor.execute('''
INSERT INTO BlackCar (CarName, Month, PlannedDate, FightTime) VALUES
('Car1', 1, '2024-04-01', 15),
('Car3', 2, '2024-04-05', 20),
('Car3', 3, '2024-04-10', 16)
''')

# 插入 BlackCarPassenger 表格的數據
# cursor.execute('''
# INSERT INTO BlackCarPassenger (CarName, Month, JoinNumber, PlayerName, DiscordID) VALUES
# ('Car1', 1, 1, 'Player1', '123456'),
# ('Car1', 1, 2, 'Player2', '234567'),
# ('Car1', 1, 3, 'Player3', '345678'),

# ('Car3', 2, 1, 'Player4', '456789'),
# ('Car3', 2, 2, 'Player5', '567890'),
# ('Car3', 2, 3, 'Player6', '678901'),
# ('Car3', 2, 4, 'Player7', '789012'),

# ('Car3', 3, 1, 'Player8', '890123'),
# ('Car3', 3, 2, 'Player9', '901234'),
# ('Car3', 3, 3, 'Player10', '012345'),
# ('Car3', 3, 4, 'Player11', '123456'),
# ('Car3', 3, 5, 'Player12', '234567')
# ''')
# endregion

# 提交更改並關閉連接
conn.commit()
conn.close()