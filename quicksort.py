def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        grater = [i for i in array[1:] if > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)