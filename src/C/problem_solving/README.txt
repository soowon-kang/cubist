Auther: Soowon Kang

The grading.c can grade an independent *.c file which has one main() function.
The name of *.c has to be given an argument when you execute the grading.c.
You have to create all input/solution files before you grade a problem.

The names of input files should be 'input*.txt'.(* is a number.)
The names of soluiton files should be 'sol*.txt'.(* is a number.)
The number should be gradually increasing started by 0.

An excution example is below.

    $ cat solution.c
    #include <stdio.h>

    int main(void){
        int a;
        scanf("%d",&a);
        printf("a=%d\n",a);
        return 0;
    }
    
    $ cat input0.txt
    3

    $ gcc grading.c -o grade
    $ ./grade solution
    How many input files? 1
    time diff= 0.000309

    $ cat output0.txt
    a=3


