def insertion_sort(arr):
    for i in range(0, len(arr)):
        j = i
        while arr[j-1]>arr[j] and j >0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1




arr = [7,2,34,5,676,32,1]
insertion_sort(arr)
print(arr)