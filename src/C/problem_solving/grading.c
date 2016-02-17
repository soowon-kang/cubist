#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char* INPUT = "input";
char* OUTPUT = "output";
char* SOL = "sol";
int TIMEOVER = 1;
int WRONGANS = 2;

int debug(int);

int main(int argc, char** argv){
    char input[80];
    char output[80];
    char solution[80];
    char path[80];
    char result[80];
    char buf[80];

    int test_case;
    int stat;
    int i;

    double sec;
    double time_limit;

    time_t start_time;
    time_t end_time;

    FILE* fin;
    FILE* fout;

    printf("What is the path of problem directory? ");
    scanf("%s", path);

    printf("How many input files are in the path? ");
    scanf("%d", &test_case);

    printf("What is the time limit (sec)? ");
    scanf("%lf", &time_limit);

    sprintf(buf, "gcc %s/main.c -o %s/main", path, path);
    system( buf );

    sprintf(result, "%s/result.txt", path);

    stat = 0;

    for (i=0; i<test_case; i++){

        sprintf(input, "%s/%s%d%s", path, INPUT, i, ".txt");
        sprintf(output, "%s/%s%d%s", path, OUTPUT, i, ".txt");
        sprintf(solution, "%s/%s%d%s", path, SOL, i, ".txt");

        sprintf(buf, "./%s/main < %s > %s", path, input, output);

        start_time = clock();
        system( buf );
        end_time = clock();

        sec = (double)(end_time-start_time)/CLOCKS_PER_SEC;

        sprintf(buf, "diff -q %s %s > %s", output, solution, result);
        system( buf );

        sprintf(buf, "rm %s", output);
        system( buf );

        buf[0] = '\0';
        fin = fopen(result, "r");
        fscanf(fin, "%79[^\n]s", buf);    // string input until meeting '\n'
        fclose( fin );

        if (sec > time_limit){
            stat = TIMEOVER;
            break;
        } else if ( strlen( buf ) > 1 ){
            stat = WRONGANS;
            break;
        }
    }
    sprintf(buf, "rm %s/main", path);
    system( buf );

    /*
    sprintf(buf, "rm %s", result);
    system( buf );
    */

    fout = fopen(result, "w");

    switch (stat){
    case 0:
        fprintf(fout, "Okay! :D\n");
        break;
    case 1:
        fprintf(fout, "Time over :<\n");
        break;
    case 2:
        fprintf(fout, "Wrong answer in file[%d] :(\n", i);
        break;
    default:
        fprintf(fout, "Wrong status, plz ask programmers.\n");
    }

    fclose( fout );

    sprintf(buf, "cat %s", result);
    system( buf );

    return 0;
}

int debug(int n){
    return printf("%d\n", n);
}
