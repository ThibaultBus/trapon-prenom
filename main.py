import discord
from trapon_client import TraponClient
from loop import Loop
from name_generator import NameGenerator

# Flemme de faire un truc avec une date je fais un truc déguelasse
LAUNCH_HOUR = 8
FILE = "prenoms.txt"
TOKEN = 'OTAyODI5ODE1MDgwNTc0OTc2.YXkHyQ.PzqWs80sXxkDLIyVP5gaBFxh9Io'


client = TraponClient()
name_generator = NameGenerator(FILE)
loop = Loop(LAUNCH_HOUR, client, name_generator)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$trapon'):
        if client.channel == None or client.channel != message.channel:
            client.channel = message.channel
            await client.channel.send("J'utiliserai ce channel pour mes annonces dorénavant !")
        await client.send_new_name(name_generator.get_random_name())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run(TOKEN)
