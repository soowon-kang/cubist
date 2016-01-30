# implement bubble sort, which is one of the famous sorting algorithm

def bsort( arr ):
    """flag is not necessary but it's useful when the list is almost sorted."""
    length = len( arr )
    flag = False                # initialize
    while length>0 and not flag:
        flag = True             # Is the array sorted?
        length -= 1
        for j in xrange( length ):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
                flag = False    # the array is not sorted
    return arr

while True:
    # input a list of numbers
    str_input = raw_input( 'input a list of numbers (ex. 4 1 2 -15 0) : ' )
    str_input = str_input.strip().split()
    try :
        arr_input = map(int, str_input)
        break
    except :
        print 'wrong input occur. please input integer numbers correctly.'

print 'Here are the result'
bubble_sorted_arr = bsort( arr_input )
for i in xrange( len( bubble_sorted_arr ) ):
    print bubble_sorted_arr[i],

