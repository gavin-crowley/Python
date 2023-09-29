# todos = ['run', 'eat', 'clean']
# todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

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

            for index, item in enumerate(todos):
                print(f"{index + 1}.{item.capitalize()}")
        case 'edit':
            todo_number = input("Enter number of todo to edit: ")
            new_todo = input("Enter new todo: ")
            todos[int(todo_number)-1] = new_todo
            print("Todo updated!")
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Unknown input")

print("Bye!")


