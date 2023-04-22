import csv
import io
from typing import Any, Dict, List

from .code_parser import CodeParser
from .results import TableResult


class CsvParser(CodeParser):

    def parse(self, result: str) -> List[Any]:
        codes = super().parse(result)
        _result = []
        for code in codes:
            try:
                csv_file = io.StringIO(code)
                csv_reader = csv.DictReader(csv_file)
                data_list = [row for row in csv_reader]
                _result.append(TableResult.from_list(data_list))
            except csv.Error as e:
                pass

        return _result
