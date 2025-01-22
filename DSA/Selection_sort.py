def selection_sort(lst):
    n = len(lst)
    for j in range(n-1):
        min_index = j
        for i in range(j+1,n):
            if(lst[i]<lst[min_index]):
                min_index= i
        lst[j],lst[min_index] = lst[min_index],lst[j]
    return lst

arr = [11,25,22,45,32,90]
results = selection_sort(arr)
print(results)