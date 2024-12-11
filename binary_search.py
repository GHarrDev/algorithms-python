from utils import time_it

@time_it
def linear_search(numbers_list, target_number):
    for index, element in enumerate(numbers_list):
        if element == target_number:
            return index
    return -1

@time_it
def binary_search(numbers_list, target_number):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0
    
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = numbers_list[mid_index]

        if target_number == mid_value:
            return mid_index
        
        if target_number > mid_value:        
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

@time_it
def binary_search_recursive(numbers_list, target_number, left_index, right_index):
    if left_index > right_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_value = numbers_list[mid_index]

    if target_number == mid_value:
        return mid_index
    
    if target_number > mid_value:        
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, target_number, left_index, right_index)

def all_occurances(numbers_list, target_number):
    index = binary_search(numbers_list, target_number)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers_list[i] == target_number:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers_list):
        if numbers_list[i] == target_number:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)