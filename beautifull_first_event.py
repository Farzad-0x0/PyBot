import discord
from discord.ext import commands
from colorama import Fore , init
init(convert=True)





bot = commands.Bot(command_prefix= "!")



@bot.event
async def on_connect():
   print(Fore.CYAN+"-->" , Fore.LIGHTGREEN_EX+"My Bot connected to" , Fore.RED+"Discord API")
   print(Fore.CYAN+"-->",Fore.LIGHTGREEN_EX+f"My Bot joined to" , Fore.RED+f"{len(bot.guilds)} server")
   print("""""")




@bot.event
async def on_ready():
    print(Fore.CYAN+"-->" , Fore.BLUE+"Calculator bot is ready !")


@bot.event
async def on_disconnect():
    print(Fore.CYAN+"-->" , Fore.LIGHTRED_EX+"My Bot disconnected from" , Fore.GREEN+"Discord API")


@bot.event
async def on_resumed():
    print(Fore.CYAN+"-->" , Fore.LIGHTMAGENTA_EX+"My Bot resumed in" , Fore.GREEN+"Discord API")