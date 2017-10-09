num = 3 
def countdown(fromVal):
    for i in range(fromVal, 0, -1):
        print(str(i) + "...")

def mergeLists(l1: list, l2: list) -> list:
    result = l1
    for item in l2:
        if not (item in result):
            result = result + [item]

    return result    

def test_mergeLists():
    assert mergeLists([1, 2, 3], [2, 3]) == [1, 2, 3]
    assert mergeLists([1, 2, 3], [4, 3]) == [1, 2, 3, 4]

def findZero(items: str) -> int:
    lst = items.split(',')
    for i in range(len(lst)):
        if lst[i] == '0':
            return i

    return -1

def test_findZero():
    assert findZero('12,532,0,36,5') == 2
    assert findZero('1,52,10,') == -1

def main():
    

    print("Counting down from", num, "to 1...")

    countdown(num)

if __name__ == "__main__":
    #main()
    #test_mergeLists()
    test_findZero()