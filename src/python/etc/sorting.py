# -*- coding: utf-8 -*-


def bsort(arr):
    length = len(arr)
    flag = False                # initialize
    # flag is not necessary but it's useful when the list is almost sorted.
    while length > 0 and not flag:
        flag = True             # Is the array sorted?
        length -= 1
        for j in range(length):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False    # the array is not sorted
    return arr


def _partition(arr):
    """helper function of quick sort."""
    val = arr[len(arr)/2]
    low = []
    high = []
    equal = []
    for v in arr:
        if v < val:
            low.append(v)
        elif v > val:
            high.append(v)
        else:
            equal.append(v)
    arr[:] = low + equal + high
    return len(low)


def qsort(arr):
    mid = _partition(arr)
    if mid == 0:
        return arr
    arr[:mid] = qsort(arr[:mid])
    arr[mid:] = qsort(arr[mid:])
    return arr


def msort(arr):
    if len(arr) < 2:
        return arr
    idx = len(arr)/2
    low = msort(arr[:idx])
    high = msort(arr[idx:])
    result = []
    while len(low) > 0 and len(high) > 0:
        if low[0] < high[0]:
            result.append(low.pop(0))
        else:
            result.append(high.pop(0))
    arr[:] = result+low+high
    return arr


def selection_sort(arr):
    pass


def insertion_sort(arr):
    pass


if __name__ == "__main__":
    # test code
    arr_input = []
    while True:
        # input a list of numbers
        str_input = raw_input('input a list of numbers (ex. 4 1 2 -15 0) : ')
        str_input = str_input.strip().split()
        try:
            arr_input = map(int, str_input)
            break
        except:
            print 'wrong input occur. please input integer numbers correctly.'

    print 'Here are the result'
    bubble_sorted_arr = bsort(arr_input[:])
    quick_sorted_arr = qsort(arr_input[:])
    merge_sorted_arr = msort(arr_input[:])
    for i in range(len(bubble_sorted_arr)):
        print bubble_sorted_arr[i],
    print
    for i in range(len(quick_sorted_arr)):
        print quick_sorted_arr[i],
    print
    for i in range(len(merge_sorted_arr)):
        print merge_sorted_arr[i],

