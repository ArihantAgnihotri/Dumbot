# App id : 848987248711041094
# token : ODQ4OTg3MjQ4NzExMDQxMDk0.YLUm_Q.e64HpBciC3A7CQ23DcSQ_cqID6o
# permissions integer : 75840
# https://discordapp.com/oauth2/authorize?client_id=848987248711041094&scope=bot&permissions=75840

import discord
import os
from discord.ext import commands
from discord.ext import tasks
from random import randint


client = commands.Bot(command_prefix="!")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print(f'Up and loaded as :  {client.user}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send(f'{ctx.author.mention} \n This command does not exist, YET!')


'''
Basic prototype of function command:

@client.command(aliases=[''])
async def _func_name(ctx):
    await ctx.channel.send(f"{ctx.author.mention}\n MESSAGE HERE")
'''


@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)


client.run('ODQ4OTg3MjQ4NzExMDQxMDk0.YLUm_Q.e64HpBciC3A7CQ23DcSQ_cqID6o')
