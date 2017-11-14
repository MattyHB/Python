def remove(lst: list, pos: int):
    n = pos
    while n < len(lst) -1:
        lst[n] = lst[n + 1]
        n += 1
    lst[-1] = None

def test_remove():
    lst = ['Turkey', 
           'Stuffing',
           'Cranberry sauce',
           'Green bean casserole',
           'Sweet potato crunch',
           'Pumpkin pie']

    remove(lst, 2)

    assert lst == ['Turkey', 
           'Stuffing',
           'Green bean casserole',
           'Sweet potato crunch',
           'Pumpkin pie',
           None]

    lst = [5, 10, 15]
    remove(lst, 0)
    assert lst == [10, 15, None]

    lst = [5]
    remove(lst, 0)
    assert lst == [None]
    
if __name__ == "__main__":
    test_remove()