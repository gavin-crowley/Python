


str.capitalize()
str.title()
str.strip()
str.replace('new', 'old')

list.sort()


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

#######

for index, item in enumerate(todos):
    print(f"{index + 1}.{item.capitalize()}")

########

    file = open('files/todos.txt', 'r')
    todos = file.readlines()
    file.close()

    todos.append(todo)

    file = open('files/todos.txt', 'w')
    file.writelines(todos)
    file.close()

#######

 # new_todos = []

            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            new_todos = [item.strip('\n') for item in todos]
#######

sum() #sum an interable

#######

#convert list ints to str
temperatures = [10, 12, 14]
temperatures = [str(i) + '\n' for i in temperatures]

#########