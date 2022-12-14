#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

void merge(int *arr, int low, int mid, int high, int *build, long *idx)
{
    int i, j, k;
    int n1 = mid - low + 1;
    int n2 = high - mid;

    int left[n1], right[n2];

    for (int p=0; p < n1; p++)
    {
        build[(*idx)++] = low + p;
        build[(*idx)++] = arr[low + p];
        left[p] = arr[low + p];
    }

    for (int q=0; q < n2; q++)
    {
        build[(*idx)++] = mid + q + 1;
        build[(*idx)++] = arr[mid + q + 1];
        right[q] = arr[mid + q + 1];
    }

    i = j = 0;
    for (k=low; i<n1 && j<n2; k++)
    {
        build[(*idx)++] = k;
        if (left[i] <= right[j])
        {
            build[(*idx)++] = left[i];
            arr[k] = left[i++];
        }
        else
        {
            build[(*idx)++] = right[j];
            arr[k] = right[j++];
        }
    }

    while (i < n1)
    {
        build[(*idx)++] = k;
        build[(*idx)++] = left[i];
        arr[k++] = left[i++];
    }

    while (j < n2)
    {
        build[(*idx)++] = k;
        build[(*idx)++] = right[j];
        arr[k++] = right[j++];
    }
}

///////////////////////////////////////////////////////////////////////////////

void insertionSort(int *arr, int low, int high, int *swaps, long *idx)
{
    for (int i=low+1; i <= high; i++)
    {
        int j = i;
        while (j > low && arr[j] < arr[j - 1])
        {
            swaps[(*idx)++] = j;
            swaps[(*idx)++] = j - 1;

            int temp = arr[j];
            arr[j] = arr[j - 1];
            arr[--j] = temp;
        }
    }
}

///////////////////////////////////////////////////////////////////////////////

int min(int x, int y)
{
    return ((x < y) ? x : y);
}

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    int RUN = (n < 300) ? 32 : 64;

    for (int i=0; i < n; i += RUN)
    {
        insertionSort(arr, i, min(i+RUN-1, n-1), swaps, &idx);
    }

    swaps[idx++] = -1;
    swaps[idx++] = -1;

    for (int size=RUN; size < n; size *= 2)
    {
        for (int left=0; left < n; left += 2*size)
        {
            int mid = left + size - 1;
            int right = min(left + 2*size - 1, n-1);
            if (mid < right)
            {
                merge(arr, left, mid, right, swaps, &idx);
            }
        }
    }

    return swaps;
}