from domain.Price import Price
from domain.Store import Store


class GoodStore:
    id: int = 0
    name: str = ''
    price: Price = None
    store: Store = None

    def __init__(self, id: int, name: str, price: Price, store: Store):
        self.id = id
        self.name = name
        self.price = price
        self.store = store
