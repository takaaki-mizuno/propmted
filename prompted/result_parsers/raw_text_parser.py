from .base_parser import BaseParser


class RawTextParser(BaseParser):

    def parse(self, result: str) -> str:
        return result
