#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    for (int i=1; i <= n/2; i++)
    {
        for (int j=i-1; j < n-i; j++)
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

        for (int j=n-i-1; j >= i; j--)
        {
            if (arr[j-1] > arr[j])
            {
                swaps[idx++] = j;
                swaps[idx++] = j - 1;

                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }
        }
    }

    return swaps;
}