import pygame
import random
import ctypes
import screens


"""
CONTROLS:

Space: Shuffle the samples
Enter: Start the sorting algorithm
S: Change the sorting algorithm
R: Arrange the samples in reverse order of sorting
"""


pygame.font.init()
screens.main()


# Constants
WINDOW_X: float = 1024.0               # width of the main window
WINDOW_Y: float = 600.0                # height of the main window
NUM: int = int(WINDOW_X)               # number of rectangle samples
WIDTH: float = WINDOW_X / NUM          # width of each rectangle
SLOPE: float = WINDOW_Y / WINDOW_X

# Window and Frame Rate
WINDOW = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
FPS: int = 60

# Set up the Sorting Algorithm
try:
    ALGORITHM: int = screens.algo
except AttributeError:
    ALGORITHM: int = 0       # default algorithm is Bubble Sort

# Create the list of samples
SAMPLES: list[pygame.Rect] = [
    pygame.Rect(WIDTH*i, 0, WIDTH, (i+1)*SLOPE) for i in range(NUM)
]

# Load the Dynamically Linked Libraries
C_BINS: list[str] = [
    r"./bin/dll/bitonicSort.dll",
    r"./bin/dll/bubbleSort.dll",
    r"./bin/dll/cocktailShakerSort.dll",
    r"./bin/dll/cycleSort.dll",
    r"./bin/dll/doubleSelectionSort.dll",
    r"./bin/dll/heapSort.dll",
    r"./bin/dll/insertionSort.dll",
    r"./bin/dll/mergeSort.dll",
    r"./bin/dll/oddEvenSort.dll",
    r"./bin/dll/quickSort.dll",
    r"./bin/dll/reverseSelectionSort.dll",
    r"./bin/dll/selectionSort.dll",
    r"./bin/dll/stoogeSort.dll",
    r"./bin/dll/timSort.dll",
    r"./bin/dll/treeSort.dll",
]

SORTING_LIBS: list[ctypes.CDLL] = [ctypes.CDLL(file) for file in C_BINS]

ALGOS: dict[int, str] = {
    0: "Bitonic Sort",
    1: "Bubble Sort",
    2: "Cocktail Shaker Sort",
    3: "Cycle Sort",
    4: "Double Selection Sort",
    5: "Heap Sort",
    6: "Insertion Sort",
    7: "Merge Sort",
    8: "Odd Even Sort",
    9: "Quick Sort",
    10: "Reverse Selection Sort",
    11: "Selection Sort",
    12: "Stooge Sort",
    13: "Tim Sort",
}

# Colors
RED:   tuple[int, int, int] = (255, 0, 0)
GREEN: tuple[int, int, int] = (0, 255, 0)
BLUE:  tuple[int, int, int] = (0, 0, 255)
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)

# Set the window-title
pygame.display.set_caption(f"Sorting Visualizer: {ALGOS[ALGORITHM]}")


def randomize_heights() -> list[int]:
    for _ in range(NUM):
        i, j = random.randint(0, NUM-1), random.randint(0, NUM-1)
        SAMPLES[i].height, SAMPLES[j].height = SAMPLES[j].height, SAMPLES[i].height

        i, j = random.randint(0, NUM-1), random.randint(0, NUM-1)
        SAMPLES[i].height, SAMPLES[j].height = SAMPLES[j].height, SAMPLES[i].height

        draw_samples()
        pygame.display.update()

    return [sample.height for sample in SAMPLES]


def reverse_samples(samples_sorted: bool) -> list[int]:
    if not samples_sorted:
        for i in range(NUM):
            draw_samples()
            pygame.display.update()
    else:
        for i in range(NUM//2):
            SAMPLES[i].height, SAMPLES[NUM-i-1].height = SAMPLES[NUM-i-1].height, SAMPLES[i].height
            draw_samples()
            pygame.display.update()

    return [sample.height for sample in SAMPLES]


def draw_samples() -> None:
    WINDOW.fill(BLACK)
    for i in range(NUM):
        SAMPLES[i].y = WINDOW_Y - SAMPLES[i].height
        pygame.draw.rect(WINDOW, WHITE, SAMPLES[i])


def draw_sorting(swaps: list[list[int]]) -> None:
    merging = False

    for (i, j) in swaps:
        if i == j == -1:
            merging = True
            continue

        if not merging:
            SAMPLES[i].height, SAMPLES[j].height = SAMPLES[j].height, SAMPLES[i].height
            draw_samples()
            pygame.draw.rect(WINDOW, RED, SAMPLES[i])
            pygame.draw.rect(WINDOW, BLUE, SAMPLES[j])
        else:
            SAMPLES[i].height = j
            draw_samples()
            pygame.draw.rect(WINDOW, GREEN, SAMPLES[i])

        pygame.display.update()


def sort_samples(algorithm: int, heights: list[int]) -> list[list[int]]:
    c_array = (ctypes.c_int * NUM)(*heights)

    SORTING_LIBS[algorithm].sort.argtypes = (ctypes.POINTER(ctypes.c_int * NUM), ctypes.c_int)
    SORTING_LIBS[algorithm].sort.restype = ctypes.POINTER(ctypes.c_int * 2*NUM**2)

    swaps_ptr = SORTING_LIBS[algorithm].sort(c_array, ctypes.c_int(NUM))
    swaps_list: list[list[int]] = []

    for i, long in enumerate(swaps_ptr.contents):
        swap = [long[0], long[1]]
        if i != 0 and swaps_list[-1] == swap == [0, 0]:
            break
        swaps_list.append(swap)

    return swaps_list


def main() -> None:
    global ALGORITHM

    heights = [sample.height for sample in SAMPLES]
    samples_sorted = True

    clock = pygame.time.Clock()
    RUN = True

    while RUN:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    heights = randomize_heights()
                    samples_sorted = False

                if event.key == pygame.K_RETURN:
                    if samples_sorted:
                        continue
                    swaps = sort_samples(ALGORITHM, heights)
                    draw_sorting(swaps)
                    samples_sorted = True

                if event.key == pygame.K_s:
                    screens.main()
                    ALGORITHM = screens.algo
                    pygame.display.set_caption(f"Sorting Visualizer: {ALGOS[ALGORITHM]}")

                if event.key == pygame.K_r:
                    heights = reverse_samples(samples_sorted)
                    samples_sorted = False

        draw_samples()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()