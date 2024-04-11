from discord.ext import commands
from discord import app_commands
from pathlib import Path
import discord
from discord.app_commands import Choice
import sys
sys.path.insert(0, Path(__file__).parent.parent.parent.as_posix())
from backend import Connecter as conn

unimplement = "尚未實裝"


def creat_embeds(list):
  embeds = []
  for i in list:
    embed = discord.Embed(
        title=i['CarName'],
        description=f"CarName : {i['CarName']}\rPlannedDate : {i['PlannedDate']}\rFightTime : {i['FightTime']}",
        color=discord.Color.blue()  # 設定 Embed 的顏色
    )
    embeds.append(embed)
  return embeds

# 宣告一個 ViewClass 類別，繼承 discord.ui.View
class ViewClass(discord.ui.View):
  def __init__(self, embeds, conne: conn.Connecter, timeout: float or None = 180):
      super().__init__(timeout=timeout)
      self.embeds = embeds
      self.current_page = 0
      self.conne = conne
  
  async def show_current_page(self, interaction: discord.Interaction):
    try:
      await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)
    except Exception as e:
      print(e)
      
  @discord.ui.button(label="<", style=discord.ButtonStyle.gray)
  async def go_previous(self, interaction: discord.Interaction, button: discord.ui.Button):
      if self.current_page > 0:
          self.current_page -= 1
          await self.show_current_page(interaction)
      else:
          await self.show_current_page(interaction)
          
  @discord.ui.button(label="ShowDetail", style=discord.ButtonStyle.gray)
  async def show_detail(self, interaction: discord.Interaction, button: discord.ui.Button):
      try:
        description = ''
        for i in self.conne.search_car_name(self.embeds[self.current_page].title, 4):
          description += f"順序:{i['JoinNumber']}  遊戲ID:{i['PlayerName']}\r"
          
        list = discord.Embed(
          title=self.embeds[self.current_page].title,
          description=description,
          color=discord.Color.blue()  # 設定 Embed 的顏色
        )
        await interaction.response.send_message(embed=list)
      except Exception as e:
        print(e)
  @discord.ui.button(label=">", style=discord.ButtonStyle.gray)
  async def go_next(self, interaction: discord.Interaction, button: discord.ui.Button):
      if self.current_page < len(self.embeds) - 1:
          self.current_page += 1
          await self.show_current_page(interaction)
      else:
          await self.show_current_page(interaction)

class Main(commands.Cog):
  x = conn.Connecter()
  def __init__(self, bot):
    self.bot = bot
     
  @app_commands.command(name = "查詢月份", description = "查詢指定月份")
  @app_commands.describe(month = "輸入月份")
  async def search_month(self, interaction: discord.Interaction ,month: int):
    try:
      list = self.x.search_car_month(month)
      embeds = creat_embeds(list)
      view = ViewClass(embeds=embeds, timeout=30, conne=self.x)
      await interaction.response.send_message(view=view, embed=embeds[0])
    except Exception as e:
      print(e)
  
  @commands.hybrid_command(name = "查詢車名", description = "查詢指定車名的車")
  @app_commands.describe(carname = "輸入車名", month = "輸入月份")
  async def search_car_name(self, ctx, carname: str, month: int):
    await ctx.send(self.x.search_car_name(carname, month))

  @commands.hybrid_command(name = "sqlcmd", description = "fortest")
  @app_commands.describe(sqltext = "sqlsql")
  async def SQL(self, ctx, sqltext: str):
    await ctx.send(sqltext)
    rets = self.x._Test(sqltext)
    for ret in rets:
      await ctx.send(ret)
  
  # @commands.hybrid_command(name = "翻車", description = "刪除一台車")
  # async def delete_car(self, ctx):
  #   await ctx.send(embed = embed)
  
  # @commands.hybrid_command(name = "加入", description = "上車")
  # async def passenger_join(self, ctx):
  #   await ctx.send(unimplement)

async def setup(bot: commands.Bot):
  await bot.add_cog(Main(bot))
