from discord.ui import Modal, TextInput, Select
from discord import Interaction, SelectOption
from discord.interactions import ClientT

class JoinCarModal(Modal):
  def __init__(self, title: str = "填寫乘車資訊"):
    super().__init__(title=title)
    self.name_input = TextInput(label="角色名稱", placeholder="輸入你的名稱")
    self.level_input = TextInput(label="角色等級", placeholder="輸入你的等級")
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
    self.month_select = Select(options=[self.THIS_MONTH, self.NEXT_MONTH], placeholder="選擇月份")
    self.duration_input = TextInput(label="預計時間", placeholder="預計要打多久")
    self.date_input = TextInput(label="發車日期", placeholder="什麼時候打")
    self.add_item(self.duration_input)
    self.add_item(self.date_input)
    
  async def on_submit(self, interaction: Interaction[ClientT]) -> None:
    await interaction.response.defer(ephemeral=True)
    try:
      await interaction.message.edit(content=f"{self.level_input.value} / {self.name_input.value} 登記成功", view=None, embed=None)
    except Exception as e:
      print(e)