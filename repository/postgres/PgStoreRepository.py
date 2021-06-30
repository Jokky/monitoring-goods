from typing import Optional, List

from domain.Store import Store
from repository.Repository import Repository


class PgStoreRepository(Repository[Store]):
    def find_all(self) -> List[Store]:
        pass

    def find(self, item_id) -> Optional[Store]:
        pass

    def find_kv(self, key: str, value: type(object)) -> Optional[Store]:
        pass

    def update(self, item: Store) -> bool:
        pass

    def delete(self, item: Store) -> bool:
        pass

    def add(self, item: Store) -> bool:
        pass