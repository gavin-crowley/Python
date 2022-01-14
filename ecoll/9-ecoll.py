# x = open('python.csv', 'a')
# Ans: [Opens or creates a text file to append]

# x = open('python.csv', 'r+')
# Ans: [Opens a text file to read from or write to]



# x = '{} 3 {}'.format('Python', 'Test')
# print(x)  # output: [Python 3 Test]
 
# x = '{1} for {0}'.format('Python', 'Questions')
# print(x)  # output: [Questions for Python]



a = 'hello'
b = "hello"
c = "'hello'"
print(a,b,c)
# The correct answer is: hello hello 'hello'



x = open('python.bat', 'rb')  # [Opens an existing binary file to read]
y = open('python.bat', 'wb')  # [Opens or creates a binary file to write]
z = open('python.bat', 'ab')  # [Opens or creates a binary file to append]


# Character   Meaning
# 'r'     open for reading (default)
# 'w'     open for writing, truncating the file first
# 'x'     open for exclusive creation, failing if the file already exists
# 'a'     open for writing, appending to the end of the file if it exists
# 'b'     binary mode
# 't'     text mode (default)
# '+'     open a disk file for updating (reading and writing)
# 'U'     universal newlines mode (deprecated)




x = open('python.csv', 'r')
# Ans: [Opens an existing text file named python.csv to read]
x = open('python.csv', 'w')
# Ans: [Opens or creates a text file to write]




x = 'seven {1} {0}'.format(4, 5)
print('x is {}'.format(x))
print(type(x))
# The correct answer is: x is seven 5 4












