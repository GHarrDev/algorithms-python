# Python offers a built-in sort() function.
# This is for educational purposes only.

def insertion_sort(elements):
    for i in range(1, len(elements)):
        self = elements[i]
        j = i - 1
        while j >= 0 and self < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j - 1] = self
        