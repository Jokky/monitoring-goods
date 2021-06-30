from typing import List

from domain.GoodStore import GoodStore
from utils.Observable import Subject, Observer


class Good(Subject):
    id: int = 0
    good_stores: List[GoodStore] = []

    def __init__(self, id: int, good_stores: List[GoodStore]):
        self.id = id
        self.good_stores = good_stores

    def attach(self, observer: Observer) -> None:
        super().attach(observer)

    def detach(self, observer: Observer) -> None:
        super().detach(observer)

    def notify(self) -> None:
        super().notify()
