from .car_model import Car, CarList, Passenger
from backend.car_manager import CarManager
from typing import Generator

class BotModel:
  __instance = None

  def __init__(self):
    self.manager = CarManager()
    pass

  @staticmethod
  def get_instance():
    if BotModel.__instance == None:
      BotModel.__instance = BotModel()
    return BotModel.__instance
  
   ## wait for manager ready
  def search_car_month(self, month: int, load_limit: int = 3) -> Generator[list, None, None]:
    car_list = self.manager.get_car_list(Month=4)
    return self.car_lazy_loader(target=car_list, load_limit=load_limit)
  
  def search_car_name(self, car_name: str) -> list:
    car_list = self.manager.get_car_list(CarName=car_name)
    return self.car_lazy_loader(target=car_list)
  
  # def join_car(self, car_name: str, month: int, player_name: str, discord_id: str) -> bool:
  #   return True

  # def search_car_name(self, car_name: str, month: int) -> list:
  #   return conn.search(CarName=car_name, Month=month)
  
  # def create_car(self, car_name: str, month: int, day: int, player_name: str, discord_id = str, fight_time: int=60) -> bool:
  #   return True
  
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

bot_model = BotModel.get_instance()