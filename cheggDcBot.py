#####################################
#  https://github.com/T4WW	    #
#  https://github.com/alpkeskin	    #
#####################################

import discord, re, requests, asyncio
from discord.ext import commands
from bs4 import BeautifulSoup

bot = discord.Client()

@bot.event
async def on_ready():	
	
	guild_count = 0
	for guild in bot.guilds:		
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("BOT is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	
	link = re.findall(r'(https?://[^\s]+)', message.content)
	check = '-ch ' + link[0]

	if(message.content == check):
		r = requests.get(link[0],headers={"user-agent":"!!! SET YOUR USER AGENT HERE !!!",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"cookie":"id_token= !!! SET CHEGG ACCOUNT'S ID TOKEN HERE !!!"})
		source = BeautifulSoup(r.content,"html")
		dmain = source.find("div",attrs={"class":"answer-given-body ugc-base"})
		images = dmain.findAll('img')
		for image in images:
			await message.author.send(image['src'])
		await message.author.send('-----------------------------------------------------')
		data = source.find("div",attrs={"class":"answer-given-body ugc-base"}).text
		file = open('answer.txt', 'w')   
		file.write(data)  
		file.close()
		answer_file = [discord.File('answer.txt')]
		await message.author.send(files=answer_file)
	else:
	 	print("ERROR")


bot.run("!!! SET YOUR BOT TOKEN HERE !!!")
