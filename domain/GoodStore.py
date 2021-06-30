from typing import List

from domain.Price import Price
from domain.Store import Store
from utils.Observable import Subject, Observer


class GoodStore(Subject):
    id: int = 0
    name: str = ''
    price: Price = None
    store: Store = None
    prices: List[Price] = []

    def __init__(self, id: int, name: str, price: Price, store: Store):
        super().__init__()
        self.id = id
        self.name = name
        self.price = price
        self.store = store
        self.prices.append(price)

    def attach(self, observer: Observer) -> None:
        super().attach(observer)

    def detach(self, observer: Observer) -> None:
        super().detach(observer)

    def notify(self) -> None:
        super().notify()
