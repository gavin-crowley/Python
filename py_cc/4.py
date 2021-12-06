#1
# pizza = ['mushroom', 'swedish', 'calzone']

# for p in pizza:
#     print(p)

# for p in pizza:
#     print(f"Today we have {p} pizza.")
# print(f"I love pizza\nI mean I really love pizza\nlike reaaallly...")


#2
# animals = ['aardvark', 'cat', 'dog']

# for a in animals:
#     print(a)


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
list = list(range(1,11))

for num in list:
    print(num ** 3)

#9
[num ** 3 for num in range(1, 11)]






























