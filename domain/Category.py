from typing import Iterable

from domain.CategoryStore import CategoryStore
from domain.Good import Good


class Category:
    def __init__(self, categoryStore: Iterable[CategoryStore], name: str, goods: Iterable[Good], children: Iterable[object] = None):
        self.categoryStore = categoryStore
        self.name = name
        self.goods = goods
        self.children = children
