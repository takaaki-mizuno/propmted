import json
from typing import Any, List

from .code_parser import CodeParser


class JsonParser(CodeParser):

    def parse(self, result: str) -> List[Any]:
        codes = super().parse(result)
        _result = []
        for code in codes:
            try:
                _result.append(json.loads(code))
            except json.JSONDecodeError:
                # Just ignore the code if it is not a valid json
                pass

        return _result
