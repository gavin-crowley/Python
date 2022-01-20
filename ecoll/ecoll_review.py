





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



# white space is considered as a line
# x = range(3, 6) up to not including 6
# programming2 = {1:"Java", 2:"Python", 3:"Ruby"} don't need "" around numbers in dict


programming = {"Java":1, "Python":2, "Ruby":3}
programming2 = {1:"Java", 2:"Python", 3:"Ruby"}

for i in programming:
    print(programming[i]) # prints dict value, rhs of key


#The flush() method in Python file handling clears the internal buffer of the file. In Python, files are automatically flushed while closing them
# f.tell() limits file size





x = 0
y = 1
z = "2"
sum = x + y + z
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


#import doc pydoc -> import module, help(module)


words = "The cow has spots and walks slowly."
my_sentence = words[-7:]
my_sentence = words[-7:] + words[:8]
my_sentence = my_sentence + words[4:7]
print(my_sentence)



print(5 % True) # 0
print(3 + False) # 3
print(True + 1) # 2
print(True and False) # False
print(True and True) # True



# python -m pydoc -p 314
# -p allows to open a page in web browser to view python packages



content = 'Learning Python is interesting especially when using strings'

x = content.find('in',6) #beginning at index 6 find 'in'
print(x)
result = content[x:30].capitalize()
print(result.center(20,'#'))





index = -1
system = {1:"A", 2:"B", 3:"C", 4:"D", 5:"F"}
index = 2
print(system[index]) # prints B, the dictionary key/value, not the index



words =['rat','bat','house','barn']

for w in words:
    if len(w) <=4:
        print(w) # rat bat barn






# just prints function docstring
"""
print the elements separated by sep
"""

def print_them(*elements, sep=","):
    """"
    another docstring
    """
    return sep.join(elements)

print(print_them.__doc__)




# they all print something
import random
my_list = ['Ruby', 'Python', 'Java', 'PHP']
print(random.sample(my_list,1))
print(random.choice(my_list))
print(random.choices(my_list)[0])
print(random.sample(my_list,2)[0])




elements = (12,2,8,5,14,6,22,35,18,4)
# items = {1:"C", 2:"C++", 3:"Java", 4:"Python", 5:"JavaScript", 6:"Go"}
items = {1:"C", 2:"C", 3:"J", 4:"P", 5:"J", 6:"G"}
count = 0
for e in elements:
    if e in items:
        continue # skips over iteration if condition is met
    count += e
print(count)





def fn(balance):
    balance += 2
    return balance * 2
x = 4
y = fn(x)
print(y)





students = [["M","T"], ["B","B"], ["L","C"], ["J","D"], ["T","E"]]
import csv
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)




measurements = [23.0, .0056, .023]
print(",".join("%.2f" % f for f in measurements)) #23.00,0.01,0.02

print(",".join("%.4d" % f for f in measurements)) # 0023,0000,0000 -> 0 padding on left

#  %s acts a placeholder for a string while %d acts as a placeholder for a number


a = 45
b = 45
print(a is not b) #False

a = 'Test'
b = 'Test'
print(a is b) # True

test1 = "This is a test"
test2 = 'This is a test'.upper()
print(test1 is test2) # False

print('h' in "Python") # True

print('is' in 'This IS a test') # True , in is case sensitive


colors = ('red', 'green', 'blue')
more_colors = ('red', 'green', 'blue')
extra_colors = more_colors
print(colors is extra_colors) # True
print(colors is more_colors) # True
print(more_colors is extra_colors) # True
# print(colors is in extra_colors) # Error


a = [1,2,3]
b = [1,2,3]

print(a == b) #True 
print(a is b) #False

colors = ['red', 'green', 'blue']
more_colors = ['red', 'green', 'blue']
extra_colors = more_colors
print(colors is extra_colors) # False
print(colors is more_colors) # False
print(more_colors is extra_colors) # True





amount = 325154.5687
print("{:,.2f}".format(amount)) #325,154.57





def my_list(a, L=[]):
    L.append(a)
    return L

my_list("eggs")
my_list("milk")
print(my_list("steak")) #['eggs', 'milk', 'steak']





v = bool([False])
x = bool(3)
y = bool("")
z = bool(' ')
print(v, x, y, z) #True True False True




x = 10
y = 6
z = y // 3 * 3 / 2 + x % 2 ** 2
print(z) # 5.0



#Custom exception
class MyException(Exception):
    pass



x = range(6) # 0,1,2,3,4,5




#==============================



print(4//6) #0


#=========================

# x = open('python.csv', 'r')
# Ans: [Opens an existing text file named python.csv to read]

# x = open('python.csv', 'w')
# Ans: [Opens or creates a text file to write]

# Character   Meaning
# 'r'     open for reading (default)
# 'w'     open for writing, truncating the file first
# 'x'     open for exclusive creation, failing if the file already exists
# 'a'     open for writing, appending to the end of the file if it exists
# 'b'     binary mode
# 't'     text mode (default)
# '+'     open a disk file for updating (reading and writing)
# 'U'     universal newlines mode (deprecated)




# To remember the difference between strftime and strptime, think of the " f " in strftime as "format" 
# and think of the " p " in strptime as "parse" as in convert.  For the statement, then, the two functions 
# just need to be reversed.


# In error handling, the else clause is indeed optional.  
# If it is used, it must come right after the except clause. 


# The break keyword exists a loop.  
# The while keyword starts a loop.  
# The continue keyword skips a turn in a loop.  
# The pass keyword is used as a placeholder.  
# It is commonly used as part of an if/elif/else statement to where one condition 
# temporarily does not need any action taken.  
# It is also used as a placeholder for the body of a function during development. 


# 5 and a maximum value of 11
#  random.randint(5, 11), random.randrange(5, 12, 1)


#When converting b to an integer, b == 5.  When converting d to an integer, d == 7. 
# Thus, a == int(b) and c == int(d).  Remember that the integer conversion function
# drops everything after the decimal point on a number. 


x = round(5.76543, 2)
print(x)


range(1,6) # 1,2,3,4,5


x,y = input() # is not a valid statement in Python. 
# We CANNOT input() a list of elements using a single input() function.  




# The try block lets you test a block of code for errors. 
# The except block lets you handle the error. 
# The else block lets you execute code when there is no error.






































