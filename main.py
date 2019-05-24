import os
import discord
import time
import asyncio

from wkai import *
from discord.ext import commands

description = """Billy vs Snakeman InfoBot by tn5421"""
prefix = "!"
bot = commands.Bot(command_prefix=prefix, description=description)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
wkai()

@bot.command()
adam()

bot.run("a token")
