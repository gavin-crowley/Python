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
def make_album(name, title):
    album = {
        'name': name,
        'title': title,
    }
    return album

out = make_album('Black Sabbath', 'Paranoid')
print(out)

#8






































