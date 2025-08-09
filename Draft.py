class House:
    #Consturctor/initialiser
    def __init__(self, num_rooms, colour, availability):
        self.set_num_room(num_rooms)
        self.set_colour(colour)
        self.set_availability(availability)

    #setter each attribute
    def set_num_room(self, num):
        if num >=1 and num <= 20:
            self.__num_room=num
        elif num < 1:
            self.__num_room = 1
        elif num > 20:
            self.__num_room = 20
    def set_colour(self, clr):
        if clr.lower() not in ['white', 'orange', 'red', 'green']:
            self.__colour = 'black'
        else:
            self.__colour = clr.lower()

    def set_availability(self, avl):
        if avl == True:
            self.__availability= 'for sale'
        else:
            self.__availability = 'not for sale'

    # Getters
    def get_num_room(self):
        return self.__num_room

    def get_colour(self):
        return self.__colour

    def get_availability(self):
        return self.__availability

myHouse=House(20, 'Red', True)

print(f'There is a {myHouse.get_colour()} house with {myHouse.get_num_room()} rooms, this house is {myHouse.get_availability()}')
