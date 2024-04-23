from discord.ext import commands
import importlib

import model.bot_model as models
import views.bot_views as views

layout = views.Bot_Layouts

class Gui(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    self.bc = models.BotModel()
    importlib.reload(views)
    importlib.reload(models)

  @commands.hybrid_command(name = "老黑", description = "開啟老黑介面")
  async def show_black(self, ctx: commands.Context):
    await ctx.defer();
    try: 
      await layout.OVERVIEW.value.show_view(ctx);
    except Exception as e:
      print(e);

  @commands.hybrid_command(name = "gui", description = "popup GUI")
  async def show_interface(self, ctx: commands.Context):
    await ctx.send("For testing purpose, please modify the code to show the GUI.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Gui(bot))
