def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
arr = [10, 5, 2, 3, 7, 6, 8, 9, 1, 4]
sorted_arr = quick_sort(arr)
print(sorted_arr)