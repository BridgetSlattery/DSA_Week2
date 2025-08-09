class House:
    """
    Class Doc
    this class is about an object 'House', its attributs: room number and its availability to the market
    the class has three setters three getters and str
    additionally the class has user defined functions
    Paint
    Extend_house
    Redesign
    Sell_house
    """
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
        """
        The function will get a new colour from the user and if the colour as the existing will display a message
        if the colour is new and exists in the accepted colour list, the colour will be changed
        otherwise an error message will be printed
        :param new_colour: string
        :return: None
        """

        if new_colour.lower() == self.accepted_colours: # check if new colour is different from original colour
            print('That\'s the same colour buddy')
        else:
            if new_colour.lower() in self.accepted_colours: # check if colour is in defined list
                print(f'{new_colour}, vey nice')
                self.set_colour(new_colour.lower())
            else:
                print(f'{new_colour} too ugly')

    def extend_house(self):
        """

        :return:
        """
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
            return f'This property is{(' ' if self.get_availability() else ' not ')}on the market. The property has {self.get_num_room()} rooms and is painted {self.get_colour()}.'
############## Making child Apartment from class house ##################


class Apartment(House):
    def __init__(self, num_rooms, colour, availability, level_num):
        super().__init__(num_rooms, colour, availability)
        self.set_level_num(level_num)

    def set_level_num(self, level_num):
        if -10 <= level_num <= 100:
            self.__level_num=level_num
        else:
            self.__level_num = 0
    def get_level_num(self):
        return self.__level_num
    def redesign(self, new_room_num):
        if new_room_num > 5:
            print('Apartments cannot be redesigned with more than 5 rooms')
        else:
            self.set_level_num(new_room_num)
    def __str__(self):
        return f'{super().__str__()} This is an apartment on level {self.__level_num}'

myHouse1 = House(10, 'Brown', True)
myHouse2 = House(15, 'White', True)
myHouse3 = House(75, 'Blue', False)
myApt1 = Apartment(3, 'red', True, 2)
myApt2 = Apartment(6, 'blue', True, 30)
myApt3 = Apartment(15, 'white', False, 90)
myApt4 = Apartment(1, 'white', True, 29)

# dynamic object in a list
property_list = [myHouse1, myHouse2, myHouse3, myApt1, myApt2, myApt3, myApt4]

print('Available Properties:')
for item in property_list:
    if item.get_availability():
        print(item)

print('Boring Houses:')
for item in property_list:
    if item.get_colour() == 'white':
        print(item)

print('Small Houses:')
for item in property_list:
    if item.get_num_room() < 10:
        print(item)