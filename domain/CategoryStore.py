from typing import List

from domain.GoodStore import GoodStore


class CategoryStore:
    def __init__(self, store, name: str, goods: List[GoodStore], children: List[object] = None):
        self.name = name
        self.goods = goods
        self.store = store
        self.children = children
