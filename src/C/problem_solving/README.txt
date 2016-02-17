Auther: Soowon Kang

    @ grading.c

The grading.c can grade an independent *.c file which has one main() function.
You have to create all input/solution files before you grade a problem.
When you execute the grading.c, there are 3 questions.
1. You should input the path (directory) of a problem set.
2. You should input the number of test cases in integer number format.
3. You should input the time limit in floating number format.

The names of input files should be 'input*.txt'.(* is a number.)
The names of soluiton files should be 'sol*.txt'.(* is a number.)
The number should be gradually increasing started by 0.

The script file which is named grade can compile grading.c and excute it.
You can just excute grade and input some appropriate arguments.

An excution example is below.

    $ cat p1/main.c
    #include <stdio.h>

    int main(void){
        int n;
        int i;
        scanf("%d", &n);
        for (i=1; i<10; i++)
            printf("%d*%d=%d\n", n, i, n*i);
        return 0;
    }
    
    $ cat p1/input0.txt
    1

    $ cat p1/sol0.txt
    1*1=1
    1*2=2
    1*3=3
    1*4=4
    1*5=5
    1*6=6
    1*7=7
    1*8=8
    1*9=9

    $ ./grade
    What is the path of problem? p1
    How many input files are in the path? 9
    What is the time limit (sec)? 1.0

    $ cat p1/output0.txt
    1*1=1
    1*2=2
    1*3=3
    1*4=4
    1*5=5
    1*6=6
    1*7=7
    1*8=8
    1*9=9

    $ cat p1/result.txt
    Okay! :D

-------------------------------------------------------------------------------

    @ txt_maker.c

The txt_maker.c can make some test files of problem set for grading.
You can just compile and excute it.

An excution example is below.

    $ gcc txt_maker.c -o make_txt

    $ ./make_txt
    What is the path of problem directory? factorial
    What is the mode? (input/sol) input
    How many files do you want to make? 5
    Start input0.txt data input! (\n for END)
    0 

    Start input1.txt data input! (\n for END)
    1

    Start input2.txt data input! (\n for END)
    2

    Start input3.txt data input! (\n for END)
    3

    Start input4.txt data input! (\n for END)
    4

    $ ./make_txt
    What is the path of problem directory? factorial
    What is the mode? (input/sol) sol
    How many files do you want to make? 5
    Start sol0.txt data input! (\n for END)
    1

    Start sol1.txt data input! (\n for END)
    1

    Start sol2.txt data input! (\n for END)
    2

    Start sol3.txt data input! (\n for END)
    6

    Start sol4.txt data input! (\n for END)
    24

