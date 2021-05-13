import discord
from discord.ext import commands

token = 'your token'

client = commands.Bot(command_prefix="*") 
client.remove_command('help')

client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(f"*help")) 

@client.command()
async def help(ctx):
  embed = discord.Embed(title = "Help Center", description = "All commands of this bot is displayed here!")
  embed.add_field(name = "*hello", value = "Greet the bot.")
  embed.add_field(name = "*embed", value = "Example Embed.")
  await ctx.send(embed=embed)



@client.command()
async def hello(ctx):
	await ctx.author.send('Hello There')
	

@client.command()
async def embed(ctx):
	embed = discord.Embed(title = "Example", description = "Type your description.")
	embed.add_field(name="Example", value = "Type your value.")
	embed.add_field(name= "Example", value = "Type your value.")
	embed.add_field(name= "Example", value = "Type your value.") 
	await ctx.send(embed=embed)


@client.command()
async def reaction(ctx):
	await ctx.send("I will put a reaction")
	await ctx.message.add_reaction("✅")

client.run(token)
