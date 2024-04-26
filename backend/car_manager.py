import sys
sys.path.append('./')
from bot.model.car_model import CarList, Car, Passenger
from connecter import conn

class CarManager:
    def __init__(self) -> None:
        self.car_list = CarList()
    
    def delete_car(self, car: Car):
        pass
    
    def update_car(self, car: Car):
        db_data = conn.search_car(CarName=car.CarName, Month=car.Month)
        
        db_car = Car(db_data[0])
        for db_passenger in db_data:
            db_car.join_passenger(Passenger(db_passenger))
            
        attr1 = vars(db_car)
        for attr in attr1:
            print(getattr(db_car, attr) == getattr(car, attr))
            
    def search_car(self, month) -> CarList:
        data = conn.search_car(Month=month)
        self.car_list._create_list(data)
    
def main():
    cm = CarManager()
    cm.search_car(4)
    print(cm.car_list['ACar'])
    
if __name__=='__main__':
    main()