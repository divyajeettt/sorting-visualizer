#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void printSwaps(int *swaps, long count)
{
    for (long i=0; i < count; i++)
    {
        printf("%d ", swaps[i]);
    }
}


int *sort(int *arr, int n)
{
    int *swaps = (int *) malloc(2*n*n * sizeof(int));
    memset(swaps, -1, 2*n*n * sizeof(int));

    long idx = 0;

    for (int i=0; i < n; i++)
    {
        for (int j=0; j < n-i-1; j++)
        {
            if (arr[j+1] < arr[j])
            {
                swaps[idx++] = j;
                swaps[idx++] = j+1;

                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    // printSwaps(swaps, idx);
    // printf("\n\n");
    return swaps;
}