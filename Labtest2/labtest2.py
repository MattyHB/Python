def stringify(items: list) -> str:
    string = ':'
    for item in items:
        string += '<{}>:'.format(item)
    return string

def select(items: list, key: str) ->list:
    current = 0
    final = []
    for i in items:
        selectDict = items[current]
        if key in selectDict:
            val = str(selectDict[key])
            final.append(val)
            current += 1
        else:
            current += 1
    return final
# - Tests - 
def test_Stringify():
    assert stringify(['a','b','c']) == ':<a>:<b>:<c>:'
    assert stringify([]) == ':'

def test_select():
    assert select([{'a': 'cat', 'b': 'dog'},{'a': 'gerbil', 'b': 'pig'}], 'b') == ['dog','pig']
    assert select([{'a': 'cat', 'c': 'dog'},{'a': 'gerbil', 'b': 'pig'}], 'b') == ['pig']