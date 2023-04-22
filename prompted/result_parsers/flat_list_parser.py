import re

from .base_parser import BaseParser
from .results import ListResult


class FlatListParser(BaseParser):

    def __init__(self):
        self.regex_line_detector = re.compile(r'^(\s*)([-*+]\s+)(.*)$')

    def parse(self, result: str) -> ListResult:
        _lines = self.convert_into_lines(result)
        _result = ListResult()

        # strip head and tail empty lines
        while _lines and not _lines[0].strip():
            _lines.pop(0)
        while _lines and not _lines[-1].strip():
            _lines.pop()

        while _lines:
            line = _lines.pop(0)
            match = self.regex_line_detector.match(line)
            if not match:
                continue
            _result.append(match.group(3))

        return _result
