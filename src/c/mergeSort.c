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

void mergeSort(int *arr, int start, int end, int *build, long *idx)
{
    if (start >= end)
    {
        return;
    }
    else
    {
        int mid = (start + end) / 2;
        mergeSort(arr, start, mid, build, idx);
        mergeSort(arr, mid+1, end, build, idx);
        merge(arr, start, mid, end, build, idx);
    }
}

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *build = (int *) calloc(2*n*n, sizeof(int));
    static long idx = 0;

    build[idx++] = -1;
    build[idx++] = -1;
    mergeSort(arr, 0, n-1, build, &idx);

    return build;
}