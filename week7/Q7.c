// Simulate RIP-like behavior for 3 rounds
// command to run 
// compile gcc Q7.c -o Q7
// run .\Q7.exe
#include <stdio.h>

int main()
{
    int a[3][3] = {
        {0, 1, 3},
        {1, 0, 999},
        {3, 999, 0}
    };

    int i, j, k, round;

    for(round = 1; round <= 3; round++)
    {
        for(i = 0; i < 3; i++)
        {
            for(j = 0; j < 3; j++)
            {
                for(k = 0; k < 3; k++)
                {
                    if(a[i][k] + a[k][j] < a[i][j])
                    {
                        a[i][j] = a[i][k] + a[k][j];
                    }
                }
            }
        }

        printf("\nRound %d\n", round);

        for(i = 0; i < 3; i++)
        {
            for(j = 0; j < 3; j++)
            {
                if(a[i][j] == 999)
                    printf("INF ");
                else
                    printf("%d ", a[i][j]);
            }

            printf("\n");
        }
    }

    return 0;
}


