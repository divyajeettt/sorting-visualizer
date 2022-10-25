void selectionSort(int arr[], int n) {
    int minIndex, min, temp;

    for (int i=0; i < n/2; i++)
    {
        min = arr[i];
        minIndex = i;

        for (int j=i+1; j < n; j++)
        {
            if (arr[j] < min)
            {
                min = arr[j];
                minIndex = j;
            }
        }

        if (minIndex != i)
        {
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}