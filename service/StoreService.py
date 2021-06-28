from typing import List

from domain.Store import Store


class StoreService:
    __stores: List[Store] = []

    def __init__(self):
        self.__stores = [
            Store(1, 'Eldorado'),
            Store(2, 'MVideo'),
            Store(3, 'DNS')
        ]

    def get_store_by_id(self, store_id):
        return [store for store in self.__stores if store.id == store_id][0]

    def get_store_by_name(self, store_name):
        return [store for store in self.__stores if store.name == store_name][0]

    def get_stores(self):
        return self.__stores

    def add_store(self, store: Store):
        self.__stores.append(store)
