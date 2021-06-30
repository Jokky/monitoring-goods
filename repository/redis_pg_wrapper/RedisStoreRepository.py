from typing import Optional, List

from domain.Store import Store
from repository.Repository import Repository


class RedisStoreRepository(Repository[Store]):
    def __init__(
        self,
        redis_store_repository: Repository[Store],
        pg_store_repository: Repository[Store],
    ):
        super().__init__()
        self.redis_store_repository = redis_store_repository
        self.pg_store_repository = pg_store_repository

    def find_all(self) -> List[Store]:
        redis_stores = self.redis_store_repository.find_all()

        if len(redis_stores) > 0:
            return redis_stores

        return self.pg_store_repository.find_all()

    def find(self, item_id) -> Optional[Store]:
        redis_store = self.redis_store_repository.find(item_id)

        if redis_store is not None:
            return redis_store

        return self.pg_store_repository.find(item_id)

    def find_kv(self, key: str, value: type(object)) -> Optional[Store]:
        redis_store = self.redis_store_repository.find_kv(key, value)

        if redis_store is not None:
            return redis_store

        return self.pg_store_repository.find_kv(key, value)

    def update(self, item: Store) -> bool:
        self.redis_store_repository.update(item)
        self.pg_store_repository.update(item)

        return True

    def delete(self, item: Store) -> bool:
        self.redis_store_repository.delete(item)
        self.pg_store_repository.delete(item)

        return True

    def add(self, item: Store) -> bool:
        self.redis_store_repository.add(item)
        self.pg_store_repository.add(item)

        return True
