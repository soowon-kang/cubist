# 3n+1 problem
# Receive one non-negative integer number, which is starting number,
# and then print a procedure of calculation of 3n+1 problem.
# If n is an odd number, n becomes 3n+1.
# If n is an even number, n becomes n/2.
# When the n becomes 1, the whole procedure will finish.

n = input('n? ')
while n > 1 :
    print n,
    if n%2 == 0:
        n /= 2
    else:
        n = 3*n+1
print n
