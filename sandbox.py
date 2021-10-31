three_nums = input("Enter three nums: ")

n1, n2, n3 = tuple(three_nums)

if(n1 == n2 == n3):
    print((n1 + n2 + n3)*3)
else:
    print(n1 + n2 + n3)
