#-*- coding: utf-8 -*-
"""Implementation radix sort, which is one of the famous sorting algorithms.
Reference: http://goo.gl/zzphB3"""

from math import log
from random import randrange

def partition(array=[], pivot=0, radix=10):
    """Prepare to sort the input array.
    Calculate pivot position and the length of the lengthiest item of array."""
    low = []
    same = []
    high = []
    max_len = -1
    for idx, t in enumerate(array):
        if t != 0:
            length = int(log(abs(t), radix)+1)
        else:
            length = 1

        if length > max_len:
            max_len = length

        if t < pivot:
            low.append(t)
        elif t == pivot:
            same.append(t)
        elif t > pivot:
            high.append(t)
        else:
            raise ValueError("%s of input array is not compatible with %s."\
                    %(t, pivot))
    return low+same+high, len(low), max_len

def radix_sort(arr=[], start=0, end=0, radix=10):
    """partition cost: O(n) where n is the length of array.
    rsort cost: O(d*n) where d is the length of the lengthiest item of array."""
    arr[start:end+1], idx, max_digit = partition(arr[start:end+1], 0, radix)
    low = rsort(arr[start:idx], radix, max_digit)
    high = rsort(arr[idx:end+1], radix, max_digit)
    return low+high

def rsort(arr=[], radix=10, length=0):
    if len(arr) == 0:
        return 

    for i in xrange(length):
        # make an empty list of size radix
        radix_array = [ [] for _ in xrange(radix) ]     

        # beware of the negative integers
        for t in arr:
            radix_array[(t/(radix**i))%radix].append(t)

        # replace the elements
        l = 0
        for t in radix_array:
            arr[l:l+len(t)] = t
            l += len(t)

        del radix_array
    
    return arr

while True:
    # input a list of integers
    str_input = raw_input('Input some integers (ex. 4 1 2 -15 0) : ')
    str_input = str_input.strip().split()
    try :
        arr_input = map(int, str_input)
        break
    except :
        print 'Wrong input occur. Please input integer numbers correctly.'

"""
arr_input = [ randrange(-999, 1000) for _ in xrange(50) ]
print arr_input
"""

print 'Sorting result is as follows.'
radix_sorted_arr = radix_sort(arr_input, 0, len(arr_input)-1, 10)
for t in radix_sorted_arr:
    print t,

