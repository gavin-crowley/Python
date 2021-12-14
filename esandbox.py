
cheese = 'cheddar'


def make_omelette():
    cheese = 'swiss'
    omelette = 'a {} omelette'.format(cheese)
    return omelette

def make_pancake1():
    global cheese
    cheese = 'Brie'
    pancake = 'a {} pancake'.format(cheese)
    return pancake

def make_pancake2():
    pancake = 'a {} pancake'.format(cheese)
    return pancake
    
print(make_omelette())
print(make_pancake1())
print(make_pancake2())

# https://www.geeksforgeeks.org/global-local-variables-python/ 