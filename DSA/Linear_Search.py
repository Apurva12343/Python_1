def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [12,45,66,75,3,22,77,56]
target = 3
result = linear_search(arr,target)
print(result)