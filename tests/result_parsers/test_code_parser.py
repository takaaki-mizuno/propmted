from prompted.result_parsers import CodeParser


def test_instance_create():
    instance = CodeParser()
    assert instance is not None


def test_parse():
    instance = CodeParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
def test():
    return "Hello World"
```
Test Line 3 
    ''')

    assert len(result) == 1
    assert result[0] == 'def test():\n    return "Hello World"\n'


def test_parse_multiple_codes():
    instance = CodeParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
def test():
    return "Hello World"
```
Test Line 3 
```
def test_2():
    return "Hello World 2"
```
Test Line 4
    ''')

    assert len(result) == 2
    assert result[0] == 'def test():\n    return "Hello World"\n'
    assert result[1] == 'def test_2():\n    return "Hello World 2"\n'


def test_parse_with_not_ended_code():
    instance = CodeParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
def test():
    return "Hello World"
```
Test Line 3 
```
def test_2():
    return "Hello World 2"
    ''')

    assert len(result) == 2
    assert result[0] == 'def test():\n    return "Hello World"\n'
    assert result[1] == 'def test_2():\n    return "Hello World 2"\n'
