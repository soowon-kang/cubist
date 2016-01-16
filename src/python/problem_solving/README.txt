Auther: Soowon Kang

grading.py can grade solution.py file which has a main() function.
You have to create some input files first, if it needs in order to grade a problem.

The names of input files should be 'input*.txt'.(* is a number.)

An excution example is below.

    $ cat solution.py
    def main():
        a = raw_input()
        b = input()
        print type(a), a
        print type(b), b
    
    $ cat input0.py
    417
    115

    $ python grading.py
    How many input files? 1

    $ cat output0.py
    <type 'str'> 417
    <type 'int'> 115
    TIME: 0.000118017196655


