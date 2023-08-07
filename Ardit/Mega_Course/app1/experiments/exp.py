# password = ''
#
# while True:
#     if(password == 'abc123'):
#         print("Correct!")
#         break
#     else:
#         password = input("Enter a password: ")

# --------

# password = ''
#
# while password != 'abc123':
#     password = input("Enter a password: ")
#
# print("Correct!")

# -------

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# ------------
#
# filenames = ["1.Raw", "2.Report"]
# new_filenames = []
#
# for item in filenames:
#     new_item = item.replace('.','-')
#     new_filenames.append(new_item)
#
# print(new_filenames)

# --------------
# waiting_list = ['sen', 'ben', 'john']
# waiting_list.sort()
#
# for index, item in enumerate(waiting_list, 1):
#     print(f"{index}.{item.capitalize()}")

# ---------------

# contents = ["a", "b", "c"]
# filenames = ["1.txt", "2.txt", "3.txt"]
#
# for content, filename in zip(contents, filenames):
#     file = open(f"../files/{filename}", 'w')
#     file.write(content)

########### DAY 7

# filenames = ['a.blah', 'b.blah', 'c.blah']
# new_names = [name.replace('.', '-') + '.txt' for name in filenames]
# print(new_names)

########### DAY 8
date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow: ")

with open(f"journal/{date}.txt", 'w') as file:
    file.writelines(mood + 2 * "\n")
    file.writelines(thoughts)

