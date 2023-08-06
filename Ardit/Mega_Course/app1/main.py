

# user_input = ''
# while user_input != 'done':
#     user_input = input("Enter a todo: ")
#     print(user_input)

# input_status = ''
# user_input = ''
# todo_list = []
# while input_status != 'done':
#     user_input = input("Enter a todo: ")
#     if user_input == 'done':
#         input_status = user_input
#     else:
#         todo_list.append(user_input)
#
# print(todo_list)



# user_prompt = "Enter a todo:"
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
#
# todos = [todo1, todo2, todo3]
# print(todos)
#
# print(type(todo1))
#
# book_title = input("Enter title: ")
# print('Title length is', len(book_title))

# 1
# my_str_var = 'Friday!'
# print(type(my_str_var))

# 2
# user_input = input("Enter a string: ")
# print(user_input)

# 3
# my_list = ['a', 'b', 'c', 'd']

# 1
# user_prompt = input("Enter your name once: ")
# print(user_prompt.capitalize())

# 2
# user_prompt = input("Enter your name once: ")
# while True:
#     print(user_prompt.capitalize())

# 3
# name = ''
# while True:
#     name = input("Enter your name: ")
#     print(name.capitalize())

# DAY 3
#
# todos = []
#
# while True:
#     user_action = input("Type add, show, or exit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show' | 'display':
#             for item in todos:
#                 print(item)
#         case 'exit':
#             break
#         case _:
#             print("Unknown command")
#
# print("bye!")
















# 1
# country = []
#
# while True:
#     user_input = input("Enter the country you are from: ")
#
#     match user_input:
#         case 'USA':
#             print("Hello")
#         case 'India':
#             print("Namaste")
#         case 'Germany':
#             print("Hallo")
#         case 'exit':
#             break
#         case _:
#             print("Enter a different country")
# print("bye!")

# 2
#
# ingredients = ["john smith", "sen plakay", "dora ngacely"]
#
# for item in ingredients:
#     print(item.title())


# Day 4

# todos = ['clean', 'run']
#
# while True:
#     user_action = input("Type add, show, edit or exit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show':
#             for item in todos:
#                 print(item)
#         case 'edit':
#             todo_number = int(input("Enter the number of todo: "))
#             updated_todo = input("Enter the new todo: ")
#             todos[todo_number-1] = updated_todo
#         case 'exit':
#             break
#
# print("bye!")

# 1
# exchange_rate = 0.95
# amount = float(input("How many dollars have you got? "))
# print("The amount in euros is:\n", amount * exchange_rate)

# 2
# ranking = ['John', 'Sen', 'Lisa']
# rank_number = int(input("Enter rank number: "))
# print(ranking[rank_number-1])

# 3
# ranking = ['John', 'Sen', 'Lisa']
# name = input("Enter a name: ")
# print(ranking.index(name)+1)

# ----------

# Day 5 / 6

# todos = ['clean', 'cook', 'wash']
todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for i, item in enumerate(todos, 1):
                row = f"{i}.{item}"
                print(row)
        case 'edit':
            todo_number = int(input("Enter the number of todo: "))
            updated_todo = input("Enter the new todo: ")
            todos[todo_number-1] = updated_todo
        case 'complete':
            todo_num_comp = int(input("Number of completed todo: "))
            todos.pop(todo_num_comp - 1)
            print(f"Todo number {todo_num_comp} deleted!")
        case 'exit':
            break

print("bye!")















