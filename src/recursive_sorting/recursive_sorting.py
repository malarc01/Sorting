# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    if len(arr) > 1:
        middle = len(arr)//2  # find the middle of the array to split
        left_side = arr[:middle]  # left side of the array
        right_side = arr[middle:]  # right side of the array

        # calling merge_sort()
        merge_sort(left_side)
        merge_sort(right_side)
        i = j = k = 0

        # copy data to temp arrays left_side[] + right_side[]
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1

        # checking if any element was left
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
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
