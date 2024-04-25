from car_model import CarList, Car, Passenger
from connecter import conn

class CarManager:
    def __init__(self) -> None:
        self.car_list = CarList()
        pass
    
    def delete_car(self, car: Car):
        pass
    
    def update_car(self, car: Car):
        pass
    
    def delete_passenger(self, car: Car, passenger: Passenger):
        pass
    
    def add_passenger(self, car: Car, passenger: Passenger):
        pass
    
    def search_car(self, month) -> CarList:
        data = conn.search_car_month(month)
        self.car_list._create_list(data)
    
def main():
    cm = CarManager()
    cm.search_car(4)
    print(cm.car_list)

    
if __name__=='__main__':
    main()