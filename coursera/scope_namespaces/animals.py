def d():
    animal = 'elephant'
    def e():
        # Using nonlocalreferences the enclosed variable of animal one level up
        #this code block will reassign the value of animal from elephant to giraffe.
        nonlocal animal
        animal = 'giraffe'
        print('Inside nested function: ' + animal)

    print('Before calling nested function: ' + animal)
    e()
    print('After calling nested function: ' + animal)

animal = 'camel'
d()
print('Global animal: ' + animal)