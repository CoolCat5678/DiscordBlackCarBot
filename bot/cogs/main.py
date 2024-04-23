from discord.ext import commands
from model.bot_model import BotModel
from views.bot_views import Bot_Layouts

unimplement = "尚未實裝"

class Main(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.bc = BotModel()
  
  @commands.hybrid_command(name = "查詢月份", description = "查詢指定月份")
  async def search_month(self, ctx: commands.Context, month: int):
    await ctx.send(self.bc.search_car_month(month = month))
  
  @commands.hybrid_command(name = "查詢車長", description = "查詢指定車長的車")
  async def search_car(self, ctx: commands.Context, car_name: str, month: int):
    await ctx.send(self.bc.search_car_name(car_name = car_name, month = month))

  @commands.hybrid_command(name = "開車", description = "新增一台車")
  async def create_car(self, ctx: commands.Context, car_name: str, month: int, day: int, player_name: str, discord_id: str, fight_time: int=60):
    await ctx.send(self.bc.create_car(car_name=car_name, month=month, day=day, player_name=player_name, discord_id=discord_id, fight_time=fight_time))
  
  @commands.hybrid_command(name = "翻車", description = "刪除一台車")
  async def delete_car(self, ctx):
    await ctx.send(unimplement)
  
  @commands.hybrid_command(name = "加入", description = "上車")
  async def passenger_join(self, ctx: commands.Context, car_name: str, month: int, player_name: str, discord_id: str):
    await ctx.send(self.bc.join_car(car_name=car_name, month=month, player_name=player_name, discord_id=discord_id))

async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))


