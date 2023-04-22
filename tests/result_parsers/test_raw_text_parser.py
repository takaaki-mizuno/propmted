from prompted.result_parsers import RawTextParser


def test_instance_create():
    instance = RawTextParser()
    assert instance is not None


def test_parse():
    instance = RawTextParser()
    result = instance.parse("Hello World")
    assert result == "Hello World"
