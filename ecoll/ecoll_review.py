





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







































