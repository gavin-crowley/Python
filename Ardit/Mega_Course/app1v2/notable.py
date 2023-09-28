


str.capitalize()
str.title()
str.strip()
str.replace('new', 'old')


#####################
# match-case demo

todos = []

while True:
    user_action = input("Type add or show, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("Unknown input")

print("Bye!")

#####################

for can iterate over 'string'

myList.index(2)


#Get position in list with string entered:
ranking = ['John', 'Sen', 'Lisa']
user_name = input("Enter a name: ")
print(ranking.index(user_name)+1)

########

# replace item in list:
list[1] = new


