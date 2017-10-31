class Date:
    def __init__(self, year: int, month:int, day:int):
        self.year = year
        self.month = month
        self.day = day
    def makeDate(self) -> (int, int, int):
        return (self.year, self.month, self.day)

    def getYear(self) -> int:
        return self.year

    def getMonth(self) -> int:
        return self.month

    def getDay(self) -> int:
        return self.day

    def addMonths(self, months: int) -> (int, int, int):
        year = self.getYear()
        month = self.getMonth()
        day = self.getDay()

        addedMonths = (self.year + (self.month + months - 1) // 12,
                        ((self.month + months - 1) % 12 + 1),
                        self.day)
        return self.makeDate(addedMonths)

    def toString(self, date: (int, int, int)) -> str:
        return '{}-{:02}-{:02}'.format(self.year , self.month, self.day)

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
    d = Date(2017, 11 ,1)
    new = d.makeDate
    assert d.toString(new) == "2017-11-01"

def test_addMonths():
    d = Date(2017,11,1)
    newd = d.makeDate()
    
    newDate = d.addMonths(1)
    assert d.getYear(newDate) == 2017
    assert d.getMonth(newDate) == 12

    newDate = d.addMonths(2)
    assert d.getYear(newDate) == 2018
    assert d.getMonth(newDate) == 1