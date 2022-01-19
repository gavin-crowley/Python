#Q1 1 Q5
# The calc_power function calculates exponents
#A
# Yes, No, No

#Q2
# def increment_score(score, bonus, points)
#A
# Yes
# once we have a default argument, all the arguments to its right must also have default values.


#Q3
# online game
# update_score
#A
# update_score, (current, value), return current 


#Q4
# Woodgrove Bank is migrating their legacy
#A
#D Returns current balance

#Q4
# Evaluate numList = [0,1,2,3,4]
#A
numList = [0,1,2,3,4]
print(5 in numList) #False


#Q5
# Evaluate numList = [0,1,2,3,4]
#A
numList = [0,1,2,3,4]
print(5 in numList) #False


#Q6
# def checkType(value):
#A
#bool float int string

#Q7
# Woodgrove Bank must generate
#A
print(2234223.45/234) # 9547.962342342
print(2234223.45//234) # 9547.0
print(float(2234223.45//234)) # 9547.0


#Q8
# num1 = eval(input("Please enter the first number"))
#A
# line 4 yes, line 6 ?, line 8 yes, line 9 yes


#Q9
alph = "abcdefghijklmnopqrstuvwxyz"

print(alph[3:15]) # defghijklmno
print(alph[3:15:3]) # dgjm 
print(alph[3:15:-3]) #""
print(alph[15:3:-3]) # pmjg 
print(alph[15:3]) #""
print(alph[::-3]) #zwtqnkheb


#Q10
# def main(a,b,c,d)
#A
# first b * c
# second a +
# (a + (b * c)) - c


#Q11
# def get_discount(minor, senior)

print(not(True or True)) #False
print((not True) or True) #True
print(not(True and True)) #False
print((not True) and True) #False
#C


#Q12
# a = 'Config1'
#A
# first Config1
# second Config1Config2
# third Config1




#Q13
# Python program....collects customer data and stores in a database
#A
# int, bool, string, float,



#Q14
# Python program that compares numbers
#A
print(0 or 5) #5 
print(bool(0)) #False
print(None is None) #True
print(-5 < 0 < 5) #True



#Q15
# Debug
# x = 4
# while x >= 1:
#A
# party, birthday, birthday, cake



#Q16
#function reverses characters in a string
def reverse_name(backwards_name):
    forward_name = ''
    for index in backwards_name:
        forward_name += backwards_name[len(forward_name)-1]
    return forward_name

print(reverse_name("cba"))



#Q17
# age = input("Enter your age: ")
# data type
#A
# str, int, str
print(type(eval("3"))) # class int
print(type(eval("3") - eval("2"))) # class int



#Q18
# list_1 = [1,2]
#A
#C 1234 1234 1234


#Q19
# 200 colors
# colors[1::2]
colors = [9,8,7,6,5,4,3,2,]
print(colors[1::2]) # [8, 6, 4, 2]


#Q20
# def safe_division(numerator, denominator)
#A
# if numerator is None or denominator is None
#elif denominator == 0


#Q21
# Wingtip Toys times tables 2 - 12
def times_tables():
    for col in range(2,13):
        for row in range(2,13,1):
            print( row * col, end=" ")
        print()

times_tables()
# 4 6 8 10 12 14 16 18 20 22 24 
# 6 9 12 15 18 21 24 27 30 33 36 
# 8 12 16 20 24 28 32 36 40 44 48
# 10 15 20 25 30 35 40 45 50 55 60
# 12 18 24 30 36 42 48 54 60 66 72
# 14 21 28 35 42 49 56 63 70 77 84
# 16 24 32 40 48 56 64 72 80 88 96
# 18 27 36 45 54 63 72 81 90 99 108
# 20 30 40 50 60 70 80 90 100 110 120
# 22 33 44 55 66 77 88 99 110 121 132
# 24 36 48 60 72 84 96 108 120 132 144



#Q22
# num = int(input("Enter a number with 1 or 2 digits: "))
#A
# if num > -10 and num < 10
# elif num > -100 and num < 100
# ?


#Q23
# Admission fees
# Anyone under age 5 = free admission
#A
# if age >= 5 and school == True:
# elif age >= 5 and school == False:
# if age <= 17:

#Q24
# numList = [1,2,3,4,5]
# alphaList = [a,b,c,d,e,f]
#A
# if numList == alphaList:
# else:


# #Q25
# from random import randint
# target = randint(1,10)
# chance = 1
#A
# 5 while chance < 3:, 13 break, 14 chance += 1 


#Q26
# for i in range(len(items)):
# if items[i] == term:
# A
# def search...
#  for i in range...
#     if items[]...
#     break
#     else:...


#Q27
# Adventure Works Cycle sales are so exceptional that they...
#A
# for index in range(len(salary_list))
# continue



#Q28
# import sys
# try:
#     file_in = open("in.txt", 'r')
#A
# No change needed



#Q29
# import math
# default motion for happy clown
#A
# line 7 zero division error



#Q30
# You are creating a program that accepts user input
# while True
#A
# try exceptS



#Q31
# Relecloud Virtual Learning
# employee_pay = [15000,...]
#A
# len(employee_pay), sum/count



#Q32
# You work on a team that is developing a game for Adventure Works
# number is a multiple of 5
from random import randrange
from random import randint
print(randrange(5, 105, 5))
print(randrange(0,100,5)) #CORRECT
print(randint(0,20)*5)
print(randint(1,20)*5) #CORRECT



#Q33
# random float 0.0 - 1.0
import random
print(random.randrange(0.0,1.0)) #0
print(random.randint(0,1)) #1
print(random.random()) # 0.823424 CORRECT
# print(random.randrange()) #Error


#Q34
# def read_file(file):
    # line = None
def read_file(file):
    line = None
    if os.path.isfile(file):
        data = open(file,'r')
        for line in data:
            print(line)
#  need to import os library


#Q35
# You are writing a Python program to automate inventory.
inventory = open("inventory.txt", 'r')
eof = False
while eof == False:
    line = inventory.readline()

    if line !='': #CORRECT
         if line != '\n': #CORRECT
             print(line)
    else:
        print("End of file")
        eof = True
        inventory.close()



#Q36
# import datetime
# d = datetime.datetime(2017, 4, 7)
import datetime
d = datetime.datetime(2017, 4, 7)
print('{:%B-%d-%y}'.format(d))
num = 1234567.890
print('{:,.4f}'.format(num))
# April-07-17
# 1,234,567.8900





#Q37
# You are creating an eCommerce script that accepts
item = "item1"
sales = 3653
# B, C, E
print("{0},{1}".format(item,sales)) # item1,3653
print('"{0}",{1}'.format(item,sales)) # "item1",3653 CORRECT



#Q38 4 20:23k
# Tailspin Toys is building a basketball court
#A
# left-aligned -> %-10s



#Q39
# Oranges 5.6 1.33
# Apples 
# formatting 
#A
# {5:1f}
# {7:2f}


#Q40
# Northwind Electric Cars needs help
# import os
#A
# os.exists("myFile.txt")

#Need more for
#Q11, 16, 22, 39, 40