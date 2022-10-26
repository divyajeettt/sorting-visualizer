#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

void heapify(int *arr, int i, int n, int *swaps, long *idx) {
    int end = n - 1;
    while (i <= (end-1)/2)
    {
        int max = i;
        if (arr[max] < arr[2*i + 1])
        {
            max = 2*i + 1;
        }
        if (2*i + 2 <= end && arr[max] < arr[2*i + 2])
        {
            max = 2*i + 2;
        }
        if (max == i)
        {
            break;
        }

        swaps[(*idx)++] = i;
        swaps[(*idx)++] = max;

        int temp = arr[max];
        arr[max] = arr[i];
        arr[i] = temp;
        i = max;
    }
}

///////////////////////////////////////////////////////////////////////////////

void extractMax(int *arr, int n, int *swaps, long *idx)
{
    swaps[(*idx)++] = 0;
    swaps[(*idx)++] = n - 1;

    int temp = arr[0];
    arr[0] = arr[n - 1];
    arr[n - 1] = temp;

    heapify(arr, 0, n-2, swaps, idx);
}

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    // heapify the array
    for (int i=n-1; i >=0; i--)
    {
        heapify(arr, i, n, swaps, &idx);
    }

    // // keep extracting the Maximum from the heap
    for (int i=n; i > 1; i--)
    {
        extractMax(arr, i, swaps, &idx);
    }

    return swaps;
}