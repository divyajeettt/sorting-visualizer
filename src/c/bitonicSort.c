#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

void bitonicMerge(int *arr, int start, int end, int dirn, int *swaps, long *idx)
{
    if (end > 1)
    {
        int mid = end / 2;
        for (int i=start; i < start+mid; i++)
        {
            if (dirn == (arr[i] > arr[i + mid]))
            {
                swaps[(*idx)++] = i;
                swaps[(*idx)++] = i + mid;

                int temp = arr[i];
                arr[i] = arr[i + mid];
                arr[i + mid] = temp;
            }
        }
        bitonicMerge(arr, start, mid, dirn, swaps, idx);
        bitonicMerge(arr, start+mid, mid, dirn, swaps, idx);
    }
}

///////////////////////////////////////////////////////////////////////////////

void bitonicSort(int *arr, int start, int end, int dirn, int *swaps, long *idx)
{
    if (end > 1)
    {
        int mid = end / 2;
        bitonicSort(arr, start, mid, 1, swaps, idx);
        bitonicSort(arr, start+mid, mid, 0, swaps, idx);
        bitonicMerge(arr, start, end, dirn, swaps, idx);
    }
}

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    bitonicSort(arr, 0, n, 1, swaps, &idx);

    return swaps;
}