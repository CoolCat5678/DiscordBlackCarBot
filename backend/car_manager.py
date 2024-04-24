from car_model import CarList, Car, Passenger
from connecter import conn

class CarManager:
    def __init__(self) -> None:
        self.cars = None
        pass
    
    def delete_car(self, car: Car):
        pass
     
    def update_car(self, car: Car):
        pass
    
    def search_car(self, month) -> CarList:
        data = conn.search_car_month(month)
        self.cars = CarList(data)

    
def main():
    cm = CarManager()
    cm.search_car(4)
    
if __name__=='__main__':
    main()