from typing import Optional, List

from domain.Good import Good
from repository.Repository import Repository


class RedisPgGoodStoreRepository(Repository[Good]):
    def __init__(
        self,
        redis_good_repository: Repository[Good],
        pg_good_repository: Repository[Good],
    ):
        super().__init__()
        self.redis_good_repository = redis_good_repository
        self.pg_good_repository = pg_good_repository

    def find_all(self) -> List[Good]:
        redis_goods = self.redis_good_repository.find_all()

        if len(redis_goods) > 0:
            return redis_goods

        return self.pg_good_repository.find_all()

    def find(self, item_id) -> Optional[Good]:
        redis_good = self.redis_good_repository.find(item_id)

        if redis_good is not None:
            return redis_good

        return self.pg_good_repository.find(item_id)

    def find_kv(self, key: str, value: type(object)) -> Optional[Good]:
        redis_good = self.redis_good_repository.find_kv(key, value)

        if redis_good is not None:
            return redis_good

        return self.pg_good_repository.find_kv(key, value)

    def update(self, item: Good) -> bool:
        self.redis_good_repository.update(item)
        self.pg_good_repository.update(item)

        return True

    def delete(self, item: Good) -> bool:
        self.redis_good_repository.delete(item)
        self.pg_good_repository.delete(item)

        return True

    def add(self, item: Good) -> bool:
        self.redis_good_repository.add(item)
        self.pg_good_repository.add(item)

        return True
