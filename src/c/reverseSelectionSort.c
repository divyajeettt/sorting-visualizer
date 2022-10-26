#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n) {
    int maxIndex, max, temp;

    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    for (int i=n-1; i > -1; i--)
    {
        max = arr[i];
        maxIndex = i;

        for (int j=0; j < i; j++)
        {
            swaps[idx++] = j;
            swaps[idx++] = j;

            if (arr[j] > max)
            {
                max = arr[j];
                maxIndex = j;
            }
        }

        if (maxIndex != i)
        {
            swaps[idx++] = i;
            swaps[idx++] = maxIndex;

            temp = arr[i];
            arr[i] = arr[maxIndex];
            arr[maxIndex] = temp;
        }
    }

    return swaps;
}