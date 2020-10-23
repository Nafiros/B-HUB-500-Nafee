import discord
import asyncio
import checker

client = discord.Client()

@client.event
async def on_ready():
    print("Nafee répond présent et est à votre entière disposition :) !")

@client.event
async def on_message(message):
    if message.author.name != "Nafee":
        await checker.is_command(message)

client.run("Your Token Here")