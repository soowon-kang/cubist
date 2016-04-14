# -*- coding: utf-8 -*-
import random

START_CHARACTER = 'A'
END_CHARACTER = 'Z'
END_NUMBER = 17

def make_random_occupied_seats():
    arr=[]
    for s in xrange(ord(START_CHARACTER), ord(END_CHARACTER)+1):
        for idx in xrange(END_NUMBER):
            randi = random.randint(0, 2)
            if randi == 0:
                arr.append( chr(s)+str(idx+1) )
    return arr

def make_whole_seats(occupied_seats=[]):
    #whole_seats = [ [0] for _ in xrange(END_NUMBER) ]
    #above code has aliasing error
    whole_seats = [[ 0 for _ in xrange(END_NUMBER) ]\
            for i in xrange(ord(END_CHARACTER)-ord(START_CHARACTER)+1)]


    for seat in occupied_seats:
        s = ord(seat[0])-ord(START_CHARACTER)
        idx = int(seat[1:])
        whole_seats[s][idx-1] = 1

    return whole_seats

def calc_longest_seats(seats_matrix=[]):
    answer = []
    max_length = -1
    for idx, row in enumerate(seats_matrix):
        left = right = 0
        row.append(1)
        seat_char = chr(ord(START_CHARACTER)+idx)
        for t in row:
            if t==1:
                m = right-left
                if max_length < m:
                    max_length = m
                    answer = [[ seat_char+str(left+1), seat_char+str(right) ]]
                elif max_length == m:
                    answer.append( [ seat_char+str(left+1),\
                            seat_char+str(right) ] )
                left = right+1
            right += 1

    return answer

random_array = make_random_occupied_seats()
seats = make_whole_seats( random_array )
print len(random_array)
print random_array
print calc_longest_seats( seats )

'''
1 0 1 1 1 1 1 0 1 1 0 0 1
0 1 0 0 0 0 0 1 0 0 1 2 0 2n¿¬»ê?
[idx for idx, elem in enumerate(res) if elem==max(res)]
for idx, elem in enumerae(res):
   if elem == max(res):
       tmp.append(idx)

0000011100000
0000000011111

'''


