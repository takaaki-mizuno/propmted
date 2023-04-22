import os
from pathlib import Path
from unittest import mock

from prompted import Prompted


@mock.patch.dict(os.environ, {"OPENAI_API_KEY": "test"})
def test_instance_create():
    instance = Prompted(Path("tests/templates"), "gpt3.5")
    assert instance is not None


@mock.patch.dict(os.environ, {"OPENAI_API_KEY": "test"})
def test_get_template():
    instance = Prompted(Path("tests/templates"), "gpt3.5")
    template = instance.get_template("test_prompt")

    assert template is not None


@mock.patch.dict(os.environ, {"OPENAI_API_KEY": "test"})
def test_get_prompt(mocker):

    def complete(self, prompt: str) -> str:
        return prompt

    mocker.patch("prompted.models.openai.OpenAI.complete", complete)
    instance = Prompted(Path("tests/templates"), "gpt3.5")
    result = instance.complete_row("test_prompt", {
        "data_1": "test1",
        "data_2": "test2"
    })

    assert result == "test1 - test2"


@mock.patch.dict(os.environ, {"OPENAI_API_KEY": "test"})
def test_get_prompt(mocker):

    def complete(self, prompt: str) -> str:
        return """
test
- test1
- test2
        """

    mocker.patch("prompted.models.openai.OpenAI.complete", complete)
    instance = Prompted(Path("tests/templates"), "gpt3.5")
    result = instance.complete("test_prompt", {
        "data_1": "test1",
        "data_2": "test2"
    },
                               result_type=Prompted.ResultType.FlatList)

    assert len(result) == 2
    assert str(result[0]) == "test1"
    assert str(result[1]) == "test2"
