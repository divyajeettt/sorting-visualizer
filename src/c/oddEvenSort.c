#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    int sorted = 0;
    while (sorted == 0)
    {
        sorted = 1;

        for (int i=1; i < n-1; i += 2)
        {
            if (arr[i+1] < arr[i])
            {
                swaps[idx++] = i;
                swaps[idx++] = i + 1;

                int temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;

                sorted = 0;
            }
        }

        for (int i=0; i < n-1; i += 2)
        {
            if (arr[i+1] < arr[i])
            {
                swaps[idx++] = i;
                swaps[idx++] = i + 1;

                int temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;

                sorted = 0;
            }
        }
    }

    return swaps;
}