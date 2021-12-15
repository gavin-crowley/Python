# class Dog:
#     """A simple attempts to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age =  age
        
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()

#1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} does {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

restaurant = Restaurant('Golden Balls', 'Chinese')

print(f"The restaurant's name is {restaurant.restaurant_name}, \
    which is a {restaurant.cuisine_type} restaurant.")

restaurant.describe_restaurant()
restaurant.open_restaurant()


#2

indian = Restaurant('The Taj', 'Indian')
indian.describe_restaurant()

afghan = Restaurant('Graveyard of Pies', 'Afghan')
afghan.describe_restaurant()

phillipino = Restaurant('Thousand Islands', 'Phillipino')
phillipino.describe_restaurant()


#3

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"Name is {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        print(f"Merry xmas {self.first_name} {self.last_name}")

i1 = User('tom', 'thumb')
i2 = User('mary', 'gregory')
i3 = User('alan', 'alda')

print(i1)
i1.describe_user()
i1.greet_user()

print(i2)
i2.describe_user()
i2.greet_user()

print(i3)
i3.describe_user()
i3.greet_user()






































































