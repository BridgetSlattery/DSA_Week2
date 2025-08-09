class House:
    def __init__(self, num_rooms, colour, availability):
        self.accepted_colours=['white', 'orange', 'red', 'green', 'blue', 'brown', 'yellow', 'purple']
        self.set_num_room(num_rooms)
        self.set_colour(colour)
        self.set_availability(availability)


    # Consturctor/initialiser
    # Setter each attribute
    def set_num_room(self, num):
        if num >=1 and num <= 20:
            self.__num_room=num
        elif num < 1:
            self.__num_room = 1
        elif num > 20:
            self.__num_room = 20
    def set_colour(self, clr):
        if clr.lower() not in self.accepted_colours:
            self.__colour = 'black'
        else:
            self.__colour = clr.lower()

    def set_availability(self, avl):
        if type(avl) == type(True):
            self.__availability=avl
        else:
            self.__availability = False

    # Getters
    def get_num_room(self):
        return self.__num_room

    def get_colour(self):
        return self.__colour

    def get_availability(self):
        return self.__availability

        ######### User Defined Functions

    def paint(self, new_colour):
        # colour must be in defined list
        # colour must be different from original colour
        if new_colour.lower() == self.accepted_colours:
            print('That\'s the same colour buddy')
        else:
            if new_colour.lower() in self.accepted_colours:
                print(f'{new_colour}, vey nice')
                self.set_colour(new_colour.lower())
            else:
                print(f'{new_colour} too ugly')

    def extend_house(self):
        if self.get_num_room() < 20:
            self.__num_room = self.__num_room + 1
        else:
            print('the house is big enough richy')

    def redesign(self, new_room_num):
        if new_room_num < 20 and new_room_num> 1:
            self.__num_room = new_room_num
        else:
            print('pick a normal number dude')

    def sell_house(self):
        if self.get_availability():
            print('the house is already on the market')
        else:
            self.set_availability(True)
            print('The house is now on the market')


    def __str__(self):
            return f'The house is {self.get_colour()} with {self.get_num_room()} rooms. The house is {(' ' if self.get_availability() else 'not')}, on the market.'

myHouse = House(10, 'Blue', False)

myHouse.paint('teal')
myHouse.extend_house()
myHouse.redesign(20)
print(myHouse)
print(myHouse)
myHouse.sell_house()
myHouse.paint('Blue')
print(myHouse)
myHouse.redesign(48)
print(myHouse)''