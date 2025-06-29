from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 0000000  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(f'The sum of {a} and {b} is {a + b}.')

@bot.command()
async def repeat(ctx, times: int, *, message: str):
    for _ in range(min(times, 5)):  # Limit to 5 repeats
        await ctx.send(message)

load_dotenv()
token = os.getenv("TOKEN")
bot.run(token)  # Starts the bot