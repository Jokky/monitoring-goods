from typing import List, Optional

from domain.Good import Good
from domain.GoodStore import GoodStore
from repository.Repository import Repository, T
from service.DifferentPercentGoodsPrice import DifferentPercentGoodsPrice


class GoodRepository(Repository[Good]):
    __goods: List[Good] = []

    def __init__(self, good_store_repository: Repository[GoodStore]):
        super().__init__()
        good_stores = [
            good_store_repository.find(1),
            good_store_repository.find(2),
            good_store_repository.find(3),
            # GoodStore(1, 'iphone 11 pro max 256GB', Price(90000), store_service.get_store_by_id(1)),
            # GoodStore(2, 'iphone 11 pro max white 256GB', Price(81000), store_service.get_store_by_id(2)),
            # GoodStore(3, 'iphone 11 pro max black 256GB', Price(79000), store_service.get_store_by_id(3))
        ]

        good = Good(1, good_stores)
        good.attach(DifferentPercentGoodsPrice())
        self.__goods = [good]

    def find_all(self) -> List[Good]:
        return self.__goods

    def find_kv(self, key: str, value: type(object)):
        existAttr = hasattr(Good, key)

        if not existAttr:
            return None

        return list(filter(lambda good: good.__getattribute__(key) == value, self.__goods))[0]

    def find(self, item_id) -> Optional[Good]:
        goods = list(filter(lambda g: g.id == item_id, self.__goods))
        if len(goods) > 0:
            return goods.pop()

        return None

    def update(self, item: Good) -> bool:
        positionGood: int = [i for i, g in enumerate(self.__goods) if g.id == item.id][0]
        self.__goods[positionGood] = item
        return True

    def delete(self, item: Good) -> bool:
        self.__goods.remove(item)
        return True

    def add(self, item: T) -> bool:
        self.__goods.append(item)
        return True
