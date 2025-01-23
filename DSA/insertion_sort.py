def insertion_sort(arr):
    n = len(arr)
    min_index = 0
    for j in range(n):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr
lst = [12, 11, 13, 5, 6]
results = insertion_sort(lst)
print(results)