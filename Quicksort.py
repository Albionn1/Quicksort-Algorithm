
def quicksort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

print(quicksort([7,3,543,6,31,264,32,948,2,45,63,1,2,7,4,77,5]))