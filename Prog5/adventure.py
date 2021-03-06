# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# File: adventure.py
# Author: Matthew Beals User ID: Mbeal872 Class: CPS 110
# Desc: This program is a text adventure game based on the 
# floor plan of the original house of Dr. Schaub. 
# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
class Location:
    def __init__(self, description: str, items: list ):
        self.description = description
        self.items = items
        
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    
    def __repr__(self):
        return self.description

class Item:
    def __init__(self, description: str, movable: bool, extDescription:str):
        self.description = description
        self.movable = movable
        self.extDescription = extDescription

    def __repr__(self):
        return self.description


class World:    
    def __init__(self):
        diningroom = Location('in a cheerful dining room', 
                                [Item('keys', True, 'The keys jingle as you examine them.'), 
                                Item('a small child', True, "The child appears to be pulling CD's out of the stack.")])
        kitchen = Location('in a warm, inviting kitchen', 
                                [Item('a white microwave', True, "Mmmm... something inside smells yummy!"), 
                                Item('a large refrigerator', False, "There is a large padlock around the refrigerator.")])
        livingroom = Location('in a comfortable living room', 
                                [Item('a grand piano', False, 'The piano is dusty.'), 
                                Item('a book of Bach preludes', True, 'Someone has marked up one of the preludes using a blue marker.')])
        mbedroom = Location('in the master bedroom', 
                                [Item('an alarm clock', True, 'The clock is set for 3 a.m.'), 
                                Item('a small crib', False, 'The crib is empty.')])
        hallway = Location('in a small hallway', [])
        cbedroom = Location('in another bedroom', 
                                [Item('a well-worn teddy bear', True, 'One of the ears is missing.')])
        bathroom = Location('in a small bathroom', 
                                [Item('a gold key', True, 'The key is glowing.')])

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
        self.inventory = [Item('a green basket', True, 'The basket has a broken handle.')]
    
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

    def carrying(self) -> str:
        invitem = ''
        if self.inventory != []:
            for i in range(len(self.inventory)):
                invitem += str(self.inventory[i])
                if (i == len(self.inventory) -1):
                    invitem += "."
                    return 'You are carrying: ' + invitem
                else:
                    invitem += ', '   
                    
        else:
            return 'You aren’t carrying anything.'

    def lookaround(self) -> str:
        rooomItemz = ''
        for i in range(len(self.loc.items)):
            rooomItemz += str(self.loc.items[i])
            if (i == len(self.loc.items) - 1):
                rooomItemz += '.'
            else:
                rooomItemz += ', '
        return "You see: " + rooomItemz

    def examine(self, descr: str) -> str:
        for i in self.loc.items:
            if descr in i.description:
                return i.extDescription

        for i in self.inventory:
            if descr in i.description:
                return i.extDescription

        return "There is no " + descr + " here."

    def take(self, descr: str) -> str:
        
        for i in self.loc.items:
            if descr in i.description and i.movable == True:
                self.inventory.append(i)
                self.loc.items.remove(i)
                return "You pick up " + str(self.inventory[1]) + '. ' + self.carrying()
            
            if descr in i.description and i.movable == False:
                return "You can't take that!"    
        return 'There is no ' + descr + " here."

    def drop(self, descr: str) -> str:

        for i in self.inventory:
            if descr in i.description:
                self.loc.items.append(i)
                self.inventory.remove(i)
                return "You drop " + str(i) + '. ' + self.carrying()
        return "You are not carrying " + descr + "."