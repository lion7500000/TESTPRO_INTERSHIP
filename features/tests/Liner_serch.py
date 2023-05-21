def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr = [1,3,5,6,7,8,12,45,6]
target = 45

print (search(arr, target))