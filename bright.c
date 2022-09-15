#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#define __version__ 1.0
#define __author__ "MD. ALMAS ALI"

void help();
void author();
void version();

void main(int argc, char *argv[])
{
    // system("clear");
    // printf("%s", argv[1]);
    // printf("%s", argv[2]);
    // printf("%s", argv[3]);

    // printf("%d\n", argc);

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
            cmd = popen("xrandr", "--verbose | awk '/Brightness/ { print $2; exit }'");
            if (cmd == NULL)
            {
                puts("Unable to open process");
            }
            while ((br = fgetc(cmd)) != EOF)
                printf("Brightness: ");
                putchar(br);
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
            isdigit(argv[2]);
            printf("--set %s\n", argv[2]);
        }

        // else if (strcmp(argv[1], "--get") == 0)
        // {
        //     printf("--get %s\n", argv[2]);

        // }

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
    printf("    --set <persent> - To set brightness level (Ex: 1-100)\n");
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