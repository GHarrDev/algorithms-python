def swap(a, b, arr):
    if a != b:
        # arr[a], arr[b] = arr[b], arr[a]
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
    
        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)   

    swap(pivot_index, end, elements)

    return end

def quick_sort(elements, start = 0, end = None):
    if end is None:
        end = len(elements) - 1
        
    if start < end:
        p_index = partition(elements, start, end)
        quick_sort(elements, start, p_index - 1)
        quick_sort(elements, p_index + 1, end)