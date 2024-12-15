def remove_duplicates(arr):
    seen = set()
    unique_elements = []
    for element in arr:
        if element not in seen:
            seen.add(element)
            unique_elements.append(element)
    return unique_elements

def shell_sort(arr):
    arr = remove_duplicates(arr)
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

    return arr