import discord
from trapon_client import TraponClient
from loop import Loop
from name_generator import NameGenerator
from dotenv import dotenv_values

config = dotenv_values(".env")

client = TraponClient(config["TARGET_USER"])
name_generator = NameGenerator(config["FILE"])
loop = Loop(int(config["LAUNCH_HOUR"]), client, name_generator)


@ client.event
async def on_message(message):
    if client.is_message_from_bot(message):
        return

    if message.content.startswith('$trapon'):
        await client.on_new_bot_call(message)
        await client.send_new_name(name_generator.get_random_name())


@ client.event
async def on_ready():
    await client.on_login()


client.run(config["TOKEN"])
