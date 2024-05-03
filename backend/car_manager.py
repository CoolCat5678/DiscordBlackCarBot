import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from bot.model.car_model import CarList, Car, Passenger
from Connecter import conn

class CarManager:
    def __init__(self) -> None: 
        pass
    
    def delete_car(self, car: Car):
        pass
    
    def update_car(self, car: Car):
        conn.insert_car(
                CarName=car.CarName,
                Year=car.Year,
                Month=car.Month,
                Finished=car.Finished,
                PlannedDate=car.PlannedDate,
                DiscordID=car.DiscordID,
                FightTime=car.FightTime
            )
        
        for passenger in car:
            conn.insert_passenger(
                CarName=car.CarName,
                Year=car.Year,
                Month=car.Month,
                QueueNumber=passenger.QueueNumber,
                PlayerName=passenger.PlayerName,
                DiscordID=passenger.DiscordID
            )
            
    def get_car_list(self, CarName=None, Year=None, Month=None, Finished=None, PlannedDate=None, DiscordID=None, FightTime=None) -> CarList:
        paras = {}
        if CarName is not None:
            paras['CarName'] = CarName
        if Year is not None:
            paras['Year'] = Year
        if Month is not None:
            paras['Month'] = Month
        if Finished is not None:
            paras['Finished'] = Finished
        if PlannedDate is not None:
            paras['PlannedDate'] = PlannedDate
        if DiscordID is not None:
            paras['DiscordID'] = DiscordID
        if FightTime is not None:
            paras['FightTime'] = FightTime
        data = conn.search_car(**paras)
        
        car_list = CarList()
        car_list._create_list(data)
        
        return car_list
    
def main():
    cm = CarManager()
    m4 = cm.get_car_list()['ACar']
    cm.update_car(m4)
    
if __name__=='__main__':
    main()