import os
import discord
from dotenv import load_dotenv
from discord import app_commands 
from discord.ext import commands
import random

Token = os.environ['Token']

intents = discord.Intents.all()
load_dotenv()
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online,
                            activity=discord.Game('with voltz'))


@bot.event
async def on_message(message):
  if message.content.startswith(".ping"):
    await message.channel.send("We are online.")

  elif message.content.startswith(".flip"):
    number = random.randint(0, 1)
    if number == 1:
      await message.channel.send("It has flipped a head!")
    elif number == 0:
      await message.channel.send("It has flipped a tail!")

  

  elif message.content.startswith(".troll"): #reverted to placeholder
    await message.channel.send(
      "[insert troll message/gif]")

  

  elif message.content.startswith(".help"):
    await message.channel.send(
      "`All the commands  💯 \n .ping - Checks if bot is working. \n .troll - No comment \n .flip - Flips a coin and returns Heads or Tails. \n .banger - Posts a random banger video.[temp] \n \n Hidden commands: If you know them use at own risk.`"
    )


  
  elif message.content.startswith(".banger"): #used to display random youtube videos, reverted to placeholders 
    number = random.randint(0, 5)
    if number == 0:
      await message.channel.send("0")
    elif number == 1:
      await message.channel.send("1")
    elif number == 2:
      await message.channel.send("2")
    elif number == 3:
      await message.channel.send("3")
    elif number == 4:
      await message.channel.send("4")
    elif number == 5:
      await message.channel.send("5")

  elif message.content.startswith(".spam"):
    await message.channel.send("[placeholder for spam message/gif]") #switched to placeholders for now
    i=0
    while i<10: 
     await message.channel.send("Spam incoming.")
     i=i+1    
    await message.channel.send("[placeholder for spam message/gif]")
    
    
 
 

  
bot.run(Token)
