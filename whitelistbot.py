import discord
import env
from discord.ext import commands


def parse_message(message):
    if message.lower().startswith("!whitelist"):
        return "whitelist"
    elif message.lower().startswith("!blacklist"):
        return "blacklist"
    else:
        return "pass"

def whitelist(message):
    return "Attempting to Whitelist: {username}"

def blacklist(message):
    return "Attempting to Blacklist: {username}"

def do_nothing(message):
    return ''

actions = {
            "whitelist": whitelist,
            "blacklist": blacklist,
            "pass": do_nothing
        }


def __main__():
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("logged in")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        action= parse_message(message.content)
        reply = actions[action](message.content)
        if reply != '':
            await message.channel.send(reply)
    

    client.run(env.token)


if __name__ == '__main__':
    __main__()
