import random

user_choice = input("Pick 1 for heads or 2 for tails: ")
decider = random.randrange(2) 

if decider == 0:
    print("HEADS")
else:
    print("TAILS")

num = eval(user_choice)
if num == decider: 
    print("Well done!")
else:
    print("Bad Luck!")

# The correct answers are: HEADS
# Bad Luck!, TAILS
# Well done!



# print(math.floor(67.3))  # [67]
# print(math.ceil(21.4))   # [22]




# print(datetime.today().strftime('%A')  # [Displays the full weekday name]
# print(datetime.today().strftime('%B')  # [Displays the full month name]
# print(datetime.today().strftime('%d'))  # [Displays the day of the month number (from 01 to 31)]
# print(datetime.today().strftime('%c'))  # [Displays the date and time appropriate for locale]
# print(datetime.today().strftime('%f'))  # [Displays the microsecond number (from 0 to 999999)]
# print(datetime.today().strftime('%I'))  # [Displays the hour number from 12‑hour clock]
# print(datetime.today().strftime('%H'))  # [Displays the hour number from 24‑hour clock]
# print(datetime.today().strftime('%j'))  # [Displays the day number of the year from 000 to 366]

# print(datetime.datetime.today()) # Displays current date and time

# print(getattr(datetime.today(), 'hour') ) displays current hour