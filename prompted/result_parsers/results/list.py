from typing import List


class ListRowResult(object):
    _item: str
    _children: List["ListRowResult"]

    def __init__(self, item: str, children: List["ListRowResult"] = None):
        self._item = item or []
        self._children = children

    def __str__(self):
        return self._item

    def __repr__(self):
        return self._item

    def set_children(self, children: List["ListRowResult"]):
        self._children = children

    @property
    def item(self) -> str:
        return self._item

    @property
    def children(self) -> List["ListRowResult"]:
        return self._children


class ListResult(object):

    def __init__(self, data: List[ListRowResult] = None):
        self._data = data or []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def append(self, item: str):
        return self._data.append(ListRowResult(item))

    @property
    def data(self) -> List[ListRowResult]:
        return self._data
