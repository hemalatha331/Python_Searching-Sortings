def linear_search(list1, value):
    for i in range(len(list1)):
        if list1[i] == value:
            return i
    return -1

listv = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = int(input("x = "))
result = linear_search(listv, x)

if result == -1:
    print("Element x is not present in the list")
else:
    print("Element found at index: " + str(result))

