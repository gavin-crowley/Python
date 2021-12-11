
list.sort(reverse=True)

#############################################

#3
for i in list(range(1, 21)):
    print(i)


#4
numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#8
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

#9
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)

#10
nums = []
for num in nums[:3]:
    print(num)

# last three 
for num in nums[-3:]:
    print(num)


#11
friend_pizza = pizza.copy()

################################################

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


##########################################

#3
words = {
    'ls': '1 linux command',
    'grep': '2 linux command',
    'cd': '3 linux command',
    'ps': '4 linux command',
    'ps aux': '5 linux command',
}

#4
for key, values in words.items():
    print(key)
    print(values)

for key in words.keys():
    print(key)

for value in words.values():
    print(value)


#6

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

lang_list = ['mike', 'paul']

for name in favorite_languages.keys():
    lang_list.append(name)

lang_list

for person in lang_list:
    if person in favorite_languages:
        print(f"{person.title()} thank you for your response")
    else:
        print(f"{person.title()} please take the poll")


#10
fave_nums = {
    'Ann': [4, 7],
    'Barry': [3,8],
    'Tom': [2, 9],
    'Mike': [5, 8],
    'Paul': [7, 3]
}

for person, nums in fave_nums.items():
    print(f"{person}'s fave numbers are:")
    for num in nums:
        print(f"- {num}")


#Ex
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


#4
prompt = "\nWhat topping would you like on your pizza? "
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
    else:
        break


#5
# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "
prompt = "How old are you?" + "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")


#6
#Use an active variable to control how long the loop runs
active=True
while active:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        active=False
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        active=False
    elif int(age)>12:
        print("Ticket is $15")
        active=False
        
#Use a conditional test in the while statement ot stop the loop
count=0
while count<10:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        count+=1
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        count+=1
    elif int(age)>12:
        print("Ticket is $15")
        count+=1

#Use a break statement to exit the loop when the user enters a 'quit' value.
active=True
while active:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        active=False
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        active=False
    elif int(age)>12:
        print("Ticket is $15")
        active=False
    elif age=='quit':
        break


#7
x=1
while x==1:
    print("To infinity and beyond!")

#8
sandwich_orders = ['ham', 'cheese', 'tuna']

finished_sandwiches = []

# for s in sandwich_orders:
#     print(f"I made your {s} sandwich.")
#     finished_sandwiches.append(s)

while sandwich_orders:
    s = sandwich_orders.pop() 
    print(f"I made your {s} sandwich.")
    finished_sandwiches.append(s)


print(finished_sandwiches)


#9
sandwich_orders = ['pastrami','ham', 'cheese', 'pastrami', 'pastrami', 'tuna']

finished_sandwiches = []

print("We've no more pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    s = sandwich_orders.pop() 
    print(f"I made your {s} sandwich.")
    finished_sandwiches.append(s)

print(finished_sandwiches)

##################################

#7
def make_album(name, title):
    album = {
        'name': name,
        'title': title,
    }
    return album

out = make_album('Black Sabbath', 'Paranoid')
print(out)


#14
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)


















































































