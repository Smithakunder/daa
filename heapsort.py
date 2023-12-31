def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (maximum) element with the last element
        heapify(arr, i, 0)

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements separated by spaces: ").split()))

    heap_sort(arr)

    print("Sorted array:", arr)


# output:
# Enter the number of elements: 6
# Enter the elements separated by spaces: 12 11 13 5 6 7
# Sorted array: [5, 6, 7, 11, 12, 13]
