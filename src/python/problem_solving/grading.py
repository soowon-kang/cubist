#-*- coding: utf-8 -*-

import solution
import sys
import time

INPUT = None
OUTPUT = None

class Writer(object):
    def __init__(self, *writers):
        self.writers = writers

    def write(self, text):
        """sys.stdout can be variable w."""
        assert str == type( text )
        for w in self.writers:
            w.write( text )

class Reader(object):
    def __init__(self, *readers):
        self.readers = readers

    def readline(self):
        """sys.stdin can be variable r. 
        The last element of readers must be file."""
        temp = None
        for r in self.readers:
            temp = r.readline()
        return temp

def is_matched(candidate, solution):
    assert file == type(candidate)
    assert file == type(solution)

    candidate_read_lines = candidate.readlines()
    solution_read_lines = solution.readlines()

    candidate_read_lines.pop(-1)

    return candidate_read_lines == solution_read_lines

if __name__ == "__main__":
    input_file_name = 'input'
    output_file_name = 'output'
    solution_file_name = 'sol'
    test_case = input('How many input files? ')

    save_input = sys.stdin
    save_output = sys.stdout

    for i in range( test_case ):
        INPUT = open(input_file_name+str(i)+'.txt','r')
        OUTPUT = open(output_file_name+str(i)+'.txt','w')
    
        #sys.stdin = Reader( sys.stdin, INPUT )
        #sys.stdout = Writer( sys.stdout, OUTPUT )
        sys.stdin = Reader( INPUT )
        sys.stdout = Writer( OUTPUT )
        t1 = time.time()
        try:
            solution.main()     # from solution.py
        except:
            pass
        t2 = time.time() - t1
        print 'EXCUTION TIME: '+str(t2)

        INPUT.close()
        OUTPUT.close()

    sys.stdin = save_input
    sys.stdout = save_output

    for i in range( test_case ):
        candidate = open(output_file_name+str(i)+'.txt','r')
        solution = open(solution_file_name+str(i)+'.txt','r')
        flag = is_matched(candidate, solution)
        if flag:
            print 'TEST%d PASS'%i
        else:
            print 'TEST%d FAIL'%i

