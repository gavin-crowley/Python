def binary_search(list, item):
    low = 0
    high = len(list)-1

    counter = 0
    
    while low <= high:
        counter+=1
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            # return mid
            print(f"It took {counter} cycles of the loop")
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1 
    return None

def linear_search(list, item):
    counter = 0
    for i in range(len(list)):
        counter+=1
        if list[i] == item:
            print(f"It took {counter} cycles of the loop")



    

my_list = [1, 3, 5, 7, 9]


# binary_search(my_list, 1)
# binary_search(my_list, 3)
# binary_search(my_list, 5)
# binary_search(my_list, 7)
# binary_search(my_list, 9)

linear_search(my_list, 1)
linear_search(my_list, 3)
linear_search(my_list, 5)
linear_search(my_list, 7)
linear_search(my_list, 9)