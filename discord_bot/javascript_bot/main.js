const Discord = require('discord.js')
const client = new Discord.Client()
const fs = require('fs')
var fetch = require('node-fetch')


client.on('ready', () => {
	console.log("Connected as " + client.user.tag)
})

fs.readFile('password.env', (err, data) => {
	if (err) throw err;

	var test = (data.toString());
	console.log(test)
})


//due to this file being public, my token is being held in a .env file
//
//client.login(test)
