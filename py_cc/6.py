#1
cormac = {
    'first_name': 'Cormac',
    'last_name': 'Crowley',
    'age': 4,
    'city': 'Askamore',
}

print(cormac['first_name'])
print(cormac['last_name'])
print(cormac['age'])
print(cormac['city'])

#2
fave_nums = {
    'Ann': 4,
    'Barry': 2,
    'Tom': 1,
    'Mike': 6,
    'Paul': 5
}

print(f"Ann's fave num is {fave_nums['Ann']}")

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

for key, values in words.items():
    print(f"The meaning of {key} is {values}")


#5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'niger': 'nigeria'
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

#6

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

lang_list = ['mike', 'paul']
for name in favorite_languages.keys():
    lang_list.append(name)

lang_list

for person in lang_list:
    if person in favorite_languages:
        print(f"{person.title()} thank you for your response")
    else:
        print(f"{person.title()} please take the poll")

#7

cormac = {
    'first_name': 'Cormac',
    'last_name': 'Crowley',
    'age': 4,
    'city': 'Askamore',
}

saoirse = {
    'first_name': 'Saoirse',
    'last_name': 'Crowley',
    'age': 1,
    'city': 'Askamore',
}

brian = {
    'first_name': 'Brian',
    'last_name': 'Coughlan',
    'age': 9,
    'city': 'Ardkeen',
}

people = [cormac, saoirse, brian]

# for person in people:
#     for key, value in person.items():
#         print(f"{value}")

for person in people:
    print(f"{person['first_name']} {person['last_name']}, aged {person['age']}")


#8

cat = {
    'type': 'feline',
    'owner': 'tom'
}

dog = {
    'type': 'canine',
    'owner': 'brian'
}

snake = {
    'type': 'lizard',
    'owner': 'ann'
}

pets = [cat, dog, snake]

# for pet in pets:
#     print(f"name is, {pet['name']}")


#9

favourite_places = {
    'ann': ['paris','berlin'],
    'barry': ['rome','london'],
    'kashi': ['dublin','paris']
}

for person, places in favourite_places.items():
    print(f"{person}:")
    for place in places:
        print(f"{place}")



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

#11
cities = {
    'paris': {
        'country': 'france',
        'capital': 'yes',
    },
    'cork': {
        'country': 'ireland',
        'capital': 'no',
    },
    'rome': {
        'country': 'italy',
        'capital': 'yes',
    },
}

for name, details in cities.items():
    print(f"City name is {name.title()}")
    for key, value in details.items():
        print(f" -{key}: {value}")

















































