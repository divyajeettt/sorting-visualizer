import pygame


NUM: int = 625               # number of rectangle samples
SIDE: float = 625.0          # side of the main window
WIDTH: float = SIDE / NUM    # width of each rectangle

WINDOW = pygame.display.set_mode((SIDE+200, SIDE+5))
FPS: int = 60

SAMPLES: list[int] = [
    pygame.Rect(WIDTH*i-1, 0, WIDTH, i+1) for i in range(NUM)
]

pygame.display.set_caption("Sorting-Visualizer")


def draw_samples() -> None:
    for i in range(NUM):
        color = (i//255, 100, 100)
        pygame.draw.rect(WINDOW, color, SAMPLES[i])


def main() -> None:
    clock = pygame.time.Clock()

    RUN = True
    while RUN:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        draw_samples()

    pygame.quit()


if "__name__" == "__main__":
    main()