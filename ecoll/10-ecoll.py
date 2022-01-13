# when a function is called but it returns nothing, print will give None
def add(x, y):
    return x + y

def mult(x, y):
    print(x * y)

add(1, 2)
print(add(2, 3))
mult(3, 4)
print(mult(4, 5))







# There are sometimes subtle differences between the syntax of a string and a tuple.

# Assignments through the program are akin to:

# t1 = ('cloudy') # no comma so this is a string, even if it is surrounded by parentheses

# t2 = ('cold', ) # it has a comma so this is a tuple

# sun  = ("sunny", "sun")  # a tuple of two strings

# first = 'c' + 'cold'  # the first character of t1 string, concatenated with first string of the t2 tuple

# return ("sunny", "ccold")

# The correct answer is: ('sunny', 'ccold')









global keyword
# https://stackoverflow.com/questions/4693120/use-of-global-keyword-in-python

# when a function is called but it returns nothing print will give None
def function1(a, b):
    return function2(a + b)

def function2(a):
    b = a * 5

print(function1(2, 3))



# don't need to specify variable for printing
print('Global variable: colours = ', colours) # this adds colours var

