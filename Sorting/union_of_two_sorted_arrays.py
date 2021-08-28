""" Union of two sorted arrays: Our task is two print all the elements in both the sorted arrays
    Both arrays might contain duplicates, but it should be printed once in the output"""


"""Solution: """


def union_sorted(arr1, arr2) -> list:
    n1 = len(arr1)
    n2 = len(arr2)
    temp = []
    index1, index2 = 0, 0
    while index1 < n1 and index2 < n2:
        if index1 > 0 and arr1[index1] == arr1[index1-1]:
            index1 += 1
            continue
        if index2 > 0 and arr2[index2] == arr2[index2 - 1]:
            index2 += 1
            continue
        if arr1[index1] < arr2[index2]:
            temp.append(arr1[index1])
            index1 += 1
            continue
        if arr1[index1] > arr2[index2]:
            temp.append(arr2[index2])
            index2 += 1
            continue
        if arr1[index1] == arr2[index2]:
            temp.append(arr1[index1])
        index1 += 1
        index2 += 1
    while index1 < n1:
        if index1 > 0 and arr1[index1] == arr1[index1 - 1]:
            index1 += 1
            continue
        temp.append(arr1[index1])
        index1 += 1
    while index2 < n2:
        if index2 > 0 and arr2[index2] == arr2[index2 - 1]:
            index2 += 1
            continue
        temp.append(arr2[index2])
        index2 += 1
    return temp


def main():
    arr_input1 = [1, 2, 2, 4, 5, 6, 6, 7]
    arr_input2 = [2, 4, 4, 6, 7, 8, 10]
    a2 = union_sorted(arr_input1, arr_input2)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
