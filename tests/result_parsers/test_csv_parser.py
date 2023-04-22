from prompted.result_parsers import CsvParser


def test_instance_create():
    instance = CsvParser()
    assert instance is not None


def test_parse():
    instance = CsvParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
test1,test2,test3
1,2,3
4,5,6
```
Test Line 3 
    ''')

    assert len(result) == 1
    assert result[0][0]["test1"] == "1"


def test_parse_multiple_jsons():
    instance = CsvParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
test1,test2,test3
1,2,3
4,5,6
```
Test Line 3 
```
test4,test5,test6
7,8,9
10,11,12
```
Test Line 4
    ''')

    assert len(result) == 2
    assert result[0][0]["test1"] == "1"
    assert result[1][0]["test4"] == "7"


def test_parse_with_not_ended_code():
    instance = CsvParser()
    result = instance.parse('''
Test Line 1
Test Line 2
```
test1,test2,test3
1,2,3
4,5,6
```
Test Line 3 
```
test4,test5,test6
7,8,9
10,11,12
    ''')

    assert len(result) == 2
    assert result[0][0]["test1"] == "1"
    assert result[1][0]["test4"] == "7"
