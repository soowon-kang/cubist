# calculation of factorial numbers
# input one non-negative integer number, which is n

import math

def fact_rec( n ) :
    if n == 0 :
        return 1
    return n * fact_rec( n-1 )

def fact_iter( n ) :
    result = 1
    for i in xrange( 1, n+1 ) :
        result *= i
    return result

n = input('n? ')
print '%d! is %d' % (n, fact_iter(n))

print 'log(%d!) = %f' % ( n, math.log10(fact_iter(n)) )
