from pathlib import Path
from typing import Any, Dict, Optional, Union

from jinja2 import Environment, FileSystemLoader, Template

from prompted.models import OpenAI
from prompted.result_parsers import (BaseParser, CsvParser, FlatListParser,
                                     JsonParser, NestedListParser,
                                     RawTextParser)


class Prompted(object):

    class ResultType:
        Text = "text"
        FlatList = "flat_list"
        NestedList = "nested_list"
        CSV = "csv"
        JSON = "json"

    def __init__(self, template_directory: Union[str, Path], model_name: str):
        self._template_path = template_directory
        self._model_name = model_name
        self.check_template_directory()
        self._template_engine = self.load_template_engine()
        self._model = None
        self.load_model()

    def check_template_directory(self) -> None:
        template_directory = Path(self._template_path)
        if not template_directory.exists():
            raise ValueError(
                f"Template directory {template_directory} does not exist")

    def load_template_engine(self) -> Environment:
        environment = Environment(loader=FileSystemLoader(self._template_path,
                                                          encoding='utf8'),
                                  autoescape=True)

        return environment

    def load_model(self) -> None:
        if self._model_name == "gpt3.5":
            self._model = OpenAI(model="gpt-3.5-turbo")
        else:
            raise ValueError(f"Model {self._model_name} not supported")

    def get_template(self, template_name: str) -> Template:
        template = self._template_engine.get_template(f"{template_name}.tmpl")
        return template

    def complete_row(self, template_name: str, values: Dict[str, Any]) -> str:
        template = self.get_template(template_name)
        prompt = template.render(values)

        result = self._model.complete(prompt)
        return result

    def get_parser(self, result_type: str) -> Optional[BaseParser]:
        if result_type == self.ResultType.Text:
            return RawTextParser()
        elif result_type == self.ResultType.FlatList:
            return FlatListParser()
        elif result_type == self.ResultType.NestedList:
            return NestedListParser()
        elif result_type == self.ResultType.CSV:
            return CsvParser()
        elif result_type == self.ResultType.JSON:
            return JsonParser()
        else:
            raise ValueError(f"Result type {result_type} not supported")

    def complete(self, template_name: str, values: Dict[str, Any],
                 result_type: str) -> str:
        template = self.get_template(template_name)
        prompt = template.render(values)
        parser = self.get_parser(result_type)

        result = self._model.complete(prompt)
        return parser.parse(result)
