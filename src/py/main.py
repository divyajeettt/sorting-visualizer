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


NUM: int = 625               # number of rectangle samples
SIDE: float = 625.0          # side of the main window
WIDTH: float = SIDE / NUM    # width of each rectangle

WINDOW = pygame.display.set_mode((SIDE, SIDE))
FPS: int = 60

try:
    ALGORITHM: int = screens.algo
except AttributeError:
    ALGORITHM: int = 0       # default algorithm is Bubble Sort

SAMPLES: list[int] = [
    pygame.Rect(WIDTH*i, 0, WIDTH, i+1) for i in range(NUM)
]

C_BINS: list[str] = [
    r"./bin/dll/bubbleSort.dll",
    r"./bin/dll/cocktailShakerSort.dll",
    r"./bin/dll/doubleSelectionSort.dll",
    r"./bin/dll/heapSort.dll",
    r"./bin/dll/insertionSort.dll",
    r"./bin/dll/mergeSort.dll",
    r"./bin/dll/quickSort.dll",
    r"./bin/dll/reverseSelectionSort.dll",
    r"./bin/dll/selectionSort.dll",
    r"./bin/dll/timSort.dll",
]

SORTING_LIBS: list[ctypes.CDLL] = [ctypes.CDLL(file) for file in C_BINS]

pygame.display.set_caption("Sorting Visualizer")


def randomize_heights() -> list[int]:
    heights = list(range(1, NUM+1))
    random.shuffle(heights)

    for i in range(NUM):
        SAMPLES[i].height = heights[i]

    return heights


def draw_samples() -> None:
    WINDOW.fill((0, 0, 0))
    for i in range(NUM):
        pygame.draw.rect(WINDOW, (255, 255, 255), SAMPLES[i])


def draw_sorting(swaps: list[list[int]]) -> None:
    merging = False

    for (i, j) in swaps:
        if i == j == -1:
            merging = True

        if not merging:
            SAMPLES[i].height, SAMPLES[j].height = SAMPLES[j].height, SAMPLES[i].height

            draw_samples()
            copy_i, copy_j = SAMPLES[i].copy(), SAMPLES[j].copy()
            copy_i.width = copy_j.width = 2.5

            pygame.draw.rect(WINDOW, (255, 0, 0), copy_i)
            pygame.draw.rect(WINDOW, (0, 0, 255), copy_j)

        else:
            SAMPLES[i].height = j

            draw_samples()
            copy_i = SAMPLES[i].copy()
            copy_i.width = 2.5

            pygame.draw.rect(WINDOW, (255, 0, 0) if i%2 else (0, 0, 255), copy_i)

        pygame.display.update()


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

                if event.key == pygame.K_r:
                    heights = list(range(NUM, 0, -1))
                    for i in range(NUM):
                        SAMPLES[i].height = heights[i]
                    samples_sorted = False

        draw_samples()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()