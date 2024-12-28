import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime,timezone
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

NEW_YEAR = datetime(2025, 1, 1, 0, 0, 0)
scheduler = AsyncIOScheduler()
channel = None
last_message = None

intents = discord.Intents.default()
intents.message_content = True

def get_prefix(bot, message):
    return ["!", "?", "="]  # Add multiple prefixes

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    # Starting the scheduler
    scheduler.add_job(update_countdown, "interval", seconds=60)
    scheduler.start()
    
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error: {error}")
    
@bot.command()
async def hello(ctx):
    global channel
    channel = ctx.channel
    await ctx.send("Hello, world!")

@bot.command()
async def greet(ctx):
    global channel
    channel = ctx.channel
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
    global channel
    channel = ctx.channel
    await ctx.send(f"Echoing: {arg}")
    
@bot.command()
async def countdown(ctx):
    global channel
    channel = ctx.channel
    now = datetime.now()
    if now >= NEW_YEAR:
        await ctx.send("Happy New Year! 🎉🎆🎊")
        scheduler.shutdown()
    else:
        delta = NEW_YEAR - now
        days, hours, minutes, seconds = delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds % 60
        countdown_message = (
            f"⏳ Countdown to New Year:\n"
            f"**{days} days, {hours} hours, {minutes} minutes, {seconds} seconds** remaining!"
        )
        global last_message
        last_message = await channel.send(countdown_message)   
    
async def update_countdown():
    global last_message
    global channel
    if channel is None:
        print("Channel is not set.")
        return
    
    now = datetime.now()
    if now >= NEW_YEAR:
        if last_message:
            await last_message.edit(content="Happy New Year! 🎉🎆🎊")
        scheduler.shutdown()
    else:
        delta = NEW_YEAR - now
        days, hours, minutes, seconds = delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds % 60
        countdown_message = (
            f"⏳ Countdown to New Year:\n"
            f"**{days} days, {hours} hours, {minutes} minutes, {seconds} seconds** remaining!"
        )
        if last_message:
            await last_message.edit(content=countdown_message)
        else:
            last_message = await channel.send(countdown_message)

bot.run(DISCORD_BOT_TOKEN)