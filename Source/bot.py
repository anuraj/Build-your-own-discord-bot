import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime,timezone

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

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
    
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error: {error}")

bot.run(DISCORD_BOT_TOKEN)