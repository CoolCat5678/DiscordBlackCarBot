import discord
from discord.ext import commands

class Gui(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.hybrid_command(name = "gui", description = "popup GUI")
  async def show_interface(self, ctx):
    view = discord.ui.View(timeout = 30)
    view.add_item(discord.ui.Button(label = "皮炎"))
    await ctx.send(view = view)

async def setup(bot: commands.Bot):
    await bot.add_cog(Gui(bot))
