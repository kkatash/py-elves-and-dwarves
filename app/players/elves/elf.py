from app.players.player import Player
from abc import ABC


class Elf(Player, ABC):
    def __init__(self, nickname, musical_instrument):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a "
              f"song on the {self._musical_instrument}")
