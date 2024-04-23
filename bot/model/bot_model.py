from .car_model import Car
from backend.Connecter import conn

class BotModel:
  __instance = None

  def __init__(self):
    pass

  @staticmethod
  def get_instance():
    if BotModel.__instance == None:
      BotModel.__instance = BotModel()
    return BotModel.__instance
  
  def search_car_month(self, month: int) -> list[Car]:
    car_list = conn.search_car_month(month)
    return list(map(lambda car: Car(car), car_list))

  def search_car_name(self, car_name: str, month: int) -> list:
    return conn.search_car_name(car_name, month)
  
  def create_car(self, car_name: str, month: int, day: int, player_name: str, discord_id = str, fight_time: int=60) -> bool:
    return conn.create_car(car_name, month, day, player_name, discord_id, fight_time)
  
  def join_car(self, car_name: str, month: int, player_name: str, discord_id = str) -> bool:
    return conn.join_car(car_name, month, player_name, discord_id)

bot_model = BotModel.get_instance()