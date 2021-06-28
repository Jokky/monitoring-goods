from typing import List, Optional

from domain.Good import Good
from domain.GoodStore import GoodStore
from domain.Price import Price
from service.DifferentPercentGoodsPrice import DifferentPercentGoodsPrice
from service.StoreService import StoreService


class GoodService:
    __goods: List[Good] = []

    def __init__(self, good_service: StoreService, differentPercentGoodsPrice: DifferentPercentGoodsPrice):
        iphones = [
            GoodStore(1, 'iphone 11 pro max 256GB', Price(90000), good_service.get_store_by_id(1)),
            GoodStore(2, 'iphone 11 pro max white 256GB', Price(81000), good_service.get_store_by_id(2)),
            GoodStore(3, 'iphone 11 pro max black 256GB', Price(79000), good_service.get_store_by_id(3))
        ]

        iphone = Good(1, iphones)
        iphone.attach(differentPercentGoodsPrice)

        self.__goods = [
            iphone
        ]

    def get_good_by_id(self, good_id: int) -> Optional[Good]:
        for good in self.__goods:
            if good.id == good_id:
                return good
        return None

    def get_goods(self) -> List[Good]:
        return self.__goods

    def get_good_store_by_id(self, good_id: int, good_store_id: int) -> Optional[GoodStore]:
        for good in self.__goods:
            if good.id == good_id:
                for good_store in good.good_stores:
                    if good_store.id == good_store_id:
                        return good_store

        return None

    def add_good_store(self, good_id: int, good_store: GoodStore) -> bool:
        goods: List[Good] = []
        for good in self.__goods:
            if good.id == good_id:
                good.good_stores.append(good_store)
            goods.append(good)

        self.__goods = goods

        return True

    def update_good_store(self, good_id: int, good_store: GoodStore) -> bool:
        goods: List[Good] = []
        for good in self.__goods:
            if good.id == good_id:
                for f_good_store in good.good_stores:
                    if f_good_store.id == good_store.id:
                        f_good_store.price = good_store.price
                        f_good_store.name = good_store.name
                good.notify()
            goods.append(good)

        self.__goods = goods

        return True
