#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    for (int i=1; i < n; i++)
    {
        int j = i;
        while (j > 0 && arr[j] < arr[j - 1])
        {
            swaps[idx++] = j;
            swaps[idx++] = j - 1;

            int temp = arr[j];
            arr[j] = arr[j - 1];
            arr[--j] = temp;
        }
    }

    return swaps;
}