#1
names = ['Alice', 'Bob', 'Tom']
print(names[0])
print(names[1])
print(names[2])

#2
print(f"Hey {names[0]}")
print(f"Yo {names[1]}")
print(f"Hey hey {names[2]}")

#3
classic_cars = ['Buick', 'Mustang', 'Chrysler']
print(f"I would like to own a {classic_cars[1]}")

#4
dinner_peeps = ['Jesus', 'Mary', 'Joseph']
print(f"{dinner_peeps[0]}, you're invited!")
print(f"{dinner_peeps[1]}, you're invited!")
print(f"{dinner_peeps[2]}, you're invited!")

#5
print(f"{dinner_peeps[2]}, can't make it :(")
dinner_peeps[2] = 'Aristotle'
print(f"{dinner_peeps[0]}, you're invited!")
print(f"{dinner_peeps[1]}, you're invited!")
print(f"{dinner_peeps[2]}, you're invited!")

#6
print('Found a bigger table!')
dinner_peeps.insert(0, 'Gandhi')
dinner_peeps.insert(2, 'Cobain')
dinner_peeps.append('Courtney')
dinner_peeps

#7
print("Sorry, only two people can come!")
dinner_peeps.pop()
dinner_peeps.pop()
dinner_peeps.pop()
dinner_peeps.pop()
dinner_peeps

print(f"Hey guys!, I can only accommodate {dinner_peeps[0]} and {dinner_peeps[1]}")

del dinner_peeps[0]
#del dinner_peeps[1]

print(dinner_peeps)

#8
places = ['Iceland', 'Faroes', 'Norway', 'Sweden', 'Finland']
places
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
places
places.reverse()
places
places.reverse()
places
places.sort()
places
places.sort(reverse=True)
places


#9
print(len(dinner_peeps))







