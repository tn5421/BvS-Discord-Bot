import os
import discord
import time
import asyncio

from discord.ext import commands

wk_list = ["Craftworld at War", "AspenStory", "ADAM", "FarmVale", "ForeverQuest"]
rday = (int(time.strftime("%d")))
wk_day = rday % 5

def wkai():
    async def wkai(ctx):
        day_wkai = "Today's WKAI summon is a "
        day_wkai += wk_list[wk_day]
        await ctx.send(day_wkai)
        pass

def adam ():
    async def adam(ctx):
        adam_wkai = "The next ADAM summoning is in "
        if wk_day == 2:
            adam_wkai += "5 Days"
        else:
            adam_wkai += (str((2 - rday) % 5)) + " Days"
        await ctx.send(adam_wkai)
        pass