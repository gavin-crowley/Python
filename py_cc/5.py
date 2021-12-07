#1
car = 'subaru'
print("Is car == 'subaru' ? I predict True.")
print(car ==  'subaru')

print("\nIs car == 'audi' ? I predict False.")
print(car ==  'audi')

#2


#3
alien_color = 'green'
if alien_color == 'green':
    print("You earned five points!")

alien_color = 'red'
if alien_color == 'green':
    print("You earned five points!")


#4
alien_color = 'blue'
if alien_color == 'green':
    print("You earned five points!")
else:
    print("You earned ten points!")

if alien_color == 'blue':
    print("You earned five points!")
else:
    print("You earned ten points!")

#5
alien_color = 'blue'
if alien_color == 'green':
    print("You earned five points!")
elif alien_color == 'blue':
    print("You earned ten points!")

if alien_color == 'green':
    print("You earned five points!")
elif alien_color == 'yellow':
    print("You earned ten points!")
else:
    print("You earned 15 points!")

#6

age = 25

if age < 2:
    print("Is a baby")
elif age >= 2 and age < 4:
    print("Is a toddler") 
elif age >= 4 and age < 13:
    print("Is a kid") 
elif age >= 13 and age < 20:
    print("Is a teenager") 
elif age >= 20 and age < 65:
    print("Is an adult") 
else :
    print("Is an elder") 


#7
fruits = ['apples', 'bananas', 'cherries', 'pears']

if 'apples' in fruits:
    print(True)


favorite_fruits = ['apples','cherries', 'pears']

#8
usernames = ['admin', 'john22', 'peter33', 'mary44', 'paula55']

for name in usernames:
    if name == 'admin':
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name},thank you for logging in again.")


#9
usernames = ['admin', 'john22', 'peter33', 'mary44', 'paula55']

if usernames:
    for name in usernames:
        if name == 'admin':
            print(f"Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name},thank you for logging in again.")
else:
    print("We need to find some users!")

    

#10
current_users = ['Tom', 'John', 'Peter', 'Mary', 'Paula']
new_users = ['April', 'MARY', 'Ann', 'Barry', 'John']

current_copy = current_users.copy()
current_upper = [user.upper() for user in current_copy]
current_upper

for user in new_users:
    if user in current_users or user in current_upper:
        print(f"{user} already in use. Please use another name.")
    else:
        print(f"{user} is available")


#11
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for num in num_list:
    if num == '1':
        print(f"{num}st")
    elif num == '2':
        print(f"{num}nd")
    elif num == '3':
        print(f"{num}rd")
    else:
        print(f"{num}th")





































