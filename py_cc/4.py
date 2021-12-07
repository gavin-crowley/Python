#1
pizza = ['mushroom', 'swedish', 'calzone']

for p in pizza:
    print(p)

for p in pizza:
    print(f"Today we have {p} pizza.")
print(f"I love pizza\nI mean I really love pizza\nlike reaaallly...")


#2
animals = ['aardvark', 'cat', 'dog']

for a in animals:
    print(a)


#3
for i in list(range(1, 21)):
    print(i)

#4
numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#6
odd_nums = list(range(1, 21, 2))

for num in odd_nums:
    print(num)

#7
threes = list(range(3, 31, 3))

for num in threes:
    print(num)

#8
lst = list(range(1,11))

for num in lst:
    print(num ** 3)

#9
[num ** 3 for num in range(1, 11)]

#10
nums = list(range(1, 11))

print(f"The first three items in the list are: ")
for num in nums[-3:]:
    print(num)

#11
friend_pizza = pizza.copy()
friend_pizza
pizza.append('margharita')
pizza
friend_pizza.append('ham')
friend_pizza

#12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)

for food in my_foods[:]:
    print(food)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#13
food_tup = ('a', 'b', 'c', 'd', 'e')

for f in food_tup:
    print(f)

#food_tup['snake']

food_tup = ('a', 'f', 'c', 's', 'e')
food_tup




























































