from dataclasses import dataclass
from typing import List


@dataclass
class Item():
    box: tuple = None
    text: str = None
    def uuid(self):
        return f'{self.box} {self.text}'

@dataclass
class Case():
    acction:str
    connet:str


class Stack:
    def __init__(self):
        self._data: List[Item] = []

    def push(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]

    def __contains__(self, item: Item):
        for _item in self._data:
            if _item.uuid() == item.uuid():
                return True
        return False
    def contains(self,text):
        for _item in self._data:
            if _item.text==text:
                return _item
        return None

    def pop_to_item(self, item: Item):
        if len(self._data) <= 2:
            return None
        for _item in self._data:

            if _item.uuid() == item.uuid():
                while self.top().uuid() != _item.uuid():
                    self.pop()
                return _item
        return None
    def __iter__(self):
        return self._data.__iter__()