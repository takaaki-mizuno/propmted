from prompted.result_parsers import JsonParser


def test_instance_create():
    instance = JsonParser()
    assert instance is not None


def test_parse():
    instance = JsonParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
{
  "name": "John",
  "age": 40,
  "cars": [
    "Ford",
    "Toyota",
    "Fiat"
  ]
}
```
Test Line 3 
    ''')

    assert len(result) == 1
    assert result[0]["name"] == "John"


def test_parse_multiple_jsons():
    instance = JsonParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
{
  "name": "John",
  "age": 40,
  "cars": [
    "Ford",
    "Toyota",
    "Fiat"
  ]
}
```
Test Line 3 
```
[
  "item1",
  "item2"
]
```
Test Line 4
    ''')

    assert len(result) == 2
    assert result[0]["name"] == "John"
    assert result[1][0] == "item1"


def test_parse_with_not_ended_code():
    instance = JsonParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
{
  "name": "John",
  "age": 40,
  "cars": [
    "Ford",
    "Toyota",
    "Fiat"
  ]
}
```
Test Line 3 
```
[
  "item1",
  "item2"
]
    ''')

    assert len(result) == 2
    assert result[0]["name"] == "John"
    assert result[1][0] == "item1"


def test_parse_with_not_parsable_code():
    instance = JsonParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
def test():
    return "Hello World"
```
Test Line 3 
```
[
  "item1",
  "item2"
]
    ''')

    assert len(result) == 1
    assert result[0][0] == "item1"
