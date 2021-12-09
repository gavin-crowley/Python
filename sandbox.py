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

def make_album(name, title):
        album = {
            'name': name,
            'title': title,
        }
        return album


while True:
    album = input("Enter your favourite album: ")        
    artist = input("Enter the artist name?" + "\nEnter 'quit' when you are finished. ") 
    if album == 'quit' or artist == 'quit':
        break
           
    


out = make_album(artist, album)
print(out)
