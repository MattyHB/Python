class Ball:
    def __init__(self, color: str, size: int):
        self.color = color
        self.size = size
    def __str__(self):
        return "{0} / {1}".format(self.color, self.size)
    def __repr__(self):
        return "{0} / {1}".format(self.color, self.size)

class BallBag:
    def __init__(self):
        self.bag = {}

    def __str__(self):
        return self.bag

    def __repr__(self):
        for item in self.bag:
            print(self.bag[item] + " / " + self.bag.key)

    def addBall(self, color: str, size: int):
        keyVal = Ball(color, size)
        self.bag[color] = size 

    def findBall(self, color:str):
        if color in self.bag:
            print(self.bag[color])
        else:
            return None

    def getBalls(self) -> str:
        for item in self.bag:
            print(self.bag[item],"/", self.bag)

