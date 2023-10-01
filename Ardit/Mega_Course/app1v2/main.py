# todos = ['run', 'eat', 'clean']
# todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                print(f"{index + 1}.{item.capitalize()}")
        case 'edit':
            todo_number = input("Enter number of todo to edit: ")
            new_todo = input("Enter new todo: ")

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos[int(todo_number)-1] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            print("Todo updated!")
        case 'complete':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'exit':
            break
        case _:
            print("Unknown input")

print("Bye!")

