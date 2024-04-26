### TABLE BlackCar
# CarName NVARCHAR(16) NOT NULL,            -- 車名
# Year INT NOT NULL,                        -- 日期年
# Month INT NOT NULL,                       -- 日期月
# Finished CHAR(1) DEFAULT 'N' NOT NULL,    -- 結束('Y'/'N')
# PlannedDate DATETIME,                     -- 發車日期
# DiscordID NVARCHAR(18),                   -- 車長DC
# FightTime INT,                            -- 預計幾分內

###
# CarName NVARCHAR(16) NOT NULL,            -- 車名
# Year INT NOT NULL,                        -- 日期年
# Month INT NOT NULL,                       -- 日期月
# QueueNumber INT NOT NULL,                  -- 加入順序
# PlayerName NVARCHAR(16) NOT NULL,         -- 玩家ID
# DiscordID NVARCHAR(18),                   -- 玩家DC

import sqlite3
from pathlib import Path

# 創建或連接到 SQLite 數據庫
conn = sqlite3.connect(Path(__file__).parents[1].joinpath('database', 'CoolcatDB.db'))
cursor = conn.cursor()

def main():
    # 創建 BlackCarTable 表格
    cursor.execute('''
    CREATE TABLE BlackCar (
        CarName NVARCHAR(16) NOT NULL,
        Year INT NOT NULL,
        Month INT NOT NULL,
        Finished CHAR(1) DEFAULT 'N' NOT NULL,
        PlannedDate DATETIME,
        DiscordID NVARCHAR(18),
        FightTime INT,
        
        PRIMARY KEY (CarName, Year, Month)
    )
    ''')

    # 創建 BlackCarPassenger 表格
    cursor.execute('''
    CREATE TABLE BlackCarPassenger (
        CarName NVARCHAR(16) NOT NULL,
        Year INT NOT NULL,
        Month INT NOT NULL,
        QueueNumber INT NOT NULL,
        PlayerName NVARCHAR(16) NOT NULL,
        DiscordID NVARCHAR(18),
        
        PRIMARY KEY (CarName, Year, Month, PlayerName),
        FOREIGN KEY (CarName, Year, Month) REFERENCES BlackCarTable(CarName, Year, Month)
    )
    ''')

    # 提交更改並關閉連接
    conn.commit()
    conn.close()
    
if __name__=='__main__':
    main()