from discord.ext import commands

bot = commands.Bot(command_prefix='-')


#-------------------Token Grabbing-------------------#

tokenfile = open("token.txt","r")

token = tokenfile.readline()



#----------------------------------------------------#

#----------------------Commands----------------------#



@bot.command()
async def usersearch(ctx, *args):
    await ctx.send(args)
    
bot.run(token)
    
