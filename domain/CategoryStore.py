from typing import Iterable

from domain.GoodStore import GoodStore


class CategoryStore:
    def __init__(self, store, name: str, goods: Iterable[GoodStore], children: Iterable[object] = None):
        self.name = name
        self.goods = goods
        self.store = store
        self.children = children
