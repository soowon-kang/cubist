# -*- coding: utf-8 -*-
# CS300 HW3-3

def lds(arr):
    dp_arr = [1]
    max_item = 0
    for i in xrange(len(arr)):
        dp_arr.append(1)
        for j in xrange(i+1):
            if arr[i] < arr[j]:
                dp_arr[i] = max(dp_arr[i], 1+dp_arr[j])
        max_item = max(max_item, dp_arr[i])
    return max_item

# Test
if __name__ == "__main__":
    print lds([5, 2, 4, 2, 5, 1, 9, 10, 5]) == 4
