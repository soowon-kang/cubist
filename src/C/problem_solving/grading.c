#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char* INPUT = "input";
char* OUTPUT = "output";
char* SOL = "sol";

const int NONE = 0;
const int TIMEOVER = 1;
const int WRONGANS = 2;
const int CTYPE = 1;
const int PYTYPE = 2;

int debug(int);

int main(int argc, char** argv){
    char input[80];
    char output[80];
    char solution[80];
    char path[80];
    char result[80];
    char buf[200];
    char lang[80];
    char sid[10];
    char spath[80];

    int test_case;
    int stat;
    int i;
    int flag_lang;

    double sec;
    double time_limit;

    time_t start_time;
    time_t end_time;

    FILE* fin;
    FILE* fout;
    FILE* students;

    printf("What is the path of problem directory? ");
    scanf("%s", path);

    printf("How many input files are in the path? ");
    scanf("%d", &test_case);

    printf("What is the time limit (sec)? ");
    scanf("%lf", &time_limit);

    flag_lang = NONE;

    while (flag_lang == NONE){
        printf("What is the language of main test file ('python' or 'C')? ");
        scanf("%s", lang);

        if (strcmp(lang, "C") == 0 || strcmp(lang, "c") == 0){
            flag_lang = CTYPE;
            sprintf(buf, "gcc %s/main.c -o %s/main", path, path);
            system( buf );
        }
        else if (strcmp(lang, "python") == 0 || strcmp(lang, "Python") == 0){
            flag_lang = PYTYPE;
        }
        else {
            printf("Wrong language. Please input right one.\n");
        }
    }

    sprintf(buf, "%s/students.txt", path);
    students = fopen(buf, "r");

    while (fscanf(students, "%8s", sid) != EOF){
        sprintf(spath, "%s/PA2_%s", path, sid);
    sprintf(result, "%s/result.txt", spath);
    stat = NONE;

    for (i=0; i<test_case; i++){
        sprintf(input, "%s/testcase/%s_%d.txt", path, INPUT, i+1);
        sprintf(output, "%s/testcase/%s_%d.txt", path, OUTPUT, i+1);
        sprintf(solution, "%s/%s_%d.txt", spath, SOL, i+1);

        if (flag_lang == CTYPE)
            sprintf(buf, "./%s/main < %s > %s", spath, input, solution);
        else if (flag_lang == PYTYPE)
            sprintf(buf, "python %s/PA2_%s.py %s > %s", spath, sid, input, solution);
        else {
            printf("Wrong status. Program terminates.\n");
            return 1;
        }
    printf("%s\n", buf);

        start_time = clock();
        system( buf );
        end_time = clock();

        sec = (double)(end_time-start_time)/CLOCKS_PER_SEC;

        sprintf(buf, "diff -q %s %s > %s", output, solution, result);
        system( buf );

        /*
        sprintf(buf, "rm %s", solution);
        system( buf );
        */

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
    if (flag_lang == CTYPE){
        sprintf(buf, "rm %s/main", path);
        system( buf );
    }

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
    }

    fclose( students );

    return 0;
}

int debug(int n){
    return printf("%d\n", n);
}
