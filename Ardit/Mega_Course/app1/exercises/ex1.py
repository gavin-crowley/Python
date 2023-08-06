# 1
# filenames = ['document', 'report', 'presentation']
#
# for i, item in enumerate(filenames):
#     print(f"{i}-{item.capitalize()}.txt")

# 2
# ips = ['100.122.133.105', '100.122.133.111']
# index = int(input("Enter an index: "))
# print(f"You chose {ips[index]}")

# Day 6
# 1
# file = open('../files/essay.txt', 'r')
# output = file.read()
# file.close()
# print(output.title())

# 2
# file = open('../files/essay.txt', 'r')
# content = file.read()
# file.close()
# print(len(content))

# 3
# new_member = input("Add a new member: ")
#
# file = open('../files/members.txt', 'r')
# existing_members = file.readlines()
# file.close()
#
# existing_members.append(new_member + '\n')
#
# file = open('../files/members.txt', 'w')
# file.writelines(existing_members)
# file.close()

# 4
#
# contents = ["Hello", "Hello", "Hello"]
# filenames = ["Larry.txt", "Curly.txt", "Moe.txt"]
#
# for content, filename in zip(contents, filenames):
#     file = open(f"../files/{filename}", 'w')
#     file.write(content)
# --------------
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()

# ------------------

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"../files/{filename}", 'r')
    content = file.read()
    file.close()
    print(content)
