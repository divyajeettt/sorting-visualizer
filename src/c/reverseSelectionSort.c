void sort(int arr[], int n) {
    int maxIndex, max, temp;

    for (int i=n-1; i > -1; i--)
    {
        max = arr[i];
        maxIndex = i;

        for (int j=0; j < i; j++)
        {
            if (arr[j] > max)
            {
                max = arr[j];
                maxIndex = j;
            }
        }

        if (maxIndex != i)
        {
            temp = arr[i];
            arr[i] = arr[maxIndex];
            arr[maxIndex] = temp;
        }
    }
}