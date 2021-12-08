
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


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nWhat topping would you like on your pizza? "
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
    else:
        break











































































