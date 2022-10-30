#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////

int *sort(int *arr, int n)
{
    int *swaps = (int *) calloc(2*n*n, sizeof(int));
    long idx = 0;

    for (int start=0; start < n-1; start++)
    {
        int key = arr[start];
        int loc = start;
        for (int i=start+1; i < n; i++)
        {
            if (arr[i] < key)
            {
                swaps[idx++] = loc;
                swaps[idx++] = loc++;
            }
        }

        if (loc == start)
        {
            continue;
        }

        while (key == arr[loc])
        {
            swaps[idx++] = loc;
            swaps[idx++] = loc++;
        }

        if (loc != start)
        {
            int temp = key;
            key = arr[loc];
            arr[loc] = temp;

            swaps[idx++] = loc;
            swaps[idx++] = start;
        }

        while (loc != start)
        {
            loc = start;
            for (int i=start+1; i < n; i++)
            {
                if (arr[i] < key)
                {
                    swaps[idx++] = loc;
                    swaps[idx++] = loc++;
                }
            }

            while (key == arr[loc])
            {
                swaps[idx++] = loc;
                swaps[idx++] = loc++;
            }

            if (key != arr[loc])
            {
                int temp = key;
                key = arr[loc];
                arr[loc] = temp;

                swaps[idx++] = loc;
                swaps[idx++] = start;
            }
        }
    }

    return swaps;
}