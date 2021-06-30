from typing import Optional, List

from domain.GoodStore import GoodStore
from repository.Repository import Repository


class PgGoodStoreRepository(Repository[GoodStore]):
    def find_all(self) -> List[GoodStore]:
        pass

    def find(self, item_id) -> Optional[GoodStore]:
        pass

    def find_kv(self, key: str, value: type(object)) -> Optional[GoodStore]:
        pass

    def update(self, item: GoodStore) -> bool:
        pass

    def delete(self, item: GoodStore) -> bool:
        pass

    def add(self, item: GoodStore) -> bool:
        pass
