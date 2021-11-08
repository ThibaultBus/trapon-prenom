from typing import Tuple
import discord
from discord.ext import tasks
from datetime import datetime, timedelta
from name_generator import NameGenerator


class Loop:
    def __init__(self, event_hour: int, client: discord.Client, name_generator: NameGenerator) -> None:
        self.event_hour = event_hour
        self.client = client
        self.name_generator = name_generator
        self.reset()
        self.routine.start()

    def time_before_event(self) -> Tuple[int, int, int]:
        # On calcule la date du prochain event (aujourd'hui, ou demain si l'heure de lancement est déjà passé)
        now = datetime.now()
        print()
        event = datetime(now.year, now.month,
                         now.day, self.event_hour)

        if now.hour >= self.event_hour:
            event += timedelta(days=1)

        print(event)

        # On calcule le temps avant cette date de lancement
        delta = (event - datetime.now()).seconds

        hours = delta // 3600
        mins = delta % 3600 // 60
        secs = delta % 60

        return (secs, mins, hours)

    def reset(self):
        (secs, mins, hours) = self.time_before_event()
        print(secs, mins, hours)
        self.routine.change_interval(seconds=secs, minutes=mins, hours=hours)

    @tasks.loop(hours=24.0)
    async def routine(self):
        await self.client.send_new_name(self.name_generator.get_random_name())

    @routine.before_loop
    async def before_routine(self):
        await self.client.wait_until_ready()
