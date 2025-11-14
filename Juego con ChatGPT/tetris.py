import pygame
import random

# Inicialización
pygame.init()
WIDTH, HEIGHT = 300, 600
BLOCK = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris sencillo")

# Colores
COLORS = [
    (0, 255, 255), (0, 0, 255), (255, 165, 0),
    (255, 255, 0), (0, 255, 0), (128, 0, 128), (255, 0, 0)
]

# Figuras clásicas del Tetris
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0],
     [1, 1, 1]],     # J
    [[0, 0, 1],
     [1, 1, 1]],     # L
    [[1, 1],
     [1, 1]],        # O
    [[0, 1, 1],
     [1, 1, 0]],     # S
    [[0, 1, 0],
     [1, 1, 1]],     # T
    [[1, 1, 0],
     [0, 1, 1]]      # Z
]

class Piece:
    def __init__(self, x, y, shape):
        self.x, self.y = x, y
        self.shape = shape
        self.color = random.choice(COLORS)

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_grid(locked):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
    for (x, y), color in locked.items():
        grid[y][x] = color
    return grid

def valid_space(shape, offset, grid):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = x + off_x
                new_y = y + off_y
                if new_x < 0 or new_x >= 10 or new_y >= 20:
                    return False
                if new_y >= 0 and grid[new_y][new_x] != (0,0,0):
                    return False
    return True

def clear_rows(grid, locked):
    lines = 0
    for y in range(19, -1, -1):
        if (0,0,0) not in grid[y]:
            lines += 1
            del_row = y
            for x in range(10):
                del locked[(x, y)]
    if lines > 0:
        new_locked = {}
        for (x, y), color in locked.items():
            if y < del_row:
                new_locked[(x, y + lines)] = color
            else:
                new_locked[(x, y)] = color
        return new_locked
    return locked

def draw_grid(surface):
    for x in range(10):
        pygame.draw.line(surface, (40,40,40), (x*BLOCK, 0), (x*BLOCK, HEIGHT))
    for y in range(20):
        pygame.draw.line(surface, (40,40,40), (0, y*BLOCK), (WIDTH, y*BLOCK))

def draw_window(surface, grid):
    surface.fill((0,0,0))
    for y in range(20):
        for x in range(10):
            pygame.draw.rect(surface, grid[y][x], 
                             (x*BLOCK, y*BLOCK, BLOCK, BLOCK), 0)
    draw_grid(surface)
    pygame.display.update()

def main():
    locked = {}
    grid = create_grid(locked)
    current_piece = Piece(3, 0, random.choice(SHAPES))
    clock = pygame.time.Clock()
    fall_time = 0
    run = True

    while run:
        grid = create_grid(locked)
        fall_speed = 0.4
        fall_time += clock.get_rawtime()
        clock.tick()

        # Movimiento automático hacia abajo
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece.shape, (current_piece.x, current_piece.y), grid):
                current_piece.y -= 1
                for y, row in enumerate(current_piece.shape):
                    for x, cell in enumerate(row):
                        if cell:
                            locked[(current_piece.x + x, current_piece.y + y)] = current_piece.color
                current_piece = Piece(3, 0, random.choice(SHAPES))
                locked = clear_rows(grid, locked)

        # Eventos del usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if valid_space(current_piece.shape, (current_piece.x - 1, current_piece.y), grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if valid_space(current_piece.shape, (current_piece.x + 1, current_piece.y), grid):
                        current_piece.x += 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece.shape, (current_piece.x, current_piece.y), grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    old_shape = current_piece.shape
                    current_piece.rotate()
                    if not valid_space(current_piece.shape, (current_piece.x, current_piece.y), grid):
                        current_piece.shape = old_shape

        draw_window(screen, grid)

    pygame.quit()

if __name__ == "__main__":
    main()
