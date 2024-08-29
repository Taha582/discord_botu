import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def nasılsın(ctx):
    await ctx.send("iyiyim peki siz")
@bot.command()
async def neler_yapabilirsin(ctx):
    await ctx.send("bana kodlanan her şeyi yapabilirim")
@bot.command()
async def şarkı_çalabilirmisin(ctx):
    await ctx.send("hayır(geliştiriliyor)")
@bot.command()
async def peki_nezaman_çalabilirsin(ctx):
    await ctx.send("üzgünüm bunun hakkında bilgi veremem")




bot.run()
