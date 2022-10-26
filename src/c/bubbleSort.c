#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    for (int i=0; i < n; i++)
    {
        for (int j=0; j < n-i-1; j++)
        {
            if (arr[j+1] < arr[j])
            {
                swaps[idx++] = j;
                swaps[idx++] = j + 1;

                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    return swaps;
}