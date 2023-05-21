def binary_recurs(arr, start, end, target):

    if end >= start:
        mid = start + end - 1 // 2

        if arr[mid] < target:
            return binary_recurs (arr, mid + 1, end, target)

        elif arr[mid] > target:
            return binary_recurs(arr, start, mid - 1, target)

        else:
            return mid

    else:
        return -1

arr = [1,4,8,11,16,45,33]
target = 17
result = binary_recurs(arr, 0, len(arr)-1, target)

if result != -1:
    print("Element is present at index:", str(result))

else:
    print("Element is not present in array:")






