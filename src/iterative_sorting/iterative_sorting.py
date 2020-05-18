# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # this swapped variable will stop the while loop
    swapped = True
    # this sorted variable keeps track of how many items
    # have been sorted while the loop is running
    sorted = -1
    # this loop will continue until there are no swaps
    while swapped:
        # if swapped does not change to True, this will break
        # the loop
        swapped = False
        # this increases by 1 through each loop because
        # 1 item is sorted per loop
        sorted += 1
        # since we decided the first element in the array is already
        # sorted, we begin with 1 instead of 0
        # we end with len(arr)-sorted because we don't go through
        # the already sorted indices each time
        for i in range(1, len(arr)-sorted):
            # if we find a smaller value while iterating through
            # the loop, we swap them
            if arr[i] < arr[i - 1]:
                swapped = True
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr
