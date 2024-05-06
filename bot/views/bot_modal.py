from discord.ui import Modal, TextInput, Select
from discord import Interaction, SelectOption
from discord.interactions import ClientT
from common import Utils
from bot.model.bot_model import BotModel

NAME_INPUT = TextInput(label="角色名稱", placeholder="輸入你的名稱")
LEVEL_INPUT = TextInput(label="角色等級", placeholder="輸入你的等級")
CAR_NAME = TextInput(label="想上的車", placeholder="輸入想搭乘的車名")
DURATION_INPUT = TextInput(label="預計時間", placeholder="預計要打多久")
DATE_INPUT = TextInput(label="發車日期", placeholder="什麼時候打 (年/月)")

def get_formated_date(date: str):
  year, month = date.strip().split("/")
  return [year, month]

class JoinCarModal(Modal):
  def __init__(self, title: str = "填寫乘車資訊"):
    super().__init__(title=title)
    self.name_input = NAME_INPUT
    self.level_input = LEVEL_INPUT
    self.car_input = CAR_NAME
    self.date_input = DATE_INPUT
    self.add_item(self.car_input)
    self.add_item(self.date_input)
    self.add_item(self.name_input)
    self.add_item(self.level_input)
    self.model: BotModel = BotModel.get_instance()

  async def show_modal(self, interaction: Interaction):
    try:
      await interaction.response.send_modal(self)
    except Exception as e:
      print(e)

  async def on_submit(self, interaction: Interaction[ClientT]) -> None:
    await interaction.response.defer(ephemeral=True)
    try:
      user = await Utils.get_user(interaction=interaction);
      # year, month = get_formated_date(self.date_input.value);
      # car_list = self.model.join_car(car_name=self.car_input.value, month=int(month), player_name=self.name_input.value, discord_id=user)
      await interaction.message.edit(content=f"{user.mention} 登記成功", view=None, embed=None)
    except Exception as e:
      print(e)

class CreateCarModal(JoinCarModal):
  def __init__(self):
    super().__init__(title="填寫發車資訊")
    self.remove_item(self.car_input)
    self.duration_input = DURATION_INPUT
    # self.date_input = DATE_INPUT
    self.add_item(self.duration_input)
    # self.add_item(self.date_input)
    
  async def on_submit(self, interaction: Interaction[ClientT]) -> None:
    await interaction.response.defer(ephemeral=True)
    try:
      user_id = interaction.user.id;
      await interaction.message.edit(content=f"{self.level_input.value} / {self.name_input.value} 登記成功", view=None, embed=None)
    except Exception as e:
      print(e)