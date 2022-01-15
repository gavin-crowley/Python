import datetime

print(datetime.date.today()) #2022-01-15
print(datetime.datetime.today()) #2022-01-15 13:29:57.243676


today = datetime.date.today()

print("{:%A, %b %Y}".format(today))
print("{:%d, %b %Y}".format(today))
print("{:%A, %m %Y}".format(today))



# A is day word
# b is month word


# f microsecond number
# I hour number from 12‑hour clock
# H hour number from 24‑hour clock
# d day number
# j day number of the year from 000 to 366
# m month number
# Y year number