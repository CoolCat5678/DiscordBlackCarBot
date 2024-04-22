import asyncio
import discord
from pathlib import Path
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")

@bot.command()
async def load(ctx: commands.Context, extension):
    res = await call_awaitable(lambda: bot.load_extension(f"cogs.{extension}")) == None;
    await ctx.send(f"載入 {extension} {'完成' if res else '失敗'}")

@bot.command()
async def unload(ctx: commands.Context, extension):
    res = await call_awaitable(lambda: bot.unload_extension(f"cogs.{extension}")) == None;
    await ctx.send(f"卸載 {extension} {'完成' if res else '失敗'}")

@bot.hybrid_command(name="reload", description="重新載入指定擴充功能")
async def reload(ctx: commands.Context, extension: str = 'gui'):
    res = await call_awaitable(lambda: bot.reload_extension(f"cogs.{extension}")) == None;
    await ctx.send(f"重新載入 {extension} {'完成' if res else '失敗'}")

async def load_extentions():
    for file in Path(__file__).parent.joinpath("cogs").rglob("*.py"):
        await bot.load_extension(f"cogs.{file.stem}")

async def call_awaitable(func: callable):
    try:
        await asyncio.wait_for(func(), timeout=1)
        return None
    except Exception as e:
        print(e);
        return "Error..."

async def main():
    async with bot:
        token = open("token.txt", "r").read()
        await load_extentions()
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())