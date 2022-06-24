#####################################
#  https://github.com/T4WW	    
#  https://github.com/alpkeskin	    

#####################################
import os 
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
		chegglink = link[0]
		try:
			if(chegglink[0:22] == "https://www.chegg.com/"):
				userRequest = requests.get(link[0],headers={"user-agent":"SET YOUR USER AGENT HERE",
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"cookie":"id_token= SET ID TOKEN HERE"})
				source = BeautifulSoup(userRequest.content,"html")
				dmain = source.find("div",attrs={"class":"answer-given-body ugc-base"})
				images = dmain.findAll('img')
				for image in images:
					await message.author.send(image['src'])
				await message.author.send('-----------------------------------------------------')
				data = source.find("div",attrs={"class":"answer-given-body ugc-base"}).text
				file = open('answer.txt', 'w')   
				file.write(data)  
				file.close()
				my_files = [discord.File('answer.txt')]
				print(link[0])
				await message.author.send(files=my_files)
				exit(0)
			else:
	 			print("Link is not valid.")
	 	except ValueError:
	 		print("Unexpected value is given")
			exit(1)
		 except ConnectionError as ex:
		     raise RuntimeError('Failed to establish connection to the given soruce') from ex
			

bot.run("!!! SET YOUR BOT TOKEN HERE !!!")
