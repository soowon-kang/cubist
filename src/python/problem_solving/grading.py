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
        """sys.stdin can be variable r."""
        a = None
        for r in self.readers:
            a = r.readline()
        return a

if __name__ == "__main__":
    input_file_name = 'input'
    output_file_name = 'output'
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
        solution.main()     # from solution
        t2 = time.time() - t1
        print 'EXCUTION TIME for file(%d): '%(i)+str(t2)

        INPUT.close()
        OUTPUT.close()

    sys.stdin = save_input
    sys.stdout = save_output

