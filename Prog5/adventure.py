class Location:

class World:    
    def __init__(self):
        diningroom = Location('in a cheerful dining room', [])
        kitchen = Location('in a warm, inviting kitchen', [])
        livingroom = Location('in a comfortable living room', [])
        mbedroom = Location('in the master bedroom', [])
        hallway = Location('in a small hallway', [])
        cbedroom = Location('in another bedroom', [])
        bathroom = Location('in a small bathroom', [])

        # Set up exits
        diningroom.west = kitchen
        diningroom.east = livingroom
        diningroom.south = hallway

        kitchen.east = diningroom

        livingroom.west = diningroom
        livingroom.south = hallway

        mbedroom.east = hallway
        mbedroom.north = kitchen

        hallway.west = mbedroom
        hallway.east = cbedroom
        hallway.north = diningroom
        hallway.south = bathroom

        cbedroom.west = hallway

        bathroom.north = hallway

        self.loc = diningroom
        self.items = []
    
    def go(self, dir: str) -> str:
        try:
            if dir == 's'
                self.loc = self.loc.south
            elif dir == 'n':
                self.loc = self.loc.north
            elif dir == 'w':
                self.loc = self.loc.west
            elif dir == 'e':
                self.loc = slef.loc.east
        except Exception as e:
            return "You can’t go that way."
        