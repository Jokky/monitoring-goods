from __future__ import annotations
from abc import abstractmethod, ABC
from typing import List, TypeVar, Generic

T = TypeVar('T')


class Observer(Generic[T]):
    @abstractmethod
    def update(self, subject: T) -> None:
        pass


class Subject(ABC):
    _observers: List[T] = []

    @abstractmethod
    def attach(self, observer: T) -> None:
        self._observers.append(observer)

    @abstractmethod
    def detach(self, observer: T) -> None:
        self._observers.remove(observer)

    @abstractmethod
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
