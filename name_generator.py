import random


class NameGenerator:
    def __init__(self, file: str) -> None:
        self.names = open(file).readlines()

    def get_random_name(self) -> str:
        return random.choice(self.names)
