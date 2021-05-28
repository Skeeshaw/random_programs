from requests import get
import discord
import urllib

url = "http://192.168.1.148/password.html"
file = urllib.request.urlopen(url)

for line in file:
    decoded_line = line.decode("utf-8")
    
TOKEN = decoded_line
##############################################
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('-begin'):
        channel1 = message.channel
        await channel1.send('I need to know the password first.')
        def check(m):
            return m.content == "testing-purposes" and m.channel == channel1
        msg = await client.wait_for('message', check=check)
        await channel1.send('It begins.')
        embedVar = discord.Embed(title="Heisenberg Bot", description="", color=0x00ff00)
        embedVar.add_field(name="Announcement", value="This server is now beginning automatic maintenance by the Heisenberg Bot. Thank you for using this server.", inline=False)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/838114727816462356/549cd61912d8c2fd3f7d912d84e8ffb3.webp?size=2048")
        embedVar.set_author(name="Created by skee#0855", icon_url="https://cdn.discordapp.com/avatars/250019320875188224/e2880238f7650b9564e86b8b6b8593b5.webp?size=128")
        channel2 = client.get_channel(847934712286674954)
        await channel2.send(embed=embedVar)
        guild = message.guild
        await guild.create_text_channel('cool-channel')
        channel = client.get_channel('cool-channel')
        await channel.edit(name='cooler-channel')
        #await guild.create_category('arg2')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)