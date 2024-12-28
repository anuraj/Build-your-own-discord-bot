import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime,timezone

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

NEW_YEAR = datetime(2025, 1, 1, 0, 0, 0)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

@bot.command()
async def greet(ctx):
    display_name = ctx.author.display_name
    current_time = datetime.now()
    current_hour = current_time.hour
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    await ctx.send(f"{greeting}, {display_name}!")
    
@bot.command("echo")
async def echo(ctx,arg):
    await ctx.send(f"Echoing: {arg}")
    
@bot.command()
async def countdown(ctx):
    now = datetime.now()
    if now >= NEW_YEAR:
        await ctx.send("Happy New Year! 🎉🎆🎊")
    else:
        delta = NEW_YEAR - now
        days, hours, minutes, seconds = delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds % 60
        countdown_message = (
            f"⏳ Countdown to New Year:\n"
            f"**{days} days, {hours} hours, {minutes} minutes, {seconds} seconds** remaining!"
        )
        await ctx.send(countdown_message)    

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error: {error}")

bot.run(DISCORD_BOT_TOKEN)