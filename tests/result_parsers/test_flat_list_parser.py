from prompted.result_parsers import FlatListParser


def test_instance_create():
    instance = FlatListParser()
    assert instance is not None


def test_parse():
    instance = FlatListParser()
    result = instance.parse('''
Test Line 1
Test Line 2

- item1
-  item2
    - item2-1
- item3

Test Line 3 

- item4
    ''')

    assert len(result) == 5
    assert result[0].item == 'item1'
    assert result[1].item == 'item2'
    assert result[2].item == 'item2-1'
    assert result[3].item == 'item3'
    assert result[4].item == 'item4'
