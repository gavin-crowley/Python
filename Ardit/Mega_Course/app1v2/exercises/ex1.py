# Day 1
# # 1
# any_name = "a string"
# print(type(any_name))
#
# # 2
# user_input = input("Enter input: ")
# print(user_input)
#
# # 3
# my_list = ['a', 'b', 'c', 'd']

# Day 2
# 1
# user_prompt = input("Enter name once: ")
# print(user_prompt.capitalize())

# 2
# while True:
#     user_prompt = input("Enter name once: ")
#     print(user_prompt.capitalize())

# 3
# while True:
#     user_prompt = input("Enter name once: ")
#     print(user_prompt.capitalize())

# countries = []
#
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
#     print(countries)



# Day 3
# 1
# user_country = input("Where are you from? ")
#
# match user_country:
#     case 'USA':
#         print("Hello")
#     case 'India':
#         print("Namaste")
#     case 'Germany':
#         print("Hallo")

# 2
# ingredients = ["john smith", "sen plakay", "dora ngacely"]
# for item in ingredients:
#     print(item.title())

# Day 4
# 1
# dollars = int(input("Enter a dollar amount: "))
# euro_amount = dollars * 0.95
# print("Euro amount is:",euro_amount)

# 2
# ranking = ['John', 'Sen', 'Lisa']
# user_rank = int(input("Enter a rank: "))
# print(ranking[user_rank-1])

# 3
# ranking = ['John', 'Sen', 'Lisa']
# user_name = input("Enter a name: ")
# print(ranking.index(user_name)+1)
#



# Day 5
# 1
#
# filenames = ['document', 'report', 'presentation']
# for index, filename in enumerate(filenames):
#     print(f"{index}-{filename}.txt")

#2
# ips = ['100.122.133.105', '100.122.133.111']
#
# user_index = int(input("Enter index number: "))
# print(f"You chose {ips[user_index]}")

# Day 6
# contents = ['a', 'b', 'c']
# filenames = ['1.txt', '2.txt', '3.txt']
#
# for index, filename in enumerate(filenames):
#     file = open(filename, 'w')
#     file.writelines(contents[index])
#     file.close()

# 1
# file = open('../files/essay.txt', 'r')
# output = file.read()
# file.close()
# print(output.title())

# 2
# file = open('../files/essay.txt', 'r')
# output = file.read()
# file.close()
# print(len(output))
# i = 0
# for character in output:
#     i = i + 1
# print(i)

# 3
# user_input = input("Add a new member: ") + '\n'
#
# file = open('../files/members.txt', 'r')
# output = file.readlines()
# file.close()
#
# output.append(user_input)
#
# file = open('../files/members.txt', 'w')
# file.writelines(output)
# file.close()

# 4
# filenames = ['1.txt', '2.txt', '3.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write('Hello')
#     file.close()

# 5

# filenames = ['a', 'b', 'c']
#
# for filename in filenames:
#     file = open(f'../files/{filename}.txt', 'r')
#     output = file.read()
#     file.close()
#     print(output)


# Day 7

# filenames = ['1.doc', '1.report', '1.presentation']
# # new_filenames = []
# # for file in filenames:
# #     output = f"{file.replace('.', '-')}.txt"
# #     new_filenames.append(output)
# #
# new_filenames = [f"{file.replace('.', '-')}.txt" for file in filenames]
# print(new_filenames)

# 1
# names = ["john smith", "jay santi", "eva kuki"]
# new_names = [name.title() for name in names]
# print(new_names)

# 2
# usernames = ["john 1990", "alberta1970", "magnola2000"]
# num_chars = [len(user) for user in usernames]
# print(num_chars)

# 3
# user_entries = ['10', '19.1', '20']
# floats = [float(entry) for entry in user_entries]
# print(floats)

# 4
# user_entries = ['10', '19.1', '20']
# floats = [float(entry) for entry in user_entries]
# print(sum(floats))






















