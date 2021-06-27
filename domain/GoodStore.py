from domain.Price import Price
from domain.Store import Store


class GoodStore:
    def __init__(self, name: str, price: Price, store: Store):
        self.name = name
        self.price = price
        self.store = store
