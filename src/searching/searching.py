import math


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # grab middle of array
    # check if middle is equal to, <, or > target
    # if equal, stop
    # if less than, pick the mid of the left half
    # if greater than, pick the mid of the right half
    # repeat until start crosses end
    middle_index = math.ceil(len(arr)/2-1)
    start_index = 0
    end_index = len(arr) - 1
    while start_index < end_index:
        if arr[middle_index] == target:
            return middle_index
        elif arr[middle_index] > target:
            end_index = middle_index - 1
            middle_index = math.ceil((start_index + end_index) / 2)
        elif arr[middle_index] < target:
            start_index = middle_index + 1
            middle_index = math.ceil((start_index + end_index) / 2)
    return -1  # not found
