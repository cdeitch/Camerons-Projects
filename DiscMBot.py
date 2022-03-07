# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('OTQyMjc2MTU3MjIxNTExMjM5.YgiJDg.H8WGfOYVznOKpziSw7prYU7i3hI')

bot = commands.Bot(command_prefix='m.')


#@bot.command(description="Gives description of bot command")
#async def help(ctx):
#    ctx.send("Elijah is Gay")


@bot.command(description="Mutes the specified user.")
async def mute(ctx, members: commands.Greedy[discord.Member] = None, *, reason=None):
    for member in members:
        try:
            await member.edit(reason=reason, mute=True)
        except discord.Forbidden:
            pass


@bot.command(description="Unmutes the specified user.")
async def unmute(ctx, members: commands.Greedy[discord.Member], *, reason=None):
    for member in members:
        try:
            await member.edit(reason=reason, mute=False)
        except discord.Forbidden:
            pass


@bot.command(description="Mutes the specified user.")
async def deaf(ctx, members: commands.Greedy[discord.Member] = None, *, reason=None):
    for member in members:
        try:
            await member.edit(reason=reason, deafen=True)
        except discord.Forbidden:
            pass


@bot.command(description="Undeafens the specified user.")
async def undeaf(ctx, members: commands.Greedy[discord.Member] = None, *, reason=None):
    for member in members:
        try:
            await member.edit(reason=reason, deafen=False)
        except discord.Forbidden:
            pass
bot.run('OTQyMjc2MTU3MjIxNTExMjM5.YgiJDg.H8WGfOYVznOKpziSw7prYU7i3hI')
