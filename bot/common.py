import discord
from discord.ext import commands
from discord import Interaction

THUMBNAIL_URL = "https://media.discordapp.net/attachments/552116031347490829/1231983264978178148/561fac21ff50503336602f176971b61b.png?ex=6638f0d3&is=66267bd3&hm=35f61018a1d1e23839f4dec34e73342648d3fe63511a7fa400e7a778defa323c&=&format=webp&quality=lossless"

FOOTER_ICON = "https://cdn.discordapp.com/attachments/557855385298534406/588700490728996904/707f1f2b87a0088e4e3d9de975d87adc.png?ex=6633818e&is=66210c8e&hm=515c9be384cbe0f6a0b19ca2d5c785e1ddacc046f65988d8482885c2e9df6976&"


class Utils:
  @staticmethod
  async def fetch_user(ctx: commands.Context, user_id: int) -> discord.User:
    return await ctx.bot.fetch_user(user_id)

  @staticmethod
  async def get_user_id(ctx: commands.Context | None = None, interaction: Interaction | None = None) -> int:
    if (ctx != None):
      return ctx.author.id
    return interaction.user.id
  
  @staticmethod
  async def get_user(ctx: commands.Context | None = None, interaction: Interaction | None = None) -> discord.User:
    if (ctx != None):
      return ctx.author
    return interaction.user