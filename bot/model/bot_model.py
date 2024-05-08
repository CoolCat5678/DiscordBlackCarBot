from bot.model.car_model import Car, CarList, Passenger
from backend.car_manager import car_manager
from typing import Generator



class BotModel:
  def __init__(self):
    pass
  
  def search_car_month(self):
    car_list = car_manager.get_car_list(Month=4)
    return car_list
  
  def get_generator(self, car_name: str) -> list:
    car_list = car_manager.get_car_list(CarName=car_name)
    return self.car_lazy_loader(target=car_list)
  
  def car_lazy_loader(self, target: CarList,load_limit: int = 3) -> Generator[list, None, None]:
    temp = []
    try: 
      for carData in target:
        temp.append(carData)
        if len(temp) == load_limit:
          yield temp
          temp.clear()
      yield temp
    except StopIteration:
      return None
    
  def new_car(self, car_name, year, month, finished, planned_date, discord_id, fight_time, player_name):
    new_car = Car(car_name=car_name, year=year, month=month, finished=finished, planned_date=planned_date, discord_id=discord_id, fight_time=fight_time)
    new_passenger = Passenger(player_name=player_name, discord_id=discord_id)
    new_car.join_passenger(new_passenger)
    car_manager.update_car(new_car)
  
  def join_car(self, car_name, year, month, discord_id, player_name):
    new_passenger = Passenger(player_name=player_name, discord_id=discord_id)
  
