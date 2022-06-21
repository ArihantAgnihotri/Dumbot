"""
This file is a cog file for the bot and helps in user choice

Commands used:

1. Dice roll
2. coin flip

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
        print("cog : choice_help_cog.py has been loaded")

    # Coin flip command:

    @commands.command(aliases=['coin', 'flip', 'coinflip', 'flipacoin', 'coin_flip'])
    async def _coin_flip(self, ctx):
        num = randint(0, 1)
        if num == 0:
            await ctx.channel.send(f"{ctx.author.mention}\nHeads!! 🧠")
        if num == 1:
            await ctx.channel.send(f"{ctx.author.mention}\nTails!! 🐈")

    # Dice roll command

    @commands.command(aliases=['dice', 'diceroll', 'rolladice'])
    async def _dice_roll(self, ctx):
        await ctx.channel.send(f"{ctx.author.mention}\nIt shows {randint(1, 6)} on its face!")

    # Howgay command

    @commands.command()
    async def howgay(self, ctx):
        rating = randint(1, 100)
        await ctx.channel.send(f"{ctx.author.mention} is {rating}% gay")
        if rating > 50:
            await ctx.channel.send("🌈 A proud member of the LGBTIA+ community 🌈")
        if rating < 50:
            await ctx.channel.send("🗿 Ya straight as hell beh 🗿")


def setup(client):
    client.add_cog(choice_help_cog(client))
