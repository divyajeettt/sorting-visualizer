# sorting-visualizer

## About sorting-visualizer

sorting-visualizer is a visualizer for the most popular sorting algorithms built using [`pygame`](https://www.pygame.org/docs/) in Python. It is a graphical-user interface based project.

The project sorts an array of *rectangles* (`pygame.rect()`) of increasing lengths (in ascending order). Before each trial, the array must be shuffled. The sorting algorithm can also be changed.

## Where the 'sorting-visualization' happens

The visualizer is built using an interface between Python and C (using the [`ctypes`](https://docs.python.org/3/library/ctypes.html) package). After the rectangles are shuffled, an array of their heights is passed to the chosen C-sorting function. The custom sorting function sorts it, and returns the combinations of traversals/swaps one needs to do to sort the list. These are then passed to the pygame visualization functions to draw on the screen.

The Python-C interface can be found on [Line 142](https://github.com/divyajeettt/sorting-visualizer/blob/96a5f39d092d4097adaaf4174b9a744363f862b3/src/py/main.py#L142) of `main.py`:

```py
def sort_samples(algorithm: int, heights: list[int]) -> list[list[int]]:
    c_array = (ctypes.c_int * NUM)(*heights)

    SORTING_LIBS[algorithm].sort.argtypes = (ctypes.POINTER(ctypes.c_int * NUM), ctypes.c_int)
    SORTING_LIBS[algorithm].sort.restype = ctypes.POINTER(ctypes.c_int * 2*NUM**2)

    swaps_ptr = SORTING_LIBS[algorithm].sort(c_array, ctypes.c_int(NUM))
    swaps_list: list[list[int]] = []

    for i in swaps_ptr.contents:
        if i[0] == i[1] == 0:
            continue
        swaps_list.append([i[0], i[1]])

    return swaps_list
```

## Features

The following features are provided in the visualizer:

- Ability to shuffle the samples any number of times before sorting
- Ability to change the sorting algorithm before each trial

## Sorting Agorithms implemented

Currently, twelve different popular sorting algorithms are supported. These are:

- [Bubble Sort](https://en.wikipedia.org/wiki/Bubble_sort)
- [Cocktail Shaker Sort](https://en.wikipedia.org/wiki/Cocktail_shaker_sort)
- [Cycle Sort](https://en.wikipedia.org/wiki/Cycle_sort)
- [Odd Even Sort](https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort)
- [Selection Sort](https://en.wikipedia.org/wiki/Selection_sort)
- [Reverse Selection Sort](https://en.wikipedia.org/wiki/Selection_sort#Variants): Selection Sort in reverse
- [Double Selection Sort](https://en.wikipedia.org/wiki/Selection_sort#Variants): Bidirectional Selection Sort
- [Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort)
- [Quick Sort](https://en.wikipedia.org/wiki/Quicksort) using the [Lomuto Partition Scheme](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme)
- [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort) using the [Top-Down Implementation](https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation)
- [Heap Sort](https://en.wikipedia.org/wiki/Heapsort) using the [Floyd's Heap Construction Algorithm](https://en.wikipedia.org/wiki/Heapsort#Floyd's_heap_construction)
- [Tim Sort](https://en.wikipedia.org/wiki/Timsort) using above mentioned Insertion and Merge

## Controls

- Space: Shuffle the samples
- Enter: Start the sorting algorithm
- S: Change the sorting algorithm
- R: Arrange the samples in reverse order of sorting

## Footnotes

- **Do not close** the application while the algorithmis being visualized as ongoing system processes may cause the app to crash.
- The algorithm *cannot be changed* while the samples are being sorted.
- The samples *cannot be sorted* when they are already in sorted order.

## Run

To run the visualizer, clone the repository on your device, navigate to the folder, and execute:

```
make
python3 ./src/py/main.py
```

## Future Plans

- Ability to select ascending/descending order for sorting
- Add more interesting algorithms (non-exhasutively):
  - [Comb Sort](https://en.wikipedia.org/wiki/Comb_sort)
  - [Smooth Sort](https://en.wikipedia.org/wiki/Smoothsort)
- Ability to dynamically change the number of samples
- Speed up the visualization process if possible
- Add a timer/counter that counts the time elapsed in sorting, the number of array traversals, and the number of swaps (difficult to implement due to Python-C interfacing)
