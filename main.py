import pygame


NUM: int = 625               # number of rectangle samples
SIDE: float = 625.0          # side of the main window
WIDTH: float = SIDE / NUM    # width of each rectangle

WINDOW = pygame.display.set_mode((SIDE+200, SIDE+5))
FPS: int = 60

SAMPLES: list[pygame.Rect] = [
    pygame.Rect(WIDTH*i-1, 0, WIDTH, i) for i in range(NUM)
]

pygame.display.set_caption("Sorting-Visualizer")

