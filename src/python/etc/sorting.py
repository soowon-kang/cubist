# -*- coding: utf-8 -*-


def bsort(arr):
    """flag is not necessary but it's useful when the list is almost sorted."""
    length = len(arr)
    flag = False                # initialize
    while length > 0 and not flag:
        flag = True             # Is the array sorted?
        length -= 1
        for j in xrange(length):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False    # the array is not sorted
    return arr


def _partition(arr):
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
    return len(low), low + equal + high


def qsort(arr):
    mid, arr = _partition(arr)
    if mid == 0:
        return arr
    print "arr", arr
    low = qsort(arr[:mid])
    high = qsort(arr[mid:])
    return low + high


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
bubble_sorted_arr = bsort(arr_input)
quick_sorted_arr = qsort(arr_input)
for i in range(len(bubble_sorted_arr)):
    print bubble_sorted_arr[i],
for i in range(len(quick_sorted_arr)):
    print quick_sorted_arr[i],
