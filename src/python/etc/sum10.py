# show up many ways of the sum of 1 to 10.

# ver 5
def sum_n( n ):
    sum_i = 0
    for i in xrange(1, n+1):
        sum_i += i
    return sum_i
print sum_n( 10 )

# ver 4
sum_i = 0
for n in xrange(1, 11):
    sum_i += n
print sum_i

# ver 3
sum_i = 0
for n in xrange(1, 11):
    sum_i = sum_i + n
print sum_i

# ver 2
sum_i = 0
for n in [1,2,3,4,5,6,7,8,9,10]:
    sum_i = sum_i + n
print sum_i

# ver 1
sum_i = 0
n   = 0
while n<10 :
    n   = n+1
    sum_i = sum_i + n
print sum_i

