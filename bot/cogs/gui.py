from discord import Embed, ButtonStyle, Interaction
from discord.ext import commands
from discord.ui import button, View
from datetime import datetime

from pathlib import Path
import sys
sys.path.insert(0, Path(__file__).parents[1].as_posix())
from model.bot_model import BotModel
import common as cm

class Overview_views(View):
  def __init__(self):
    super().__init__()
    self.embed = Embed(title=f"{datetime.now().month}月黑魔法師列隊系統", color=0xff5a5a)
    self.init_layout(self.embed)
    pass

  def add_new_line(self):
    self.embed.add_field(name="", value="\n", inline=False)

  def init_layout(self, embed: Embed):
    embed.set_thumbnail(url=cm.thumbnail_url)
    embed.add_field(name="現有車數", value="`48763`", inline=False)
    embed.add_field(name="總人數", value="`48763`", inline=False)
    embed.add_field(name="還有空位的車數", value="`48763`", inline=False)
    self.add_new_line()
    embed.set_footer(text=f"最後更新時間 {datetime.now().strftime('%m-%d %H:%M')}", icon_url=cm.thumbnail_url)

  @button(label="登記上車", style=ButtonStyle.primary, custom_id="create_car")
  async def create_car(self, interaction: Interaction):
    # await interaction.response.defer(ephemeral=True)
    await interaction.response.send_message("請輸入車名", ephemeral=True) ##currently not working

  @button(label="詳細資訊", style=ButtonStyle.grey, custom_id="search_car")
  async def delete_car(self, interaction: Interaction):
    await interaction.channel.send("翻車")

class Gui(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    self.bc = BotModel()
    self.overview = Overview_views()

  @commands.hybrid_command(name = "老黑", description = "開啟老黑介面")
  async def show_black(self, ctx: commands.Context):
    await ctx.defer();
    await ctx.send(view=self.overview, embed=self.overview.embed)

  @commands.hybrid_command(name = "gui", description = "popup GUI")
  async def show_interface(self, ctx: commands.Context):
    await ctx.send("For testing purpose, please modify the code to show the GUI.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Gui(bot))
