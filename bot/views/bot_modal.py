from discord.ui import Modal, TextInput
from discord import Interaction
from discord.interactions import ClientT

class JoinCarModal(Modal):
  def __init__(self):
    super().__init__(title="填寫乘車資訊")
    self.name_input = TextInput(label="Name", placeholder="enter your name")
    self.level_input = TextInput(label="Level", placeholder="enter your level")
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
