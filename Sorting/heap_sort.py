""" Heap Sort: This algorithm is similar to selection sort and take O(n log n) while it builds a heap data structure to sort
    the elements. Using Max and Min Heaps. In a heap parent of a element in  (i-1)/2 where i is index of element and the
    left child = 2*i + 1 and right child = 2*i + 2"""

""" Implementation: """


def max_heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def build_heap(arr, n):
    for i in range((n-2)//2, -1, -1):
        max_heapify(arr, n, i)


def heap_sort(arr, n) -> list:
    build_heap(arr, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)
    return arr


def main():
    arr_input = [10, 5, 30, 1, 2, 5, 10, 10]
    n = len(arr_input)
    a2 = heap_sort(arr_input, n)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()

