from typing import Dict, List


class TableRowResult(object):

    def __init__(self, data: Dict[str, str]):
        self._data = data or {}

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index: str):
        return self._data[index]

    def add_cell(self, header: str, data: str):
        self._data[header] = data

    @property
    def data(self) -> Dict[str, str]:
        return self._data


class TableResult(object):

    @classmethod
    def from_list(cls, data: List[Dict[str, str]]):
        return cls([TableRowResult(row) for row in data])

    def __init__(self, data: List[TableRowResult] = None):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    @property
    def data(self) -> List[TableRowResult]:
        return self._data
