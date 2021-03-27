import json
import discord

PATH = "secret.json"
TOKEN = get_token(PATH)

def get_token(path):
    """get token from json file 
    to connect to discord API
    """
    with open(path) as f:
        token = json.load(f)['token']
    return token

client = discord.Client()
