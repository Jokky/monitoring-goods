from typing import Iterable

from domain.GoodStore import GoodStore


class Good:
    def __init__(self, goodStore: Iterable[GoodStore]):
        self.goodStore = goodStore
