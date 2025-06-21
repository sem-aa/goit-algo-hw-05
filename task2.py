arr = [1,2,3,4,5,6,7,8,9,10,11, 12, 13, 14, 15, 16]

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    result = None
    count = 0 

    while (low <= high):
        count += 1
        mid = (high + low) // 2

        if arr[mid] >= x:
            result = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

  
    return (count, result)


print(binary_search(arr, 5))