from sys import argv

script, filename = argv

contents = open(filename)

print(f"Here's your filename: {filename}")
print(contents.read())