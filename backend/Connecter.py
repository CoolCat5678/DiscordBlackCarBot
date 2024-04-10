import sqlite3
from datetime import datetime

# 更改cursor return to dict
def DictFactory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Connecter:
    __conn = sqlite3.Connection
    __cursor = sqlite3.Cursor
    def __init__(self, database: str="CoolcatDB"):
        """
        Constructor
        """
        __dbPath = f'./database/{database}.db'
        self.__conn = sqlite3.connect(__dbPath)
        self.__conn.row_factory = DictFactory
        self.__cursor = self.__conn.cursor() 
        
    def SearchCarMonth(self, month: int) -> list:
        """
        This function search car in month.

        return:
            list
        """
        self.__cursor.execute(f"SELECT * FROM BlackCar M WHERE M.Month={month}")    
        rows = self.__cursor.fetchall()
        return rows
            
    def SearchCarName(self, carName: str, month: int) -> list:
        """
        This function search car with name.
        
        return:
            list
        """
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName AND M.Month=D.Month WHERE M.CarName='{carName}' AND M.Month={month}")
        rows = self.__cursor.fetchall()
        return rows

    def CreateCar(self, CarName: str, month: int, day: int, playerName: str, discordID = str, fightTime: int=60) -> bool:
        """
        This function Create a new car.

        return:
            bool: success=true
        """
        try:
            date = FormattedDate(month, day)
            self.__cursor.execute(f"INSERT INTO BlackCar (CarName, Month, PlannedDate, FightTime, DiscordID) VALUES ('{CarName}', {month}, '{date}', {fightTime}, {discordID})")
            self.__conn.commit()
            self.JoinCar(CarName, month, playerName, discordID)
            return True
        
        except Exception as e:
            print(e)
            return False

    def JoinCar(self, CarName: str, month: int, playerName: str , discordID = str):  
        """
        This function calculates the area of a rectangle.

        Parameters:
            length  (float): The length of the rectangle.
            width   (float): The width of the rectangle.

        Returns:
            bool: success=true
        """
        try:
            # 檢查是否有車
            if(self.__cursor.execute(f"SELECT 1 FROM BlackCar WHERE CarName='{CarName}' AND Month={month} AND Finished='N'").fetchone()):
                pass
            else:
                print("Car Not Found")
                return False
            
            # 檢查是否加入過
            if(self.__cursor.execute(f"SELECT 1 FROM BlackCarPassenger WHERE CarName='{CarName}' AND Month={month} AND PlayerName='{playerName}'").fetchone() == None):
                pass
            else:
                print("You Have Joined")
                return False
            
            # 加入順序+1
            joinNum = self.__cursor.execute(f"SELECT MAX(JoinNumber) FROM BlackCarPassenger WHERE CarName='{CarName}' AND Month={month}").fetchone()["MAX(JoinNumber)"]
            if joinNum == None:
                joinNum = 1
            else:
                joinNum += 1
            
            self.__cursor.execute(f"INSERT INTO BlackCarPassenger (CarName, JoinNumber, PlayerName, Month, DiscordID) VALUES ('{CarName}', {joinNum}, '{playerName}', {month}, '{discordID}')")
            self.__conn.commit()
            return True
        
        except Exception as e:
            print(e)
            return False
        
    def _Test(self, x):
        self.__cursor.execute(x)
        rows = self.__cursor.fetchall()
        return rows



def FormattedDate(month: int, day: int, year: int=None) -> str:
    formattedDate = ''
    currentDate = datetime.now()
    
    if year == None:
        formattedDate = '{}-{:02d}-{:02d}'.format(currentDate.year, month, day)
    if year != None:
        # TODO
        formattedDate = '{}-{:02d}-{:02d}'.format(currentDate.year, month, day)
    return formattedDate


# test -----------------------------------------------------------------

# x = Connecter()
# x.CreateCar("懷特車", 4, 26, "Whiter5678", "12345678973748763", 59)
# x.CreateCar("怪特車", 4, 22, "Coolcat5678", "12342338972748763", 51)
# x.CreateCar("A車", 4, 21, "Pizza81324", "12345671172748763", 52)
# x.CreateCar("B車", 4, 20, "長恨晚歌", "1234562748763", 60)
# x.CreateCar("C車", 4, 27, "NSPEED", "123454748763", 19)
# x.JoinCar("懷特車", 4, "苦痛狗", "1miss123nnnggggrrrr")

# print(x._Test('SELECT * FROM BlackCar'))