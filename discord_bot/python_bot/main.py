import discord
import urllib.request

url = "http://192.168.1.146/password.txt"
file = urllib.request.urlopen(url)

for line in file:
    decoded_line = line.decode("utf-8")
    

TOKEN = decoded_line

client = discord.Client()

@client.event
async def on_ready(): # when bot starts
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run(TOKEN)
