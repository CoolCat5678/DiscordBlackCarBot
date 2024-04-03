import asyncio
import discord
from pathlib import Path
from discord.ext import commands
from discord.app_commands import Choice

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    print("Bot is ready")
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"載入 {extension} 完成")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"卸載 {extension} 完成")

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"重新載入 {extension} 完成")

async def load_extentions():
    for file in Path(__file__).parent.joinpath("cogs").rglob("*.py"):
        await bot.load_extension(f"cogs.{file.stem}")

async def main():
    async with bot:
        token = open("token.txt", "r").read()
        await load_extentions()
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())