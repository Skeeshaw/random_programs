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

async def on_message(message):
    #stop bot from replying to itself
    if message.author == client.user:
        return

    if message.content.startswith('-join'):
        await discord.VoiceProtocol.connect









client.run(TOKEN)
