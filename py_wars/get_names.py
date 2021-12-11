def itemgetter(item):
    return item['name']
    
def get_names(data):
    return list(map(itemgetter, data))

# same as 

# def get_names(data):
#     names = []
#     for item in data:
#         names.append(item['name'])
#     return names

data = [
    {'name': 'Joe', 'age': 20},
    {'name': 'Bill', 'age': 30},
    {'name': 'Kate', 'age': 23}
]

print(get_names(data))