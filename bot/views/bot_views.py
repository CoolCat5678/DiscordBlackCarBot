from enum import Enum
from discord import Embed, ButtonStyle, Interaction, Color
from discord.ui import View, button, Button
from discord.ext import commands
from datetime import datetime
from abc import ABCMeta, abstractmethod
from model.bot_model import BotModel
from bot.model.car_model import CarList, Car, Passenger

from importlib import reload
import views.bot_modal as modals
from common import THUMBNAIL_URL

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
    embed.set_footer(text=f"最後更新時間 {now.strftime('%m-%d %H:%M')}", icon_url=THUMBNAIL_URL)

  async def rerender(self, interaction: Interaction):
    try:
      await interaction.response.edit_message(embed=self.embed, view=self)
    except Exception as e:
      print(e)
  
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
    embed.set_thumbnail(url=THUMBNAIL_URL)
    embed.add_field(name="現有車數", value="`1919`", inline=False)
    embed.add_field(name="總人數", value="`810`", inline=False)
    embed.add_field(name="還有空位的車數", value="`114514`", inline=False)
    embed.add_field(name="下次發車日期", value="`48763`", inline=False)
    super().add_new_line()

  @button(label="測試", style=ButtonStyle.primary, custom_id="test")
  async def form_add_p(self, interaction: Interaction, _):
    try:
      bot_model = BotModel()
      embeds = creat_embeds(bot_model.search_car_month())
      view = ViewClass(embeds=embeds)
      await interaction.response.send_message(embed=embeds[view.current_page]['embed'], view=view)
    except Exception as e:
      print(e)
      pass
    
  @button(label="自己開車", style=ButtonStyle.primary, custom_id="create_car")
  async def create_car(self, interaction: Interaction, _):
    try:
      modal = modals.CreateCarModal()
      car = Car(car_name="test_car", month=4, finished="Y", year=123, planned_date='2024-04-10', discord_id=123, fight_time=4)
      await modal.show_modal(interaction, car)
    except Exception as e:
      print(e)
      pass

  @button(label="時刻表", style=ButtonStyle.grey, custom_id="search_car")
  async def search_car(self, interaction: Interaction, _):
    await switch_view(Bot_Layouts.DETAIL_LIST, interaction)

class Detail_list_view(Bot_views_base):
  __instance = None
  @staticmethod
  def get_instance():
    if Detail_list_view.__instance == None:
      Detail_list_view.__instance = Detail_list_view()
    return Detail_list_view.__instance

  car_list = None
  bot_model = BotModel()

  def __init__(self):
    super().__init__(title = "發車時刻表", color= 0xa5a5ff)
    pass

  def init_layout(self, embed: Embed):
    current_month = datetime.now().month
    self.car_list = self.bot_model.search_car_month()
    self.render_detail_list(embed)
  
  def render_detail_list(self, embed: Embed):
    try:
      car_list = next(self.car_list)
      embed.clear_fields()
      for car in car_list:
        ## wait for manager ready
        field_value = [f"目前人數: `{len(car)}`", "\n"
                      ,f"預計: `{car.FightTime}`分鐘"]
        embed.add_field(name=f"{car.CarName} 車 / `{car.PlannedDate}`", value="".join(field_value), inline=False)
      return True
    except Exception as e:
      print(e)
      return False

  @button(label="登記上車", style=ButtonStyle.primary, custom_id="search_car")
  async def join_car(self, interaction: Interaction, _):
    try:
      modal = modals.JoinCarModal()
      car = Car(car_name="test_car", month=4, finished="Y", year=123, planned_date='2024-04-10', discord_id=123, fight_time=4)
      await modal.show_modal(interaction, car)
    except Exception as e:
      print(e)
      pass

  @button(label="下一頁", style=ButtonStyle.grey, custom_id="next_page")
  async def next_page(self, interaction: Interaction, button: button):
    try:
      button.disabled = not self.render_detail_list(self.embed)
      await self.rerender(interaction)
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
  
#region test embedsview
def creat_embeds(list):
  embeds = []
  for i in list:
    embed = Embed(
        title=i.CarName,
        description=f"{i}",
        color=Color.blue(),
    )
    car_dic = {
      'embed' : embed,
      'CarName' : i.CarName,
      'Year' : i.Year,
      'Month' : i.Month
    }
    embeds.append(car_dic)
  return embeds

class ViewClass(View):
  def __init__(self, embeds, timeout: float or None = 180):
      super().__init__(timeout=timeout)
      self.embeds = embeds
      self.current_page = 0

  async def show_current_page(self, interaction: Interaction):
    try:
      await interaction.response.edit_message(embed=self.embeds[self.current_page]['embed'], view=self)
    except Exception as e:
      print(e)


  @button(label="上一頁", style=ButtonStyle.gray)
  async def go_previous(self, interaction: Interaction, button: Button):
      if self.current_page > 0:
          self.current_page -= 1
          await self.show_current_page(interaction)
      else:
          await self.show_current_page(interaction)
          
  @button(label="測試登記上車", style=ButtonStyle.primary, custom_id="search_car")
  async def join_car(self, interaction: Interaction, _):
    try:
      modal = modals.JoinCarModal()
      car = Car(car_name="test_car", month=4, finished="Y", year=123, planned_date='2024-04-10', discord_id=123, fight_time=4)
      await modal.show_modal(interaction, car)
    except Exception as e:
      print(e)
      pass

  @button(label="加入這台車", style=ButtonStyle.gray)
  async def join(self, interaction: Interaction, button: Button):
      try:
        list = Embed(
          title=self.embeds[self.current_page]['embed'].title,
          description=f'''
          取得key帶入表單
          {self.embeds[self.current_page]['CarName']}
          {self.embeds[self.current_page]['Year']}
          {self.embeds[self.current_page]['Month']}
          ''',
          color=Color.blue()  # 設定 Embed 的顏色
        )
        await interaction.response.send_message(embed=list)
      except Exception as e:
        print(e)


  @button(label="下一頁", style=ButtonStyle.gray)
  async def go_next(self, interaction: Interaction, button: Button):
      if self.current_page < len(self.embeds) - 1:
          self.current_page += 1
          await self.show_current_page(interaction)
      else:
          await self.show_current_page(interaction)
# endregion