import discord
import asyncio

async def hello(message):
    str = "Hey, bonjour à toi " + message.author.name
    await message.channel.send(str)
