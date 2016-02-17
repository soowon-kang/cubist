#include <stdio.h>
#include <string.h>

int main(int argc, char** argv){
    int i;
    int test_case;

    char p_dir[80];
    char mode[80];
    char buf[80];
    FILE* fout;

    printf("What is the path of problem directory? ");
    scanf("%79s", p_dir);

    printf("What is the mode? (input/sol) ");
    scanf("%79s", mode);

    printf("How many files do you want to make? ");
    scanf("%d", &test_case);

    for (i=0; i<test_case; i++){
        sprintf(buf, "%s/%s%d.txt", p_dir, mode, i);
        fout = fopen(buf, "w");

        printf("Start %s%d.txt data input! (\\n for END)\n", mode, i);
        while( 1 ){
            rewind(stdin);
            fgets(buf, sizeof(buf)-1, stdin);
            buf[ strlen(buf) ] = '\0';
            if (buf[0] == '\n' )
                break;
            fprintf(fout, "%s", buf);
        }

        fclose( fout);
    }
    return 0;
}
