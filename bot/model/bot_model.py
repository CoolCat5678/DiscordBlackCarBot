from .car_model import Car
# from backend.car_manager import CarManager
from typing import Generator

class BotModel:
  __instance = None

  def __init__(self):
    # self.manager = CarManager()
    pass

  @staticmethod
  def get_instance():
    if BotModel.__instance == None:
      BotModel.__instance = BotModel()
    return BotModel.__instance
  
   ## wait for manager ready
  def search_car_month(self, month: int, load_limit: int = 3) -> Generator[list, None, None]:
    car_list = [f"car{i}" for i in range(10)]
    return self.car_lazy_loader(target=car_list, load_limit=load_limit)

  # def search_car_name(self, car_name: str, month: int) -> list:
  #   return conn.search(CarName=car_name, Month=month)
  
  # def create_car(self, car_name: str, month: int, day: int, player_name: str, discord_id = str, fight_time: int=60) -> bool:
  #   return conn.create_car(car_name, month, day, player_name, discord_id, fight_time)
  
  # def join_car(self, car_name: str, month: int, player_name: str, discord_id = str) -> bool:
  #   return conn.join_car(car_name, month, player_name, discord_id)
  
  def car_lazy_loader(self, target: list,load_limit: int = 3) -> Generator[list, None, None]:
    temp = []
    try: 
      for carData in target:
        temp.append(carData)
        # temp.append(Car(carData))
        if len(temp) == load_limit:
          yield temp
          temp.clear()
      yield temp
    except StopIteration:
      return None

bot_model = BotModel.get_instance()