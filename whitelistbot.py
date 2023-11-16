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

def whitelist(command):
    return "Attempting to Whitelist: {username}"

def blacklist(command):
    return "Attempting to Blacklist: {username}"

def start_gamemaster(command):
    return ''

def stop_gamemaster(command):
    return ''

def do_nothing(command):
    return ''

actions = {
            "whitelist": whitelist,
            "blacklist": blacklist,
            "pass": do_nothing,
            "start_gamemaster": start_gamemaster,
            "stop_gamemaster": stop_gamemaster,
            "check_gamemaster":do_nothing,
            "check_whitelist":do_nothing,
            "check_blacklist":do_nothing,
            "unwhitelist":do_nothing,
            "unblacklist":do_nothing,
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
