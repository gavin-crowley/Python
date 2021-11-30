
# n = float(input("Enter: "))

# def fn(n):
#     return

# fn(n)


# def fn(n):
#     return

# fn(n)


# def numbers_to_strings(argument):
#     switcher = {
#         0: "zero",
#         1: "one",
#         2: "two",
#     }

#     return switcher.get(argument, "nothing")


# print(numbers_to_strings(0))

def numbers_to_strings(argument):
    switcher = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",  
        8: "Neptune"
    }
    
    return switcher.get(argument, "nothing")


print(numbers_to_strings(3))