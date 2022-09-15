#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "bright.h"

#define __version__ 1.0
#define __author__ "MD. ALMAS ALI"

void help();
void author();
void version();

void main(int argc, char *argv[])
{

    if (argc == 2)
    {

        if (strcmp(argv[1], "--version") == 0)
        {
            version();
        }

        else if (strcmp(argv[1], "--help") == 0)
        {
            help();
        }

        else if (strcmp(argv[1], "--author") == 0)
        {
            author();
        }

        else if (strcmp(argv[1], "--set") == 0)
        {
            printf("Error: option --set requires an argument\n");
            printf("Try `bright --help' for more options.\n");
        }

        else if (strcmp(argv[1], "--get") == 0)
        {

            FILE *cmd;
            float br;
            char bz[10], bx[10];
            cmd = popen("xrandr --verbose | awk '/Brightness/ { print $2; exit }'", "r");
            if (cmd == NULL)
            {
                puts("Unable to open process");
            }
            while ((br = fgetc(cmd)) != EOF)
            {
                putchar(br);
                ftoa(br, bz, 2);
                strcat(bx, bz);
                // printf("%c", br);
                // float calc = (float)br * 100.0;
            }
            puts(bx);
                // printf("Brightness: %f\n", (float)br * 100.0);
            pclose(cmd);

            // double br = system("xrandr --verbose | awk '/Brightness/ { print $2; exit }'");
            // printf("Brightness: %f\n", br);
        }

        else
        {
            printf("Bright: command not found: %s\n", argv[1]);
        }
    }

    else if (argc == 3)
    {

        if (strcmp(argv[1], "--set") == 0)
        {
            // char input[3] = argv[2];
            int length, i;

            length = strlen(argv[2]);
            for (i = 0; i < length; i++)
            {
                if (!isdigit(argv[2][i]))
                {
                    printf("Error: --set need an number\n");
                    exit(1);
                }
            }

            if (atoi(argv[2]) < 10)
            {
                printf("Warning: screen can be blackout!\n");
                exit(1);
            }
            else if (atoi(argv[2]) > 300)
            {
                printf("Warning: screen can be overbright!\n");
                exit(1);
            }
            else
            {
                float num;
                num = (float)atoi(argv[2]) / 100.0;
                char cm[10];
                ftoa(num, cm, 2);
                char cc[] = "xrandr --output LVDS-1 --brightness ";
                strcat(cc, cm);
                // printf("%s\n", cc);
                system(cc);
            }
        }

        else
        {
            printf("Bright: command not found: %s\n", argv[1]);
        }
    }

    else
    {
        printf("bright: missing OPTION\n");
        printf("Try `bright --help' for more options.\n");
    }
}

void help()
{
    printf("Usage: bright [OPTION]...\n");
    printf("    --set <persent> - To set brightness level (From 10%% to 300%%)\n");
    printf("    --get - To get brightness level\n");
    printf("    --help - To get help\n");
    printf("    --version - To get version\n");
    printf("    --author - To get author information\n");
    printf("\nExample:\n");
    printf("    bright --set 80\n");
    printf("    bright --get\n");
    printf("    bright --help\n");
    printf("    bright --version\n");
    printf("    bright --author\n\n");
    author();
}

void author()
{
    printf("Made by: %s\n", __author__);
}

void version()
{
    printf("%.1f\n", __version__);
}