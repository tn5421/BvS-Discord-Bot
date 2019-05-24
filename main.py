import os
import discord
import time
import asyncio

from discord.ext import commands

description = """Billy vs Snakeman InfoBot by tn5421"""
prefix = "!"
bot = commands.Bot(command_prefix=prefix, description=description)

startup_extensions =  ["wkai"]

if __name__ == "__main__":
    for ext in startup_extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            print(f"Failed to load extension {ext}\n{type(e).__name__}: {e}")

@bot.command()
async def load(ctx, extension_name:str=None):
    """
    Loads an extension.

    Valid extensions are:
        wkai
    """
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("`*`*`py\n{}: {}\n`*`*`".format(type(e).__name__, str(e)), delete_after=5)
        await asyncio.sleep(4)
        await bot.delete_message(ctx.message)
        return

    await bot.say(f"Loaded extension: __{extension_name}__")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run("a token")