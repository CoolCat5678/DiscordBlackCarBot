from discord.ext import commands
from discord import app_commands
from pathlib import Path
from discord.app_commands import Choice
import sys
sys.path.insert(0, Path(__file__).parent.parent.parent.as_posix())
from backend import Connecter as conn

unimplement = "尚未實裝"

class Main(commands.Cog):
  x = conn.Connecter()
  def __init__(self, bot):
    self.bot = bot
  
  @commands.hybrid_command(name = "查詢月份", description = "查詢指定月份")
  @app_commands.describe(month = "輸入月份")
  async def search_month(self, ctx, month: int):
    await ctx.send(self.x.SearchCarMonth(month))
  
  @commands.hybrid_command(name = "查詢車長", description = "查詢指定車長的車")
  @app_commands.describe(carname = "輸入車名", month = "輸入月份")
  async def search_car_name(self, ctx, carname: str, month: int):
    await ctx.send(self.x.SearchCarName(carname, month))

  @commands.hybrid_command(name = "sqlcmd", description = "fortest")
  @app_commands.describe(sqltext = "輸入車名")
  async def SQL(self, ctx, sqltext: str):
    await ctx.send(sqltext)
    rets = self.x._Test(sqltext)
    for ret in rets:
      await ctx.send(ret)
  
  # @commands.hybrid_command(name = "翻車", description = "刪除一台車")
  # async def delete_car(self, ctx):
  #   await ctx.send(unimplement)
  
  # @commands.hybrid_command(name = "加入", description = "上車")
  # async def passenger_join(self, ctx):
  #   await ctx.send(unimplement)

async def setup(bot: commands.Bot):
  await bot.add_cog(Main(bot))