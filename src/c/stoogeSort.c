#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

void stoogeSort(int *arr, int start, int end, int *swaps, long *idx)
{
    if (start < end)
    {
        if (arr[start] > arr[end])
        {
            swaps[(*idx)++] = start;
            swaps[(*idx)++] = end;

            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
        }

        if (end-start+1 > 2)
        {
            int t = (end - start + 1) / 3;
            stoogeSort(arr, start, end-t, swaps, idx);
            stoogeSort(arr, start+t, end, swaps, idx);
            stoogeSort(arr, start, end-t, swaps, idx);
        }
    }
}

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    stoogeSort(arr, 0, n-1, swaps, &idx);

    return swaps;
}