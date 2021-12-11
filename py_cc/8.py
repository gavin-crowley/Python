#1
def display_message():
    print("I'm learning about functions.")

display_message()

#2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book('Cosmos')

#3
def make_shirt(size, text):
    print(f"It's a {size} shirt with text \"{text.title()}\".")

make_shirt('large', 'yolo')
make_shirt(size='medium', text='yolo')

#4
def make_shirt(text, size='large'):
    print(f"It's a {size} shirt with text \"{text.title()}\".")

make_shirt('I Love Python')
make_shirt('I Love Python', size = 'medium')
make_shirt('Yolo', 'small')


#5
def describe_city(city, country = 'Ireland'):
    print(f"{city.title()} is in {country.title()}")

describe_city('Paris', 'France')
describe_city('Rome', 'Italy')
describe_city('Dublin')

#6
def city_country(city, country):
    pairs = f"{city}, {country}"
    return pairs

output = city_country('Santiago', 'Chile')
print(output)

#7
def make_album(artist, title, num_tracks = None):
    album = {
        'artist': artist,
        'title': title,
    }
    if num_tracks:
        album['num_tracks'] = num_tracks
    return album

out1 = make_album('Black Sabbath', 'Paranoid', 11)
out2 = make_album('Pink Floyd', 'Echoes')
out3 = make_album('Van Morrison', 'Astral Weeks', 9)
print(out1)
print(out2)
print(out3)

#8

def make_album(artist, title, num_tracks = None):
    album = {
        'artist': artist,
        'title': title,
    }
    if num_tracks:
        album['num_tracks'] = num_tracks
    return album

print("What's your favourite album?")
print("(enter 'q' at any time to quit)")

while True:
    title = input("Enter title: ")
    if title == 'q':
        break
    
    artist = input("Enter artist: ")
    if artist == 'q':
        break
    
    fave_album =  make_album(artist, title)
    print(fave_album)

print("Thanks for playing!")

#9
def show_messages(messages):
    for mess in messages:
        print(f"The message is: {mess}")

texts = ['hey you', 'how goes it', 'what you up to']

show_messages(texts)


#10
def send_messages(messages, sent_messages):
    for message in messages:
        print(f"The message is: {message}")
        sent_messages.append(message)
    return sent_messages


messages = ['hey you', 'how goes it', 'what you up to']
sent_messages = []

print(messages)
sent_output = send_messages(messages, sent_messages)
print(sent_output)

#11
def send_messages(messages, sent_messages):
    for message in messages:
        print(f"The message is: {message}")
        sent_messages.append(message)
    return sent_messages


messages = ['hey you', 'how goes it', 'what you up to']
sent_messages = []

print(messages)
sent_output = send_messages(messages, sent_messages)
print(sent_output)

#12
def sandwich_maker(*items):
    print(f"This sandwich contains: ")
    for item in items:
        print(f" - {item}")

sandwich_maker('ham', 'cheese', 'tuna')    

#13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('gavin', 'crowley', location='cork', field='IT', hobby='guitar')

print(user_profile)

#14
def make_car(make, colour, **options):
    options['make'] = make
    options['colour'] = colour
    return options

car = make_car('subaru', 'red', model='GT', tow_package=True)
print(car)

#15





















































































































