void sort(int arr[], int n) {
    int minIndex, maxIndex, min, max, temp, i1, i2;

    for (int i=0; i < n/2; i++)
    {
        i1 = i;
        i2 = n - i - 1;

        min = arr[i1]; max = arr[i2];
        minIndex = i1; maxIndex = i2;

        for (int j=i1; j < i2; j++)
        {
            if (arr[j] < min)
            {
                min = arr[j];
                minIndex = j;
            }
            else if (arr[j] > max)
            {
                max = arr[j];
                maxIndex = j;
            }
        }

        if (minIndex != i1)
        {
            temp = arr[i1];
            arr[i1] = arr[minIndex];
            arr[minIndex] = temp;
        }
        if (maxIndex != i2)
        {
            temp = arr[i2];
            arr[i2] = arr[maxIndex];
            arr[maxIndex] = temp;
        }
    }
}