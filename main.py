import json
import discord
import os

PATH = "secret.json"
TOKEN = get_token(PATH)
client = discord.Client()

def get_token(path):
    """get token from json file 
    to connect to discord API
    """
    with open(path) as f:
        token = json.load(f)['token']
    return token

@client.event
async def on_message(message):
    if message.author == client.user :
        #if the message was written by bot
        return
    
    
