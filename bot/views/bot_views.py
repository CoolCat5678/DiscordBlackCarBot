from enum import Enum
from discord import Embed, ButtonStyle, Interaction
from discord.ui import View, button
from discord.ext import commands
from datetime import datetime
from abc import ABCMeta, abstractmethod
from model.bot_model import BotModel

## for development fast reload, should be enhanced in the future
from importlib import reload
from pathlib import Path
import sys
sys.path.insert(0, Path(__file__).parent.as_posix())
import bot_modal as modals
##

import common as cm

now: datetime = datetime.now()

class Bot_views_base(View, metaclass=ABCMeta):
  def __init__(self, title: str, color: int):
    super().__init__()
    self.embed = Embed(title=title, description='', color=color)
    self.init_layout(self.embed)
  
  @abstractmethod
  def init_layout(self, embed: Embed):
    return NotImplementedError
  
  def add_new_line(self):
    self.embed.add_field(name="", value="\n", inline=False)
  
  async def show_view(self, ctx: commands.Context):
    self.embed.clear_fields()
    self.init_layout(self.embed)
    self.sync_time(self.embed)
    await ctx.send(embed=self.embed, view=self)

  def sync_time(self, embed: Embed):
    embed.set_footer(text=f"最後更新時間 {now.strftime('%m-%d %H:%M')}", icon_url=cm.thumbnail_url)
  
class Overview_view(Bot_views_base):
  __instance = None

  @staticmethod
  def get_instance():
    if Overview_view.__instance == None:
      Overview_view.__instance = Overview_view()
    return Overview_view.__instance

  def __init__(self):
    super().__init__(title = "黑魔法師列隊系統", color= 0xff5a5a)
    pass

  def init_layout(self, embed: Embed):
    embed.set_thumbnail(url=cm.thumbnail_url)
    embed.add_field(name="現有車數", value="`1919`", inline=False)
    embed.add_field(name="總人數", value="`810`", inline=False)
    embed.add_field(name="還有空位的車數", value="`114514`", inline=False)
    embed.add_field(name="下次發車日期", value="`48763`", inline=False)
    super().add_new_line()

  @button(label="時刻表", style=ButtonStyle.grey, custom_id="search_car")
  async def delete_car(self, interaction: Interaction, _):
    await switch_view(Bot_Layouts.DETAIL_LIST, interaction)

class Detail_list_view(Bot_views_base):
  __instance = None
  @staticmethod
  def get_instance():
    if Detail_list_view.__instance == None:
      Detail_list_view.__instance = Detail_list_view()
    return Detail_list_view.__instance

  def __init__(self):
    
    super().__init__(title = "發車時刻表", color= 0xa5a5ff)
    pass

  def init_layout(self, embed: Embed):
    self.render_detail_list(embed)
  
  def render_detail_list(self, embed: Embed):
    bot_model = BotModel()
    current_month = datetime.now().month
    car_list = bot_model.search_car_month(current_month)
    for car in car_list:
      field_value = [f"車長: `{car.CarName}`", f"目前人數: `{len(car.passenger)}`", "\n"
                    ,f"預計: `{car.FightTime}`分鐘"]
      embed.add_field(name=f"{car_list.index(car) + 1} 車 / `{car.PlannedDate}`", value="  ".join(field_value), inline=False)
    pass

  @button(label="登記上車", style=ButtonStyle.primary, custom_id="search_car")
  async def join_car(self, interaction: Interaction, _):
    try:
      modal = modals.JoinCarModal()
      await modal.show_modal(interaction)
    except Exception as e:
      print(e)
      pass

class Bot_Layouts(Enum):
  reload(modals)
  OVERVIEW = Overview_view.get_instance();
  DETAIL_LIST = Detail_list_view.get_instance();

async def switch_view(layout: Bot_Layouts, interaction: Interaction):
  await interaction.response.defer(ephemeral=True)
  try:
    await interaction.message.edit(view=layout.value, embed=layout.value.embed)
  except Exception as e:
    print(e)
    pass