from __future__ import annotations

import asyncio
from abc import abstractmethod, ABC
from typing import List, TypeVar, Generic

T = TypeVar('T')


class Observer(Generic[T]):
    @abstractmethod
    async def update(self, subject: T) -> None:
        pass


class Subject(ABC):
    _observers: List[Observer] = []

    def __init__(self):
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    @abstractmethod
    def notify(self) -> None:
        for observer in self._observers:
            asyncio.run(observer.update(self))
