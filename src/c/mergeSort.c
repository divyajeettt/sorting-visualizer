void merge(int arr[], int low, int mid, int high)
{
    int i, j, k;
    int n1 = mid - low + 1;
    int n2 = high - mid;

    // make temporary copies of left and right arrays
    int left[n1], right[n2];

    for (int p=0; p < n1; p++)
        left[p] = arr[low + p];

    for (int q=0; q < n2; q++)
        right[q] = arr[mid + q + 1];

    i = j = 0;
    // i, j are index pointers for left[], right[]
    // k is the index pointer index of merged subarray

    for (k=low; i<n1 && j<n2; k++)
    {
        if (left[i] <= right[j])
        {
            arr[k] = left[i++];
        }
        else
        {
            arr[k] = right[j++];
        }
    }

    // copy remaining elements of left[]
    while (i < n1)
    {
        arr[k++] = left[i++];
    }

    // copy remaining elements of right[]
    while (j < n2)
    {
        arr[k++] = right[j++];
    }
}

///////////////////////////////////////////////////////////////////////////////

void mergeSort(int arr[], int start, int end)
{
    if (start >= end)
    {
        return;
    }
    else
    {
        int mid = (start + end) / 2;
        mergeSort(arr, start, mid);
        mergeSort(arr, mid+1, end);
        merge(arr, start, mid, end);
    }
}