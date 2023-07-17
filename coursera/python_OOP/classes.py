class MyClass:
    a = 5

    def hello(self):
        print('Hello there!')

myc = MyClass()
myc.hello()

# second example

class House:
    '''
    Base house Object with rooms and bathrooms.
    '''
    num_rooms = 5
    bathrooms = 2

    def calc_cost(self, rate):
        #functionality to calc room cost
        cost = rate * self.num_rooms
        return cost

my_house = House()
print('My house has', my_house.num_rooms, 'rooms.')
print('The rate of rooms is', my_house.calc_cost(3.75))