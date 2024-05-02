from discord.ui import Modal, TextInput, Select
from discord import Interaction, SelectOption
from discord.interactions import ClientT

NAME_INPUT = TextInput(label="角色名稱", placeholder="輸入你的名稱")
LEVEL_INPUT = TextInput(label="角色等級", placeholder="輸入你的等級")
CAR_INPUT = TextInput(label="選擇車次", placeholder="輸入想搭乘的車次編號")
DURATION_INPUT = TextInput(label="預計時間", placeholder="預計要打多久")
DATE_INPUT = TextInput(label="發車日期", placeholder="什麼時候打")

class JoinCarModal(Modal):
  def __init__(self, title: str = "填寫乘車資訊"):
    super().__init__(title=title)
    self.name_input = NAME_INPUT
    self.level_input = LEVEL_INPUT
    self.car_input = CAR_INPUT
    self.add_item(self.car_input)
    self.add_item(self.name_input)
    self.add_item(self.level_input)

  async def show_modal(self, interaction: Interaction):
    try:
      await interaction.response.send_modal(self)
    except Exception as e:
      print(e)

  async def on_submit(self, interaction: Interaction[ClientT]) -> None:
    await interaction.response.defer(ephemeral=True)
    try:
      await interaction.message.edit(content=f"{self.level_input.value} / {self.name_input.value} 登記成功", view=None, embed=None)
    except Exception as e:
      print(e)

class CreateCarModal(JoinCarModal):
  def __init__(self):
    super().__init__(title="填寫發車資訊")
    self.remove_item(self.car_input)
    self.duration_input = DURATION_INPUT
    self.date_input = DATE_INPUT
    self.add_item(self.duration_input)
    self.add_item(self.date_input)
    
  async def on_submit(self, interaction: Interaction[ClientT]) -> None:
    await interaction.response.defer(ephemeral=True)
    try:
      await interaction.message.edit(content=f"{self.level_input.value} / {self.name_input.value} 登記成功", view=None, embed=None)
    except Exception as e:
      print(e)