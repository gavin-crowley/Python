
# n = float(input("Enter: "))

# def fn(n):
#     return

# fn(n)


# def fn(n):
#     return

# fn(n)

def substring_copy(str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]

    result = ""
    for i in range(n):
        result = result + substr
    return result


print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))
print(substring_copy('pethujkol', 7))
