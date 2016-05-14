#-*- coding: utf-8 -*-

# ver 1.1
# convert decimal number to any base radix between 2 and 16
# for example, DEC: 61 == BIN: 111101 == OCT: 75 == HEX: 3D

STR_DIGIT = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def dec_to_any( num=20, base=5 ):
    result = str()
    while num > 0 :
        result = (STR_DIGIT[ num%base ]) + result
        num /= base
    return result

def any_to_dec( num='20', base=5 ):
    result = 0
    temp = 1
    while len(num) > 0:
        last_digit = num[-1]
        result += STR_DIGIT.index( last_digit ) * temp
        temp *= base
        num = num[:-1]
    return result

print 'This is base(2~16) converter.'
while True:
    print '\nCHOOSE MODE\n 1: DEC->any\n 2: any->DEC\n 3: quit\n >>> ',
    choice = raw_input()
    if choice == '1':
        dec_num = raw_input('input a decimal number(ex: 520): ')
        base = raw_input('input base(ex: 4): ')
        try: 
            dec_num = int( dec_num )
            base = int( base )
            result = dec_to_any( dec_num, base )
        except:
            print 'Wrong input occurs. Please try again'
            continue
        print 'A decimal number %d is %s in base %d'%(dec_num, result, base)
    elif choice == '2':
        any_num = raw_input( 'input a number(ex: 4F): ' )
        base = raw_input( 'input base(ex: 16): ' )
        try:
            base = int( base )
            result = any_to_dec( any_num, base )
        except:
            print 'Wrong input occurs. Please try again'
            continue
        print 'A %s in base %d is %d in base 10'%(any_num, base, result)
    elif choice == '3':
        print 'Program terminates.'
        break
    else :
        print 'Wrong choice. Please input among 1, 2 and 3'

#23456789012345678901234567890123456789012345678901234567890123456789012345678
