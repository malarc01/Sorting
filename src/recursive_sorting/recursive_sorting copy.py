# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    if len(arr) > 1:
        middle = len(arr)


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr)//2
        left_side = arr[0:middle]
        right_side = arr[middle+1:0]

    merge_sort(left_side)
    merge_sort(right_side)
    i = j = k = 0

    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            arr[k] = left_side[i]
            i += 1
        else:
            arr[k] = right_side[j]
            j += 1
        k += 1

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
