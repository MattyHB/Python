class Clock:
    def __init__(self, hours: int, minutes:int ):
        self.hours = hours
        self.minutes = minutes

    def getSeconds(self) -> int:
        return self.minutes * 60 + self.hours * 60 * 60
   
    def addMin(self, minutes:int):
        self.hours = (self.hours + (self.minutes + minutes) // 60)
        self.minutes = (self. minutes + minutes) % 60

    def addHours(self, hours:int):
        self.addMin(hours * 60)

    def __str__(self) -> str:
        return "{}:{:02}".format(self.hours, self.minutes)




# Tests
def test_Clock_constructor():
    c = Clock(5, 15)
    assert c.hours == 5
    assert c.minutes == 15

def test_getSeconds():
    c1 = Clock(2,10)
    c2 = Clock(0,30)
    assert c1.getSeconds() == 2 * 60 * 60 + 10 * 60
    assert c2.getSeconds() == 30 * 60

def test_addMin():
    c = Clock(5, 45)
    c.addMin(120)
    c.hours == 7
    c.minutes == 45
    
def test_addHours():
    c = Clock(5, 5)
    c.addHours(1)
    assert c.hours == 6
    assert c.minutes == 5

def test_toString():
    c = Clock(10,5)
    assert str(c) == '10:05'
    