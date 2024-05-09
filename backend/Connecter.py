import sqlite3
from datetime import datetime
from pathlib import Path

# 更改cursor return to dict
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Connecter:
    __instance = None

    @staticmethod
    def get_instance():
        if Connecter.__instance == None:
            Connecter.__instance = Connecter()
        return Connecter.__instance

    def __init__(self, database: str="CoolcatDB"):
        """
        Constructor
        """
        __dbPath = Path(__file__).parents[1].joinpath('database', f'{database}.db')
        self.__conn = sqlite3.connect(__dbPath)
        self.__conn.row_factory = dict_factory
        self.__cursor = self.__conn.cursor()
                
    def search_car(self, **kwargs) -> list:
        """
        This function search car
        return:
            list
        """
        where_str = "1=1"
        for key in kwargs.keys():
            where_str += f" AND M.{key}=?"
        value_input = tuple(kwargs.values())
        
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName AND M.Month=D.Month WHERE {where_str}", value_input)    
        rows = self.__cursor.fetchall()
        return rows

    def search_passenger(self, **kwargs) -> list:
        """
        This function search passenger
        return:
            list
        """
        where_str = "1=1"
        for key in kwargs.keys():
            where_str += f" AND D.{key}=?"
        value_input = tuple(kwargs.values())
            
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName AND M.Month=D.Month WHERE {where_str}", value_input)    
        rows = self.__cursor.fetchall()
        return rows
    
    def insert_car(self, **kwargs) -> bool:
        """
        This function Create a new car.
        return:
            bool: success=true
        """
        try:
            columns = f"({' ,'.join(kwargs.keys())})"
            value_input = tuple(kwargs.values())
            placeholders = ', '.join(['?' for _ in kwargs])
            
            self.__cursor.execute(f"INSERT INTO BlackCar {columns} VALUES ({placeholders})", value_input)
            self.__conn.commit()
            print('asd')
            return True
        
        except Exception as e:
            print(e)
            return False
        
    def insert_passenger(self, **kwargs) -> bool:
        """
        This function Create a new car.
        return:
            bool: success=true
        """
        try:
            columns = f"({' ,'.join(kwargs.keys())})"
            values = str(tuple(kwargs.values()))
            
            self.__cursor.execute(f"INSERT INTO BlackCarPassenger {columns} VALUES {values}")
            self.__conn.commit()
            return True
        
        except Exception as e:
            print(e)
            return False

    def join_car(self, car_name: str, month: int, year : int, player_name: str , discord_id = str):  
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
            if(self.__cursor.execute(f"SELECT 1 FROM BlackCar WHERE CarName='{car_name}' AND Month={month} AND Finished='N'").fetchone()):
                pass
            else:
                print("Car Not Found")
                return False
            
            # 檢查是否加入過
            if(self.__cursor.execute(f"SELECT 1 FROM BlackCarPassenger WHERE CarName='{car_name}' AND Month={month} AND PlayerName='{player_name}'").fetchone() == None):
                pass
            else:
                print("You Have Joined")
                return False
            
            # 加入順序+1
            join_num = self.__cursor.execute(f"SELECT MAX(QueueNumber) FROM BlackCarPassenger WHERE CarName='{car_name}' AND Month={month}").fetchone()["MAX(QueueNumber)"]
            if join_num == None:
                join_num = 1
            else:
                join_num += 1
            
            self.__cursor.execute(f"INSERT INTO BlackCarPassenger (CarName, QueueNumber, PlayerName, Month, DiscordID) VALUES ('{car_name}', {join_num}, '{player_name}', {month}, '{discord_id}')")
            self.__conn.commit()
            return True
        
        except Exception as e:
            print(e)
            return False
        
    def _Test(self, x):
        self.__cursor.execute(x)
        rows = self.__cursor.fetchall()
        return rows


conn = Connecter.get_instance()

def formatted_date(month: int, day: int, year: int=None) -> str:
    formatted_date = ''
    current_date = datetime.now()
    
    if year == None:
        formatted_date = '{}-{:02d}-{:02d}'.format(current_date.year, month, day)
    if year != None:
        # TODO
        formatted_date = '{}-{:02d}-{:02d}'.format(current_date.year, month, day)
    return formatted_date


# test -----------------------------------------------------------------
def main():
    print(conn.insert_car(CarName="ACar", Year=2024, Month=4, PlannedDate='2024-04-29', DiscordID='20', FightTime=16))
    pass

if __name__ == '__main__':
    main()
    
    
    