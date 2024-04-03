from discord.ext import commands

unimplement = "尚未實裝"

class Main(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.hybrid_command(name = "查詢月份", description = "查詢指定月份")
  async def search_month(self, ctx):
    await ctx.send(unimplement)
  
  @commands.hybrid_command(name = "查詢車長", description = "查詢指定車長的車")
  async def search_car(self, ctx):
    await ctx.send(unimplement)

  @commands.hybrid_command(name = "開車", description = "新增一台車")
  async def create_car(self, ctx):
    await ctx.send(unimplement)
  
  @commands.hybrid_command(name = "翻車", description = "刪除一台車")
  async def delete_car(self, ctx):
    await ctx.send(unimplement)
  
  @commands.hybrid_command(name = "加入", description = "上車")
  async def passenger_join(self, ctx):
    await ctx.send(unimplement)

async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))


