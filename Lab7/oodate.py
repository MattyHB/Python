class Date:
    def __init__(self, year: int, month:int, day:int):
        self.year = year
        self.month = month
        self.day = day
    def makeDate(self) -> (int, int, int):
        return (year, month, day)

    def getYear(self) -> int:
        return self.year

    def getMonth(self) -> int:
        return self.month

    def getDay(self) -> int:
        return self.day

    def addMonths(self, months: int) -> (int, int, int):
        year = getYear(date)
        month = getMonth(date)
        day = getDay(date)

        return makeDate(self.year + (self.month + months - 1) // 12,
                        ((self.month + months - 1) % 12 + 1),
                        day)

    def toString(date: (int, int, int)) -> str:
        return "{}-{:02}-{:02}".format(date[0], date[1], date[2])

def test_Date_Constructor():
    d = Date(1997, 3, 12)
    assert d.year == 1997
    assert d.month == 3
    assert d.day == 12

def test_getYear():
    d = Date(1997, 3, 12)
    assert d.getYear() == 1997

def test_getMonth():
    d = Date(1997, 3, 12)
    assert d.getMonth() == 3

def test_getDay():
    d = Date(1997, 3, 12)
    assert d.getDay() == 12

def test_toString():
    date = makeDate(2017,11,1)
    assert toString(date) == "2017-11-01"

def test_addMonths():
    d = Date(2017,11,1)
    d.makeDate()
    newDate = addMonths(1)
    assert getYear(newDate) == 2017
    assert getMonth(newDate) == 12

    newDate = addMonths(2)
    assert getYear(newDate) == 2018
    assert getMonth(newDate) == 1