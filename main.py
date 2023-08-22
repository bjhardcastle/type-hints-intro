from __future__ import annotations
import os

from typing import Dict, Iterable, Literal, TypeVar, Any, Protocol, Union
import pathlib

name: str = 'Ben'
name: int = 5

names_to_ages: Dict[str, dict[str, Any]] = {'Ben': '5'}

Dictionary = Union[str, int]

class WithName(Protocol):
    def name(self):
        pass

class MyClass:

    data: tuple[int, ...]

    def __init__(self, *data: int) -> None:
        self.data = data
        
    def __contains__(self, value: Any) -> bool:
        return True
    
    def __iter__(self):
        return iter(self.data)
    
    def name(self) -> str:
        return str(self.data)
    
class YourClass(tuple):
    def __str__(self):
        return super().__str__() + 'extra'
    def __le__(self, other):
        if self.data[0] < other.data[0]:
            return True
        return False
    
    def name(self) -> str:
        return str(self.data)
    
print(YourClass([3,4,5]))

m = MyClass([3,4,5])

for _ in m:
    print(_)


def hail(user: Literal[5, 'Ben', 'Corbett']) -> None:
    """
    user: str
    """
    print(user.name())
    os.path

hail(6)


hail(YourClass([1,2,3]))

# hail(name) # type: ignore

# print(2)
# print('2')
# print()