#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int minIndex, maxIndex, min, max, temp, l;

    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    for (int i=0; i < n/2; i++)
    {
        int j = n - i - 1;

        min = arr[i]; max = arr[i];
        minIndex = i; maxIndex = i;

        for (int k=i; k <= j; k++)
        {
            swaps[idx++] = k;
            swaps[idx++] = k;

            if (arr[k] < min)
            {
                min = arr[k];
                minIndex = k;
            }
            else if (arr[k] > max)
            {
                max = arr[k];
                maxIndex = k;
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

        l = ((arr[minIndex] == max) ? minIndex : maxIndex);

        swaps[idx++] = j;
        swaps[idx++] = l;

        temp = arr[j];
        arr[j] = arr[l];
        arr[l] = temp;
    }

    return swaps;
}