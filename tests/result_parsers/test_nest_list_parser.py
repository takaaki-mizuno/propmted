from prompted.result_parsers import NestedListParser


def test_instance_create():
    instance = NestedListParser()
    assert instance is not None


def test_parse():
    instance = NestedListParser()
    result = instance.parse('''
Test Line 1
Test Line 2

- item1
-  item2
    - item2-1
    - item2-2
      - item2-2-3
    - item2-3
- item3

Test Line 3 

- item4
  - item4-1
  - item4-2
    ''')

    assert len(result) == 4
    assert result[0].item == 'item1'
    assert len(result[0].children) == 0
    assert result[1].item == 'item2'
    assert len(result[1].children) == 3
    assert result[1].children[0].item == 'item2-1'
    assert len(result[1].children[0].children) == 0
    assert result[1].children[1].item == 'item2-2'
    assert len(result[1].children[1].children) == 1
    assert result[1].children[1].children[0].item == 'item2-2-3'
    assert len(result[1].children[1].children[0].children) == 0
    assert result[1].children[2].item == 'item2-3'
    assert len(result[1].children[2].children) == 0
    assert result[2].item == 'item3'
    assert len(result[2].children) == 0
    assert result[3].item == 'item4'
    assert len(result[3].children) == 2
    assert result[3].children[0].item == 'item4-1'
    assert len(result[3].children[0].children) == 0
    assert result[3].children[1].item == 'item4-2'
    assert len(result[3].children[1].children) == 0
