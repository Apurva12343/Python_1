def bubble_sort(lst):
    n = len(lst)
    for j in range(0,n):
        for i in range(0,n-1):
            if(lst[i]>lst[i+1]):
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst
    
l = [90,10,23,11,27,52]
results = bubble_sort(l)
print(results)