# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.\n")

# describe_pet('willie')


# def get_formatted_name(first_name, last_name, age=None):
#     """Return a full name, neatly formatted."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = get_formatted_name('jimi', 'hendrix', age=27)
# print(musician)

# prompt = "How old are you?" + "\nEnter 'quit' when you are finished. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("  You get in free!")
#     elif age < 13:
#         print("  Your ticket is $10.")
#     else:
#         print("  Your ticket is $15.")

# def make_album(name, title):
#         album = {
#             'name': name,
#             'title': title,
#         }
#         return album


# while True:
#     album = input("Enter your favourite album: ")        
#     artist = input("Enter the artist name?" + "\nEnter 'quit' when you are finished. ") 
#     if album == 'quit' or artist == 'quit':
#         break
           
    


# out = make_album(artist, album)
# print(out)

# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


# #Start with some desing that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# #Simulate printing each design, until none are left.
# #Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

# print(user_profile)






























































