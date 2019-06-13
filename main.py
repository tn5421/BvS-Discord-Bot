import os
import discord
import time
import asyncio
import json

from discord.ext import commands

settings = json.loads(open('settings.json').read())
token = settings['token']
bvs_ver = settings['version']
# this comment only here because the interpreter is actually toxic awful garbage cancer
description = """Billy vs Snakeman InfoBot by tn5421"""
prefix = "!"
bot = commands.Bot(command_prefix=prefix, description=description)

wk_list = ["Craftworld at War", "AspenStory", "ADAM", "FarmVale", "ForeverQuest"]

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def wkai(ctx):
    day_wkai = "Today's WKAI summon is a "
    def get_rday():
        return (int(time.strftime("%d")))
    wk_day = get_rday() % 5
    day_wkai += wk_list[wk_day]
    await ctx.send(day_wkai)
    pass

@bot.command()
async def adam(ctx):
    adam_wkai = "The next ADAM summoning is in "
    def get_rday():
        return (int(time.strftime("%d")))
    wk_day = get_rday() % 5
    if wk_day == 2:
        adam_wkai += "5 Days"
    else:
        adam_wkai += (str((2 - get_rday()) % 5)) + " Day(s)"
    await ctx.send(adam_wkai)
    pass

@bot.command()
async def version(ctx):
    botver = "BvS-Discord-Bot is currently version " + (str(bvs_ver))
    await ctx.send(botver)
    pass

def yadg(string):
    ENDPOINT = 'https://yadg.cc/api/v2/query/'
    headers = {'Content-Type': 'application/json'}
    payload = {'input': string, }
    response = requests.post(url=f'{ENDPOINT}', json=payload)
    yadg_step1 = json.loads(response.text)
    print(yadg_step1)
    resp1 = yadg_step1['url']
    time.sleep(1)
    response = requests.get(resp1)
    yadg_step2 = json.loads(response.text)

@bot.command()
async def search_music(ctx):
	await ctx.send(str(yadg_step2))

bot.run(token)
