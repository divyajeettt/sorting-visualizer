int partition(int arr[], int start, int end)
{
    int temp;
    int pivot = arr[end];  // Always assume pivot as the last element
    int i = start - 1;     // Correct position of the pivot so far

    for (int j=start; j <= end-1; j++)
    {
        if (arr[j] < pivot)
        {
            temp = arr[++i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    temp = arr[i+1];
    arr[i+1] = arr[end];
    arr[end] = temp;

    return (i + 1);
}

void quickSort(int arr[], int start, int end)
{
    if (start >= end)
    {
        return;
    }
    else
    {
        // arr[partitionIndex] is now at the right place
        int partitionIndex = partition(arr, start, end);
        quickSort(arr, start, partitionIndex-1);
        quickSort(arr, partitionIndex+1, end);
    }
}