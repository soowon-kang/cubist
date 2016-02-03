#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char* INPUT = "input";
char* OUTPUT = "output";
char* SOL = "sol";

int main(int argc, char** argv){
    char input_name[20];
    char output_name[20];
    char solution_name[20];
    char buf[80];

    int test_case;
    int i;

    time_t start_time;
    time_t end_time;

    printf("How many input files? ");
    scanf("%d", &test_case);

    for (i=0; i<test_case; i++){

        sprintf(buf, "gcc %s.c -o %s", argv[argc-1], argv[argc-1]);
        system( buf );

        sprintf(input_name, "%s%d%s", INPUT, i, ".txt");
        sprintf(output_name, "%s%d%s", OUTPUT, i, ".txt");

        sprintf(buf, "./%s < %s > %s", argv[argc-1], input_name, output_name);

        start_time = clock();
        system( buf );
        end_time = clock();

        sprintf(buf, "rm %s", argv[argc-1]);
        system( buf );

        printf("time diff= %lf\n", (float)(end_time-start_time)/CLOCKS_PER_SEC);
    }

    return 0;
}
