from typing import List

from .base_parser import BaseParser


class CodeParser(BaseParser):

    def parse(self, result: str) -> List[str]:
        _lines = self.convert_into_lines(result)
        _result = []

        current_code = ""
        in_the_code = False
        while _lines:
            line = _lines.pop(0)
            if line.startswith("```"):
                if in_the_code:
                    _result.append(current_code)
                    in_the_code = False
                    current_code = ""
                else:
                    in_the_code = True
                    current_code = ""
            else:
                if in_the_code:
                    current_code += line + "\n"

        # if prompt code section is not closed, add it to the result
        if in_the_code:
            _result.append(current_code)

        return _result
