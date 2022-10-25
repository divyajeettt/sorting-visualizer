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


NUM: int = 625               # number of rectangle samples
SIDE: float = 625.0          # side of the main window
WIDTH: float = SIDE / NUM    # width of each rectangle

WINDOW = pygame.display.set_mode((SIDE, SIDE))
FPS: int = 60

ALGORITHM: int = screens.algo

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

SORTING_FUNCTIONS: list[ctypes.CDLL] = [ctypes.CDLL(file) for file in C_BINS]

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


def sort_samples(algorithm: int) -> None:
    if algorithm == 1:
        bubble_sort()

    elif algorithm == 2:
        double_selection_sort()

    elif algorithm == 3:
        heap_sort()

    elif algorithm == 4:
        insertion_sort()

    elif algorithm == 5:
        merge_sort()

    elif algorithm == 6:
        quick_sort()

    elif algorithm == 7:
        reverse_selection_sort()

    else:
        selection_sort()


def main() -> None:
    heights = [sample.height for sample in SAMPLES]

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

                if event.key == pygame.K_RETURN:
                    sort_samples(ALGORITHM)

        WINDOW.fill((0, 0, 0))
        draw_samples()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()