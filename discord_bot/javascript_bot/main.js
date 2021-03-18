const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready', () => {
	console.log("Connected as " + client.user.tag)
})

//due to this file being public, my token is hosted privately with apache2
bot_secret_token = "XXXXXX"

client.login(bot_secret_token)
