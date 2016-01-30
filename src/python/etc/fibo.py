# generate Fibonacci's numbers

import math
lst = [0,1]

def fibo(n):
    arr = list()
    a,b = 0,1
    for _ in xrange(n):
        arr.append(a)
        a,b = b,a+b
    return arr

print 'This program generates Fibonacci sequence.'
while True:
    n = raw_input('How many numbers do you want to make? ')
    try :
        n = int(n)
        break
    except ValueError:
        print 'Wrong input occurs. Please input a natural number'

print 'Here are Fibonacci sequence.'
for i in fibo(n):
    print i,

def fibo_n(n):
    global lst
    while len(lst) < n :
        lst.append( lst[-1]+lst[-2] )
    return lst[n-1]

n = 100
f = fibo_n(n)
print n, math.log(f,2)
