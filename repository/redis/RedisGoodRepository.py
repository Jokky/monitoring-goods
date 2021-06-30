from typing import Optional, List

from domain.Good import Good
from repository.Repository import Repository


class RedisGoodRepository(Repository[Good]):
    def find_all(self) -> List[Good]:
        pass

    def find(self, item_id) -> Optional[Good]:
        pass

    def find_kv(self, key: str, value: type(object)) -> Optional[Good]:
        pass

    def update(self, item: Good) -> bool:
        pass

    def delete(self, item: Good) -> bool:
        pass

    def add(self, item: Good) -> bool:
        pass
