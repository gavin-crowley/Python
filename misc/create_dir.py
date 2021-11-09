#Create directory with inputted name:

import os
dirName = input("Enter the name of the folder you want to create: ")
os.mkdir(dirName)
print("Directory created.")