class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')


apple = FruitFlavour()

# isinstance keyword Position1 an instance of Position2
print(isinstance(apple,Fruit))
print(isinstance(apple,FruitFlavour))

# issubclass keyword, seen as is Position1 a subclass of Position 2
print(issubclass(Fruit, FruitFlavour))
print(issubclass(FruitFlavour,Fruit))