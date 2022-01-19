
#Q3
#All below are true
#A try clause can have any number of except clauses to handle different exceptions
#a try statement can have a finally clause without an except clause
#a try statement can have a finally clause and an except clause
#a try statement cannot have more than one finally clauses

#Q6_1 
#A and F

#Q17
#order of operations
# Paren, Exp, Pos/Neg, M/D, A/S, AND
# https://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html


x1 = "20"
y1 = 3
print(x1*y1) #202020
print(type(x1*y1)) #str

x2 = 6
y2 = 4
print(x2/y2) #1.5
print(type(x2/y2)) #float


# Q22
print("Congratualtions on " + str(int(end) - int(start)) + "years of service!") #CORRECT

#Q29
#200 employees
# first 195 employees[:-5], employees[0:-5]

#Q30
#scientific notation is type float

# Q11
#primes from 2 to 100
p = 2
while p <= 100:
    is_prime = True
    for i in range(2,p):
        if p % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(p)
    p = p + 1


# Q32
print("What is your name?")
name = input()
print(name)


# Q34
def get_first_line(filename, mode):
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            return file.readline()
    else:
        return None


# Q36
# read and write data to file
open("local_data", "r+")



# Q38
from math import sqrt as squareroot
from tkinter import X

# Q39
# abs value and no decimals
math.fabs(x)
math.ceil(x)

# Q40
# min of 5 max of 11
random.randint(5, 11)
random.randint(5, 11, 1)