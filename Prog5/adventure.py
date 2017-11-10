# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# File: adventure.py
# Author: Matthew Beals User ID: Mbeal872 Class: CPS 110
# Desc: This program is a text adventure game based on the 
# floor plan of the original house of Dr. Schaub. 
# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
class Location:
    def __init__(self, descripion: str, items: list ):
        self.description = descripion
        self.items = items
        
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    
    def __repr__(self):
        return self.description

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
    
    def look(self) -> str:
        return "You are " + str(self.loc) + "."
        
    def go(self, dir: str) -> str:
        if dir == 's' and self.loc.south != None:
            self.loc = self.loc.south
        elif dir == 'n'and self.loc.north != None:
            self.loc = self.loc.north
        elif dir == 'w'and self.loc.west != None:
            self.loc = self.loc.west
        elif dir == 'e'and self.loc.east != None:
            self.loc = self.loc.east
        else:
            return "You can't go that way."
        return self.look()