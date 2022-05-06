import discord
from discord.ext import commands
import asyncio

guilds = [972245173046227014]
intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = discord.Bot(command_prefix = ";", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is now on")
    print("------------------")
    print("enjoy!")


@bot.event
async def  on_member_join(member):
   if member.guild.id in guilds:
       embed = discord.Embed(title = f"welcome {member.display_name}~", description= f"thanks for joining {member.guild.name}")
       embed.set_image(url = "https://media.discordapp.net/attachments/971951707049295876/972241568318783498/unknown.png?width=674&height=422")
       embed.add_field(name = "rules", value = "check out <#972245374309900288>", inline= True)
       embed.add_field(name = "general", value = "talk in <#972245175298580481>", inline = True)
       embed.add_field(name = "events", value = "see events in <#972245535203418132>", inline = True)
       embed.add_field(name = "applications", value = "try and become a mod <#972245670595547186>", inline = True)
       embed.set_author(url= member.avatar)
       await member.send(embed = embed)

@bot.slash_command(name = "ping")
async def ping(ctx):
   embed = discord.Embed(color = 0xe91e63, title= "pong 🏓", description= f" ping took {round(bot.latency, 1)}ms")
   embed.set_thumbnail(url = "https://c.tenor.com/LqNPvLVdzHoAAAAC/cat-ping.gif")
   await ctx.respond(embed = embed)

@bot.slash_command(name = "echo", guild_ids = [971951707049295873])
async def echo(ctx, content: str):
    await ctx.respond(content)


#keep at bottom
bot.run("OTcyMjE5NjMwMzM4ODUwODU2.GQa7El.LM5awLwn40PbbsTeQcOVxnq-uoapvzzHOYB5B8")
