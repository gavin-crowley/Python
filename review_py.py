
list.sort(reverse=True)

############

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