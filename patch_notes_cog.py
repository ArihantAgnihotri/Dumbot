"""
This file is a cog file for the bot.py and helps in user choice

Commands used:

1. web scrape the most recent patch notes
3. use pornhub api to get vids
4. add a special command to load a premium cog

"""
import random
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import requests


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


class web_cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("cog : patch_notes_cog.py has been loaded")

    @commands.command(aliases=['patch', 'patch notes', 'patch_notes'])
    async def _patch_notes(self, ctx, *, message):
        game_list = [x.strip() for x in message.split(',')]
        length = len(game_list)
        game_name = game_list[length-1]
        await ctx.channel.send(game_name)
        await ctx.channel.send(f'{ctx.author.mention} Searching for latest patch notes of the game:  {game_name}')
        url = f'https://allpatchnotes.com/{game_name}/'
        print(url)
        r1 = requests.get(url)
        html_content1 = r1.content
        soup = BeautifulSoup(html_content1, 'html.parser')
        anchors = soup.find_all('a')
        link_list = ['']

        for links in anchors:
            s = links.get('href')
            if type(s) is str:
                link_list.append(s)

        patch_url = ""
        flag = 0

        index = 0
        for links in link_list:
            if flag == 1:
                break

            notes = list(links.split('/'))
            for item in notes:
                if item == 'patch-notes':
                    patch_url = link_list[index + 2]
                    flag = 1
                    break
            index += 1

        r2 = requests.get(patch_url)
        html_content2 = r2.content
        patch_soup = BeautifulSoup(html_content2, 'html.parser')
        patch_list = ['']
        for para in patch_soup.find_all("p"):
            patch_list.append(para.get_text())
        end = 'Your email address will not be published. Required fields are marked *'
        n = patch_list.index(end)
        patch_list = patch_list[3:n]
        final_patch_list = ['']

        for item in patch_list:
            final_patch_list += list(item.split('.'))
        await ctx.channel.send(f"{ctx.author.mention}")
        for item in final_patch_list:
            await ctx.channel.send(f'{item}')

        patch_embed = discord.Embed(title="For more information", colour=0xff0000)
        patch_embed.add_field(name=f"{patch_url}", value="", inline=False)
        await ctx.channel.send(embed=patch_embed)

    @_patch_notes.error
    async def patch_notes_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.send(f'{ctx.author.mention} \n Correct way to enter the command is : !patch '
                                   f'apex-legends (spaces replaced by -)')






def setup(client):
    client.add_cog(web_cog(client))
