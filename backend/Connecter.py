import sqlite3
from datetime import datetime


class Connecter:
    __conn = sqlite3.Connection
    __cursor = sqlite3.Cursor
    def __init__(self, database: str="CoolcatDB"):
        """
        Constructor
        """
        __dbPath = f'./database/{database}.db'
        self.__conn = sqlite3.connect(__dbPath)
        self.__cursor = self.__conn.cursor() 
        
    # region function
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
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName WHERE M.CarName='{carName}' AND M.Month={month}")
        rows = self.__cursor.fetchall()
        return rows

    def CreateCar(self, CarName: str, month: int, day: int, playerName: str, fightTime: int=60) -> bool:
        """
        This function Create a new car.

        return:
            bool: success=true
        """
        try:
            date = FormattedDate(month, day)
            self.__cursor.execute(f"INSERT INTO BlackCar (CarName, Month, PlannedDate, FightTime) VALUES ('{CarName}', {month}, '{date}', {fightTime})")
            self.__conn.commit()
            self.JoinCar(CarName, playerName, month)
            return True
        
        except Exception as e:
            print(e)
            return False

    def JoinCar(self, CarName: str, playerName: str ,month: int):  
        """
        This function calculates the area of a rectangle.

        Parameters:
            length  (float): The length of the rectangle.
            width   (float): The width of the rectangle.

        Returns:
            bool: success=true
        """
        try:
            joinNum = self.__cursor.execute(f"SELECT MAX(JoinNumber) FROM BlackCarPassenger WHERE CarName='{CarName}' AND Month={month}").fetchone()[0]
            print(type(joinNum))
            if joinNum == None:
                joinNum = 1
            else:
                joinNum += 1
            
            self.__cursor.execute(f"INSERT INTO BlackCarPassenger (CarName, JoinNumber, PlayerName, Month) VALUES ('{CarName}', {joinNum}, '{playerName}', {month})")
            self.__conn.commit()
            return True
        
        except Exception as e:
            print(e)
            return False
        
    # def __Test(self, x):
    #     self.__cursor.execute(x)
    #     rows = self.__cursor.fetchone()
    #     return rows
    # endregion


# ----
def FormattedDate(month: int, day: int, year: int=None) -> str:
    formattedDate = ''
    currentDate = datetime.now()
    
    if year == None:
        formattedDate = '{}-{:02d}-{:02d}'.format(currentDate.year, month, day)
    if year != None:
        # TODO
        formattedDate = '{}-{:02d}-{:02d}'.format(currentDate.year, month, day)
    return formattedDate

# x = Connecter('CoolcatDB')
# x.CreateCar("A", 4, 4, "coolcat")
# x.JoinCar("A", "sadCat", 3)
# print(x.SearchCarMonth(4))
# print(x.SearchCarName("A", 4))
