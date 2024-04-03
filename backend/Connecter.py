import sqlite3
from datetime import datetime

class Connecter:
    __conn=any
    __cursor=any
    
    def __init__(self, database: str="CoolcatDB"):
        """
        Constructor.

        Parameters:
            database (str) deafault:CoolcatDB
        """
        __dbPath = f'./database/{database}.db'
        self.__conn = sqlite3.connect(__dbPath)
        self.__cursor = self.__conn.cursor() 


    # region function
    def SearchCarMonth(self, month: int=0):
        """
        This function search car in month.

        Parameters:
            month (int) range between 1 to 12
        """
        formattedDate = ''
        currentDate = datetime.now()
        
        if month > 0 and month < 13:
            formattedDate = '{}-{:02d}'.format(currentDate.year, month)
        else:
            formattedDate = currentDate.strftime('%Y-%m')
        
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName WHERE M.PlannedDate LIKE '{formattedDate}%'")    
        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)
            
            
    def SearchCarName(self, carName: str):
        """
        This function search car with Name.

        Parameters:
            carName (str)
        """
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName WHERE M.CarName='{carName}'")    
        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)
                
                
    def CreateCar(self, CarName: str, month: int, day: int):
        """
        This function Create a new car.

        Parameters:
            month (int) range between 1 to 12
            day   (int) range between 1 to 31
        """
        PlannedDate = ''
        currentDate = datetime.now()
        
        if 0 < month < 13:
            PlannedDate = '{}-{:02d}-{:02d}'.format(currentDate.year, month, day)
        else:
            PlannedDate = currentDate.strftime('%Y-%m-%d')
        print(PlannedDate)
        self.__cursor.execute(f"INSERT INTO BlackCar (CarName, Month, PlannedDate) VALUES ('{CarName}', {month}, '{PlannedDate}')")
        self.__conn.commit()

    # def JoinCar(self):  
    #     """
    #     This function calculates the area of a rectangle.

    #     Parameters:
    #         length (float): The length of the rectangle.
    #         width (float): The width of the rectangle.

    #     Returns:
    #     """
    #     self.__cursor.execute("INSERT INTO BlackCarPassenger (CarName, JoinNumber, PlayerName) VALUES ('CarA', 1, 'Player1')")
    #     self.__conn.commit()
    # endregion


x = Connecter('CoolcatDB')
# x.CreateCar('CoolCar', 5, 15)
# x.SearchCarMonth(5)