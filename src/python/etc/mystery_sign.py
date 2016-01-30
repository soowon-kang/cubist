# implement a guessing game, which is named "mystery sign"

import math

def digit_sum(a, b):
    lst_a = list(str(a))
    lst_b = list(str(b))
    return sum(map(int, lst_a)) + sum(map(int, lst_b))

def reverse_product(a, b):
    lst_a = list(str(a))
    lst_b = list(str(b))
    lst_a.reverse()
    lst_b.reverse()
    str_a = "".join(lst_a)
    str_b = "".join(lst_b)
    return int(str_a) * int(str_b)

def digit_sum_product(a, b):
    lst_a = map(int, list(str(a)))
    lst_b = map(int, list(str(b)))
    len_a = len(lst_a)
    len_b = len(lst_b)
    if len_a < len_b :
        lst_c = lst_b
        for i in range(len_a):
            lst_c[-1-i] += lst_a[-1-i]
    else :
        lst_c = lst_a
        for i in range(len_b):
            lst_c[-1-i] += lst_b[-1-i]
    result = 1    
    for t in lst_c:
        result *= t
    return result
            
def is_a_big(a, b):
    if a > b :
        return 1
    else :
        return 0
    
def digit_del(a, b):
    if a < b :
        return digit_del(b, a)
    lst_a = list(str(a))
    lst_b = list(str(b))
    for t in lst_b:
        count = lst_a.count(t)
        for _ in range(count):
            lst_a.remove(t)
    if len(lst_a) > 0:
        return int("".join(lst_a) )
    else :
        return 0

def radix_length(a, b):
    return int(math.log(a, b)) + 1

def gcd(a, b):
    if b == 0 :
        return a
    return gcd(b, a%b)

def ab_div_gg(a, b):
    GCD = gcd(a, b)
    return a*b / GCD / GCD

def seven_segment(a, b):
    table = dict()
    table[0] = 6
    table[1] = 2
    table[2] = 5
    table[3] = 5
    table[4] = 4
    table[5] = 5
    table[6] = 6
    table[7] = 4
    table[8] = 7
    table[9] = 6
    
    lst_a = map(int, list( str(a) ))
    lst_b = map(int, list( str(b) ))

    result = 0
    for t in lst_a :
        result += table[t]
    for t in lst_b :
        result += table[t]
    return result

def odd_diff_even(a, b):
    lst_c = map(int, list( str(a)+str(b) ))
    odd = 0
    even = 0
    for i in range(len(lst_c)):
        if i%2 == 1 :
            odd += lst_c[-1-i]
        else :
            even += lst_c[-1-i]
    return odd - even

def mod60(a, b) :
    return (a+b)%60

def max_digit(a, b) :
    lst_c = map(int, list( str(a)+str(b) ))
    return max(lst_c)

def func(a, b, n) :
    round_arr = range(10)

    round_arr[1] = digit_sum
    round_arr[2] = reverse_product
    round_arr[3] = digit_sum_product
    round_arr[4] = is_a_big
    round_arr[5] = mod60
    round_arr[6] = digit_del
    round_arr[7] = max_digit
    round_arr[8] = ab_div_gg
    round_arr[9] = odd_diff_even

    return round_arr[n] (a, b)
    

def main() :
    while True :
        print '-'*23
        print '|', ' input "q" to quit ', '|'
        print '-'*23

        commend = raw_input(' Round n? (ex. 5) ')
        if commend.strip() == 'q' :
            break
        try :
            int_a = input('input the first integer number (ex. 4) : ')
            int_b = input('input second integer number (ex. 19) : ')
            n = int( commend )
        except ValueError :
            print 'wrong input occur! please try again'
            continue

        print '\nRound %d'%(n)
        print '%d @ %d = %d\n'%(int_a, int_b, func(int_a, int_b, n))

    return 0

if __name__ == '__main__' :
    main()
    
