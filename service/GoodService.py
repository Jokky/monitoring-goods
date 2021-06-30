import asyncio
from typing import List, Optional

from domain.Good import Good
from domain.GoodStore import GoodStore
from domain.Price import Price
from repository.Repository import Repository
from service.DifferentPercentGoodsPrice import DifferentPercentGoodsPrice
from service.StoreService import StoreService


class GoodService:
    def __init__(
        self,
        good_repository: Repository[Good],
        good_store_repository: Repository[GoodStore]
    ):
        self.good_repository = good_repository
        self.good_store_repository = good_store_repository

    def get_good_by_id(self, good_id: int) -> Optional[Good]:
        return self.good_repository.find_kv('id', good_id)

    def get_goods(self) -> List[Good]:
        return self.good_repository.find_all()

    def get_good_store_by_id(self, good_id: int, good_store_id: int) -> Optional[GoodStore]:
        for good_store in self.good_repository.find(good_id).good_stores:
            if good_store.id == good_store_id:
                return good_store

        return None

    def add_good_store(self, good_id: int, good_store: GoodStore) -> bool:
        self.good_store_repository.add(good_store)
        # self.good_repository.find(good_id).good_stores.append(good_store)
        return True

    def update_good_store(self, good_id: int, good_store: GoodStore) -> bool:
        good = self.good_repository.find(good_id)
        self.good_store_repository.update(good_store)
        # positionGoodStore = good.good_stores.index(good_store)
        #
        # good.good_stores = [
        #     *good.good_stores[0:positionGoodStore + 1],
        #     good_store,
        #     *good.good_stores[positionGoodStore + 1:len(good.good_stores)],
        # ]

        good.notify()

        return True
