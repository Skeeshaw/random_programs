from requests import get
import discord
import urllib
from time import sleep

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
        embedVar = discord.Embed(title="Heisenberg Bot", description="", color=0x058bff)
        embedVar.add_field(name="Announcement", value="This server is now beginning automatic maintenance by the Heisenberg Bot. Thank you for using this server.", inline=False)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/838114727816462356/549cd61912d8c2fd3f7d912d84e8ffb3.webp?size=2048")
        embedVar.set_author(name="Created by skee#0855", icon_url="https://cdn.discordapp.com/avatars/250019320875188224/e2880238f7650b9564e86b8b6b8593b5.webp?size=128")
        channel2 = client.get_channel(847934712286674954)
        await channel2.send(embed=embedVar)
        guild = message.guild
        await guild.create_category_channel(name="Administrator+", overwrites=all_staff_overwrites)
        staff_category=discord.utils.get(guild.categories, name="Staff")
    if message.content.startswith('!staffroles'):
        guild = message.guild
        await guild.create_role(name="Drug Lord", color=discord.Color(0x058bff), hoist=1, permissions=discord.Permissions(permissions=8))
        await guild.create_role(name="Chairman", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=8))
        """i know these work so to save me from deleting these every timei  run this i will comment it out
        await guild.create_role(name="Chief Executive Officer", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=8))
        await guild.create_role(name="Chief Financial Officer", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Board of Directors", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Director", color=discord.Color(0x0f1233), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Independent Director", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Senior Vice President", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Vice President", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Principal Accounting Officer", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Accountant", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        await guild.create_role(name="Investor", color=discord.Color(0x030303), hoist=1, permissions=discord.Permissions(permissions=2251542080))
        """
              
#2251542080 - permisions for a normal user
#0x0f1233 - board of directors	


"""
async def save_audit_logs(guild):
     with open(f'audit_logs_{guild.name}', 'w+') as f:
          async for entry in guild.audit_logs(limit=100):
               f.write('{0.user} did {0.action} to {0.target}'.format(entry))
"""




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)