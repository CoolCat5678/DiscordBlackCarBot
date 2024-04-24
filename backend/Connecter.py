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
        
        # self.cars = {}
        # cars = self.__cursor.execute('SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName AND M.Month=D.Month').fetchall()
        # for car in cars:
        #     if car['CarName'] not in self.cars:
        #         self.cars[car['CarName']] = Car(self.__conn, car)
        #     else:
        #         self.cars[car['CarName']].join_passenger(car)
        
    def search_car_month(self, month: int) -> list:
        """
        This function search car in month.

        return:
            list
        """
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName AND M.Month=D.Month WHERE M.Month={month}")    
        rows = self.__cursor.fetchall()
        return rows
            
    def search_car_name(self, car_name: str, month: int) -> list:
        """
        This function search car with name.
        
        return:
            list
        """
        self.__cursor.execute(f"SELECT * FROM BlackCar M LEFT JOIN BlackCarPassenger D ON M.CarName=D.CarName AND M.Month=D.Month WHERE M.CarName='{car_name}' AND M.Month={month}")
        rows = self.__cursor.fetchall()
        return rows

    def create_car(self, car_name: str, month: int, day: int, player_name: str, discord_id = str, fight_time: int=60) -> bool:
        """
        This function Create a new car.

        return:
            bool: success=true
        """
        try:
            date = formatted_date(month, day)
            self.__cursor.execute(f"INSERT INTO BlackCar (CarName, Month, PlannedDate, FightTime, DiscordID) VALUES ('{car_name}', {month}, '{date}', {fight_time}, {discord_id})")
            self.__conn.commit()
            self.join_car(car_name, month, player_name, discord_id)
            return True
        
        except Exception as e:
            print(e)
            return False

    def join_car(self, car_name: str, month: int, player_name: str , discord_id = str):  
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
            join_num = self.__cursor.execute(f"SELECT MAX(JoinNumber) FROM BlackCarPassenger WHERE CarName='{car_name}' AND Month={month}").fetchone()["MAX(JoinNumber)"]
            if join_num == None:
                join_num = 1
            else:
                join_num += 1
            
            self.__cursor.execute(f"INSERT INTO BlackCarPassenger (CarName, JoinNumber, PlayerName, Month, DiscordID) VALUES ('{car_name}', {join_num}, '{player_name}', {month}, '{discord_id}')")
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
    x = Connecter()
# x.CreateCar("懷特車", 4, 26, "Whiter5678", "12345678973748763", 59)
# x.CreateCar("怪特車", 4, 22, "Coolcat5678", "12342338972748763", 51)
# x.CreateCar("A車", 4, 21, "Pizza81324", "12345671172748763", 52)
# x.CreateCar("B車", 4, 20, "長恨晚歌", "1234562748763", 60)
# x.CreateCar("C車", 4, 27, "NSPEED", "123454748763", 19)
# x.JoinCar("懷特車", 4, "苦痛狗", "1miss123nnnggggrrrr")
    # print(x._Test('SELECT * FROM BlackCar'))

if __name__ == '__main__':
    main()