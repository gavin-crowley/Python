todos = ['run', 'eat', 'clean']

while True:
    user_action = input("Type add, show, edit or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            todo_number = input("Enter number of todo to edit: ")
            new_todo = input("Enter new todo: ")
            todos[int(todo_number)-1] = new_todo
            print("Todo updated!")
        case 'exit':
            break
        case _:
            print("Unknown input")

print("Bye!")


