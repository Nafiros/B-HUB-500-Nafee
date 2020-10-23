import string
import discord
import commands
import asyncio

async def is_command(message):
    if message.content[0] == '$':
        print("Command detected - Requested : " + message.content)
        if message.content == "$salut":
            await commands.hello(message)
    else:
        print("Not a command - Ignored")

def which_command(message):
    commandList = {"salut", "bye", "merci"}
    for i in commandList:
        if ("$" + i) == (message.content):
            return (i)