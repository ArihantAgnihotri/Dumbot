"""
This file is a cog file for the bot and helps in user choice

Commands used:

1. help

"""
import random
from discord.ext import commands
from random import randint

'''

command prototype for this :

@commands.command(aliases=[''])
async def _func_name(self, ctx):
    await ctx.channel.send(f"{ctx.author.mention}\n MESSAGE HERE")
    
@command_name.error
async def command_name_error(self, ctx, error)
    if isinstance(error, commands.{errorname}):
    await ctx.channel.send(f'{ctx.author.mention} \n ERROR MESSAGE')


'''


class choice_help_cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("cog : help_cog.py has been loaded")

    # Coin flip command:

    @commands.command(aliases=['help', 'support', 'commands', 'actions'])
    async def _help(self, ctx):
       await ctx.channel.send(f"{ctx.author.mention}\nThis is the help command, the bot is currently on patch 1.2 and has the following commands: \n 1. diceroll : Rolls a dice \n2. coinflip : flips a coin \n3. greetings : greets the user with a random greeting \n4. roast : roasts the user with a random roast \n5. muah : makes the bot happy :) \n6. hupp : makes the bot sad :( ")

   
def setup(client):
    client.add_cog(choice_help_cog(client))
