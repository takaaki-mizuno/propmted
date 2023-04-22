import re
from typing import List

from .base_parser import BaseParser
from .results import ListResult, ListRowResult


class NestedListParser(BaseParser):

    def __init__(self):
        self.regex_line_detector = re.compile(r'^(\s*)([-*+]\s+)(.*)$')

    def parse(self, result: str) -> ListResult:
        _lines = self.convert_into_lines(result)

        # function to parse nested lines recursively
        def parse_lines(lines: List[str],
                        indent: int = 0) -> List[ListRowResult]:
            _result: List[ListRowResult] = []
            while lines:
                line = lines.pop(0)
                match = self.regex_line_detector.match(line)
                if not match:
                    continue
                item_indent = len(match.group(1))
                item_text = match.group(3)

                if item_indent < indent:
                    lines.insert(0, line)
                    return _result
                elif item_indent > indent:
                    lines.insert(0, line)
                    child_items = parse_lines(lines, indent=item_indent)
                    _result[-1].set_children(child_items)
                else:
                    _result.append(ListRowResult(item_text, []))

            return _result

        return ListResult(parse_lines(_lines))
