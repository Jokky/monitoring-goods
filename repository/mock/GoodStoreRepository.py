from typing import Optional, List

from domain.GoodStore import GoodStore
from domain.Price import Price
from domain.Store import Store
from repository.Repository import Repository, T


class GoodStoreRepository(Repository[GoodStore]):
    __good_stores: List[GoodStore] = []

    def __init__(self, store_repository: Repository[Store]):
        super().__init__()
        self.__good_stores = [
            GoodStore(1, 'iphone 11 pro max 256GB', Price(90000), store_repository.find(1)),
            GoodStore(2, 'iphone 11 pro max white 256GB', Price(81000), store_repository.find(2)),
            GoodStore(3, 'iphone 11 pro max black 256GB', Price(79000), store_repository.find(3))
        ]

    def find_all(self) -> List[T]:
        return self.__good_stores

    def find(self, item_id) -> Optional[T]:
        return list(filter(lambda gs: gs.id == item_id, self.__good_stores))[0]

    def find_kv(self, key: str, value: type(object)) -> Optional[T]:
        existAttr = hasattr(GoodStore, key)

        if not existAttr:
            return None

        return list(filter(lambda gs: gs.__getattribute__(key) == value, self.__good_stores))[0]

    def update(self, item: T) -> bool:
        positionGoodStore: int = [i for i, g in enumerate(self.__good_stores) if g.id == item.id][0]
        self.__good_stores[positionGoodStore] = item
        return True

    def delete(self, item: T) -> bool:
        self.__good_stores.remove(item)
        return True

    def add(self, item: T) -> bool:
        self.__good_stores.append(item)
        return True