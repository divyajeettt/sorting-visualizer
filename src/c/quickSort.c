#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

int partition(int *arr, int start, int end, int *swaps, long *idx)
{
    int temp;
    int pivot = arr[end];
    int i = start - 1;

    for (int j=start; j <= end-1; j++)
    {
        if (arr[j] < pivot)
        {
            swaps[(*idx)++] = j;
            swaps[(*idx)++] = ++i;

            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    swaps[(*idx)++] = ++i;
    swaps[(*idx)++] = end;

    temp = arr[i];
    arr[i] = arr[end];
    arr[end] = temp;

    return i;
}

///////////////////////////////////////////////////////////////////////////////

void quickSort(int *arr, int start, int end, int *swaps, long *idx)
{
    if (start >= end)
    {
        return;
    }
    else
    {
        int partitionIndex = partition(arr, start, end, swaps, idx);
        quickSort(arr, start, partitionIndex-1, swaps, idx);
        quickSort(arr, partitionIndex+1, end, swaps, idx);
    }
}

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    static long idx = 0;

    quickSort(arr, 0, n-1, swaps, &idx);

    return swaps;
}