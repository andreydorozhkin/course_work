from typing import TypeVar, Generic, List
from heapq import heappush, heappop


T = TypeVar('T')


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # false для пустого контейнейра

    def push(self, item: T) -> None:
        heappush(self._container, item)  # включить по приоритету

    def pop(self) -> T:
        return heappop(self._container)  # выключить по приоритету

    def __repr__(self) -> str:
        return repr(self._container)