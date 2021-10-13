class Room:
    """
    This class represents an adventure game.
    """
    def __init__(self, description, north, east, south, west):
        """Create an adventure"""
        x = 0
        self.description = ""
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    my_list = []
    my_room = Room("West Hall", 1, 3, 5, 6)
    my_list.append(my_room)

    my_room = Room("Bedroom", None, 2, 0, None)
    my_list.append(my_room)

    my_room = Room("Kitchen", None, None, 3, 0)
    my_list.append(my_room)

    my_room = Room("East Hall", 2, None, 4, 0)
    my_list.append(my_room)

    my_room = Room("Bathroom", 3, None, None, 5)
    my_list.append(my_room)

    my_room = Room("Bedroom", 0, 4, None, None)
    my_list.append(my_room)

    my_room = Room("Porch", None, 0, None, None)
    my_list.append(my_room)

    current_room = 0
    print(my_list [current_room].description)


main()
