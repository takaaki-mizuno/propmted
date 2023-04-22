from typing import Any, List


class BaseParser(object):

    def parse(self, result: str) -> Any:
        raise NotImplementedError

    # strip head and tail empty lines
    @staticmethod
    def strip_result_lines(_lines: List[str]) -> List[str]:
        while _lines and not _lines[0].strip():
            _lines.pop(0)
        while _lines and not _lines[-1].strip():
            _lines.pop()

        return _lines

    def convert_into_lines(self, result: str) -> List[str]:
        _lines = result.split('\n')
        return self.strip_result_lines(_lines)
