from typing import List

from domain.CategoryStore import CategoryStore
from domain.Good import Good


class Category:
    def __init__(self, id: int, categoryStore: List[CategoryStore], name: str, goods: List[Good], children: List[object] = None):
        self.id = id
        self.categoryStore = categoryStore
        self.name = name
        self.goods = goods
        self.children = children
