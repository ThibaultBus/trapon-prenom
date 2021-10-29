import discord

# Client gérant les interactions avec Discord


class TraponClient(discord.Client):

    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.channel: discord.TextChannel = None

    async def send_new_name(self, name: str):
        if self.channel != None:
            await self.channel.send('Benjamin s\'appelle maintenant **{0}**'.format(name))
