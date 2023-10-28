def binary_search(arr, tosearch, low, high):
    if low > high:
        return -1  

    mid = (low + high) // 2  

    if arr[mid] == tosearch:
        return mid  
    elif arr[mid] > tosearch:
        
        return binary_search(arr, tosearch, low, mid - 1)
    else:
        
        return binary_search(arr, tosearch, mid + 1, high)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tosearch = 3
result = binary_search(arr, tosearch, 0, len(arr) - 1)

if result != -1:
    print(f"Element {tosearch} found at index {result}.")
else:
    print(f"Element {tosearch} not found in the array.")

