





######################################################################################


# functions can access variables declared outside the function

# keyword arguments need to be specified at function definition time

def test():
    pass

test()

# ordered arguments are not valid types of function arguments

# variable length keyword arguments are passed into the function as a dictionary

#Primitive Data Structures
#Integers
#Float
#Strings
#Boolean

#Non-Primitive Data Structures
#Arrays
#Lists
#Tuples
#Dictionary
#Sets
#Files

x = 3
y = 4

def add(a, b):
    result = x + y
    print(result)

add(10, 20)


# function code is not executed when defined
# a function can have multiple return values
# a function can have multiple return statments


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

############### TEST 11 Perform Troubleshooting and Error Handling 2 ###################

# You are not allowed to call len on an integer


#################### T12 Quiz: Perform Operations using Modules and Tools 2 #############


# print(datetime.today().strftime('%A')  # [Displays the full weekday name]
# print(datetime.today().strftime('%B')  # [Displays the full month name]
# print(datetime.today().strftime('%d'))  # [Displays the day of the month number (from 01 to 31)]
# print(datetime.today().strftime('%c'))  # [Displays the date and time appropriate for locale]
# print(datetime.today().strftime('%f'))  # [Displays the microsecond number (from 0 to 999999)]
# print(datetime.today().strftime('%I'))  # [Displays the hour number from 12‑hour clock]
# print(datetime.today().strftime('%H'))  # [Displays the hour number from 24‑hour clock]
# print(datetime.today().strftime('%j'))  # [Displays the day number of the year from 000 to 366]

# print(datetime.datetime.today()) # Displays current date and time

# print(getattr(datetime.today(), 'hour') ) displays current hour

# print(math.floor(67.3))  # [67]
# print(math.ceil(21.4))   # [22]


##########################################################################
# Course Appendix A
# Source Coding Best Practices




###########################################################################

# Course Appendix A
# Introduction to Clean Coding































































