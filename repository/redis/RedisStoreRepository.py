from typing import Optional, List

from domain.Store import Store
from repository.Repository import Repository, T


class RedisStoreRepository(Repository[Store]):
    def find_all(self) -> List[T]:
        pass

    def find(self, item_id) -> Optional[T]:
        pass

    def find_kv(self, key: str, value: type(object)) -> Optional[T]:
        pass

    def update(self, item: T) -> bool:
        pass

    def delete(self, item: T) -> bool:
        pass

    def add(self, item: T) -> bool:
        pass