#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int minIndex, min, temp;

    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    for (int i=0; i < n; i++)
    {
        min = arr[i];
        minIndex = i;

        for (int j=i+1; j < n; j++)
        {
            swaps[idx++] = j;
            swaps[idx++] = j;

            if (arr[j] < min)
            {
                min = arr[j];
                minIndex = j;
            }
        }

        if (minIndex != i)
        {
            swaps[idx++] = i;
            swaps[idx++] = minIndex;

            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    return swaps;
}