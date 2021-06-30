from abc import abstractmethod
from typing import TypeVar, Generic, List, Type, Optional

from domain.Good import Good

T = TypeVar('T')


class Repository(Generic[T]):
    def __init__(self):
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        pass

    @abstractmethod
    def find(self, item_id) -> Optional[T]:
        pass

    @abstractmethod
    def find_kv(self, key: str, value: type(object)) -> Optional[T]:
        pass

    @abstractmethod
    def update(self, item: T) -> bool:
        pass

    @abstractmethod
    def delete(self, item: T) -> bool:
        pass

    @abstractmethod
    def add(self, item: T) -> bool:
        pass
