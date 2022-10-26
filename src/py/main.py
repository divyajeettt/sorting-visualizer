import pygame
import random
import ctypes
import screens


"""
CONTROLS:

Space: Shuffle the samples
Enter: Start the sorting algorithm
"""


pygame.font.init()
screens.main()


NUM: int = 300               # number of rectangle samples
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
    r"./bin/dll/doubleSelectionSort.dll",
    r"./bin/dll/heapSort.dll",
    r"./bin/dll/insertionSort.dll",
    r"./bin/dll/mergeSort.dll",
    r"./bin/dll/quickSort.dll",
    r"./bin/dll/reverseSelectionSort.dll",
    r"./bin/dll/selectionSort.dll",
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
    for i in range(NUM):
        # this will make the rectangles go from bottom to top
        # SAMPLES[i].y = SIDE - SAMPLES[i].height
        pygame.draw.rect(WINDOW, (255, 255, 255), SAMPLES[i])


def draw_sorting(swaps: list[list[int]]) -> None:
    for (i, j) in swaps:
        SAMPLES[i].height, SAMPLES[j].height = SAMPLES[j].height, SAMPLES[i].height
        WINDOW.fill((0, 0, 0))
        draw_samples()
        # pygame.draw.rect(WINDOW, (255, 255, 255), SAMPLES[i])
        # pygame.draw.rect(WINDOW, (255, 255, 255), SAMPLES[i])
        pygame.display.update()


def sort_samples(algorithm: int, heights: list[int]) -> list[list[int]]:
    c_array = (ctypes.c_int * NUM)(*heights)

    SORTING_LIBS[algorithm].sort.argtypes = (ctypes.POINTER(ctypes.c_int * NUM), ctypes.c_int)
    SORTING_LIBS[algorithm].sort.restype = ctypes.POINTER(ctypes.c_int * 2*NUM**2)

    swaps_ptr = SORTING_LIBS[algorithm].sort(c_array, ctypes.c_int(NUM))

    swaps_list: list[list[int]] = []
    for i in swaps_ptr.contents:
        if i[0] == i[1] == -1:
            break
        swaps_list.append([i[0], i[1]])

    return swaps_list


def main() -> None:
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

        WINDOW.fill((0, 0, 0))
        draw_samples()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()