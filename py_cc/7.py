#1
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car.title()}.")

#2
people = int(input("How many people are in the group? "))

if people > 8:
    print("You'll have to wait a while.")
else:
    print("Great! Your table is ready.")

#3
num = int(input("Enter a number: "))

if num % 10 == 0:
    print("Num is a multiple of 10")
else:
    print("Num is not a multiple of 10")



#4
prompt = "\nWhat topping would you like on your pizza? "
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
    else:
        break


#5

# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "
prompt = "How old are you?" + "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")


#6
#Use an active variable to control how long the loop runs
active=True
while active:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        active=False
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        active=False
    elif int(age)>12:
        print("Ticket is $15")
        active=False
        
#Use a conditional test in the while statement ot stop the loop
count=0
while count<10:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        count+=1
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        count+=1
    elif int(age)>12:
        print("Ticket is $15")
        count+=1

#Use a break statement to exit the loop when the user enters a 'quit' value.
active=True
while active:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        active=False
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        active=False
    elif int(age)>12:
        print("Ticket is $15")
        active=False
    elif age=='quit':
        break


#7
x=1
while x==1:
    print("To infinity and beyond!")

#8
sandwich_orders = ['ham', 'cheese', 'tuna']

finished_sandwiches = []

# for s in sandwich_orders:
#     print(f"I made your {s} sandwich.")
#     finished_sandwiches.append(s)

while sandwich_orders:
    s = sandwich_orders.pop() 
    print(f"I made your {s} sandwich.")
    finished_sandwiches.append(s)


print(finished_sandwiches)

#9
sandwich_orders = ['pastrami','ham', 'cheese', 'pastrami', 'pastrami', 'tuna']

finished_sandwiches = []

print("We've no more pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    s = sandwich_orders.pop() 
    print(f"I made your {s} sandwich.")
    finished_sandwiches.append(s)

print(finished_sandwiches)

#10






















































