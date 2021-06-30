from typing import Optional, List

from domain.GoodStore import GoodStore
from repository.Repository import Repository


class RedisPgGoodStoreRepository(Repository[GoodStore]):
    def __init__(
        self,
        redis_good_store_repository: Repository[GoodStore],
        pg_good_store_repository: Repository[GoodStore],
    ):
        super().__init__()
        self.redis_good_store_repository = redis_good_store_repository
        self.pg_good_store_repository = pg_good_store_repository

    def find_all(self) -> List[GoodStore]:
        redis_good_stores = self.redis_good_store_repository.find_all()

        if len(redis_good_stores) > 0:
            return redis_good_stores

        return self.pg_good_store_repository.find_all()

    def find(self, item_id) -> Optional[GoodStore]:
        redis_good_store = self.redis_good_store_repository.find(item_id)

        if redis_good_store is not None:
            return redis_good_store

        return self.pg_good_store_repository.find(item_id)

    def find_kv(self, key: str, value: type(object)) -> Optional[GoodStore]:
        redis_good_store = self.redis_good_store_repository.find_kv(key, value)

        if redis_good_store is not None:
            return redis_good_store

        return self.pg_good_store_repository.find_kv(key, value)

    def update(self, item: GoodStore) -> bool:
        self.redis_good_store_repository.update(item)
        self.pg_good_store_repository.update(item)

        return True

    def delete(self, item: GoodStore) -> bool:
        self.redis_good_store_repository.delete(item)
        self.pg_good_store_repository.delete(item)

        return True

    def add(self, item: GoodStore) -> bool:
        self.redis_good_store_repository.add(item)
        self.pg_good_store_repository.add(item)

        return True
