# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

prompt = "\nWhat topping would you like on your pizza? "
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
    else:
        break

