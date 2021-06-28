from typing import List

from domain.GoodStore import GoodStore
from utils.Observable import Subject, Observer


class Good(Subject):
    def attach(self, observer: Observer) -> None:
        super().attach(observer)

    def detach(self, observer: Observer) -> None:
        super().detach(observer)

    def notify(self) -> None:
        super().notify()

    def __init__(self, goodStores: List[GoodStore]):
        self.goodStores = goodStores

    def update_good_store(self, goodStore: GoodStore):
        self.goodStores.append(goodStore)
        super().notify()
