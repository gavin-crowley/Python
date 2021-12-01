def square_sum(numbers):
    #your code here
    total = 0
    for num in numbers:
        total += num**2
    return total


#################


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


#################

def square_sum(numbers):
    return sum(map(lambda x: x**2,numbers))


##################

def square_sum(numbers):
    return sum([x**2 for x in numbers])

##################