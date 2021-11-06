import discord

# Client gérant les interactions avec Discord


class TraponClient(discord.Client):

    def __init__(self, target_user: str = "Someone", *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.channel: discord.TextChannel = None
        self.target_user: str = target_user

    async def send_msg(self, msg: str):
        if self.channel != None:
            await self.channel.send(msg)
        else:
            print("Aucun channel choisi")

    async def send_new_name(self, name: str):
        if self.channel != None:
            await self.channel.send('{0} s\'appelle maintenant **{1}**'.format(self.target_user, name))

    def is_message_from_bot(self, message: discord.Message):
        return message.author == self.user

    async def on_new_bot_call(self, message: discord.Message):
        if self.channel == None or self.channel != message.channel:
            self.channel = message.channel
            await self.channel.send("J'utiliserai ce channel pour mes annonces dorénavant !")

    async def on_login(self):
        print('We have logged in as {0.user}'.format(self))
