def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j -  gap]
                j -= gap
            arr[j] = anchor    
        gap //= 2
