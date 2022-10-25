import pygame
import random


pygame.font.init()


NUM: int = 625               # number of rectangle samples
SIDE: float = 625.0          # side of the main window
WIDTH: float = SIDE / NUM    # width of each rectangle

WINDOW = pygame.display.set_mode((SIDE, SIDE+50))
FPS: int = 60

SAMPLES: list[int] = [
    pygame.Rect(WIDTH*i, 0, WIDTH, i+1) for i in range(NUM)
]

pygame.display.set_caption("Sorting Visualizer")


def randomize_heights() -> None:
    heights = list(range(1, NUM+1))
    random.shuffle(heights)
    for i in range(NUM):
        SAMPLES[i].height = heights[i]


def draw_samples() -> None:
    for i in range(NUM):
        # SAMPLES[i].y = SIDE - SAMPLES[i].height    # this will make the rectangles go from bottom to top
        pygame.draw.rect(WINDOW, (255, 255, 255), SAMPLES[i])


def main() -> None:
    clock = pygame.time.Clock()
    RUN = True
    while RUN:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        WINDOW.fill((0, 0, 0))
        draw_samples()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()