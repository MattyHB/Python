class Date:
    def __init__(self, year: int, month:int, day:int):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '{}-{:02}-{:02}'.format(self.year , self.month, self.day)

    def makeDate(self) -> (int, int, int):
        return (self.year, self.month, self.day)

    def getYear(self) -> int:
        return self.year

    def getMonth(self) -> int:
        return self.month

    def getDay(self) -> int:
        return self.day

    def addMonths(self, months: int) -> (int,int,int):
        newYear = self.year + (self.month + months -1) // 12 
        newMonth = (self.month + months -1) % 12 + 1
        newDay = self.day
        newDate = Date(newYear, newMonth, newDay)
        return newDate

# ----- Test Data -----

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
    assert str(d) == "2017-11-01"

def test_addMonths():
    d = Date(2017, 11, 1)

    newDate = d.addMonths(2)
    assert newDate.getYear() == 2018
    assert newDate.getMonth() == 1
    
    newDate = d.addMonths(3)
    assert newDate.getYear() == 2018
    assert newDate.getMonth() == 2

    newDate = d.addMonths(0)
    assert newDate.getYear() == 2017
    assert newDate.getMonth() == 11

    newDate = d.addMonths(1)
    assert newDate.getYear() == 2017
    assert newDate.getMonth() == 12