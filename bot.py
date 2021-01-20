import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!help') or message.content.startswith('!хелп'):
    channel = message.channel
    await channel.send('```!ip или !айпи - IP сервера в майне \n!com или !сайт - cайт амазина \n!ds или !дс - вечний инвайт в дс амазина \n!help или !хелп - показать ето меню```')
  if message.content.startswith('!ip') or message.content.startswith('!айпи'):
    channel = message.channel
    await channel.send('Server IP: **95.217.224.152:26210**')  
  if message.content.startswith('!com') or message.content.startswith('!сайт'):
    channel = message.channel
    await channel.send('Сайт сервера: \n**https://amazin-server.000webhostapp.com**')
  if message.content.startswith('!ds') or message.content.startswith('!дс'):
    channel = message.channel
    await channel.send('Amazin discord invite: **https://discord.gg/RZxJF2K**')
  if message.content.startswith('!bot'):
    channel = message.channel
    await channel.send('I am here')

TOKEN='Nzk4OTA1MTQ3NzAyMjQ3NDI0.X_70Zg.gx6nD12EfLG-GFTeYbE277fP2Z4'
# value = os.getenv(TOKEN)
client.run(TOKEN)
