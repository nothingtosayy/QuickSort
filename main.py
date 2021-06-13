def Quicksort(sequence):
    if len(sequence) <=1:
        return sequence
    pivot = sequence.pop()
    lower_than_pivot = []
    higher_than_pivot = []
    for i in range(len(sequence)):
        if sequence[i] <= pivot:
            lower_than_pivot.append(sequence[i])
        else:
            if sequence[i] > pivot:
                higher_than_pivot.append(sequence[i])
    return Quicksort(lower_than_pivot) + [pivot] + Quicksort(higher_than_pivot)

print(Quicksort([11,9,29,7,2,15,28,4,5,5,6,6,6,7,7]))
