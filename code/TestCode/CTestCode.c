/* Hello World program */

#include<stdio.h>


#include <stdio.h>
#include <stdlib.h>
int main( int argc, char* argv[] )
{
    int Address;
    if (argc > 1)
    {
        Address = atoi(argv[1]);
        printf("%s\n", argv[1]);
    }
    else 
    {
        printf("No arguments passed\n");
        return 1;
    }
    return 0;
}