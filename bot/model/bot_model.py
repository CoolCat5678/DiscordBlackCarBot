from pathlib import Path
import sys
sys.path.insert(0, Path(__file__).parents[2].as_posix())
from backend.Connecter import Connecter

class BotModel:
  def __init__(self):
    self.connecter = Connecter()
    pass

  def search_car_month(self, month: int) -> list:
    return self.connecter.search_car_month(month)
  
  def search_car_name(self, car_name: str, month: int) -> list:
    return self.connecter.search_car_name(car_name, month)
  
  def create_car(self, car_name: str, month: int, day: int, player_name: str, discord_id = str, fight_time: int=60) -> bool:
    return self.connecter.create_car(car_name, month, day, player_name, discord_id, fight_time)
  
  def join_car(self, car_name: str, month: int, player_name: str, discord_id = str) -> bool:
    return self.connecter.join_car(car_name, month, player_name, discord_id)
