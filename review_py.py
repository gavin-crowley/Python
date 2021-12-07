
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






















