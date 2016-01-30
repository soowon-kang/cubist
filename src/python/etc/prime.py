# check whether a number is prime or not
# receive one non-negative integer number, which is n

def is_prime( n ) :
    if ( n < 2 ) or ( n%2 == 0 ) :
        return False

    sqn = int( n**(0.5) )
    flag = False
    for i in xrange(3, sqn+1, 2):
        flag |= ( n%i == 0 )

    return not flag
while True:
    try:
        n = input('n? ')
        break
    except:
        print 'wrong input occurs.'

print n, 'is',
if not is_prime( n ) :
    print 'not',
print 'a prime.'
