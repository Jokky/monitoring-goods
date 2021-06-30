from typing import Optional, List

from domain.Store import Store
from repository.Repository import Repository, T


class StoreRepository(Repository[Store]):
    __stores: List[Store] = []

    def __init__(self):
        super().__init__()
        self.__stores = [
            Store(1, 'Eldorado'),
            Store(2, 'MVideo'),
            Store(3, 'DNS')
        ]

    def find_all(self) -> List[T]:
        return self.__stores

    def find(self, item_id) -> Optional[T]:
        return list(filter(lambda s: s.id == item_id, self.__stores))[0]

    def find_kv(self, key: str, value: type(object)) -> Optional[T]:
        existAttr: bool = hasattr(Store, key)

        if not existAttr:
            return None

        return list(filter(lambda store: store.__getattribute__(key) == value, self.__stores))[0]

    def update(self, item: T) -> bool:
        positionStore: int = [i for i, s in enumerate(self.__stores) if s.id == item.id][0]
        self.__stores[positionStore] = item
        return True

    def delete(self, item: T) -> bool:
        self.__stores.remove(item)
        return True

    def add(self, item: T) -> bool:
        self.__stores.append(item)
        return True