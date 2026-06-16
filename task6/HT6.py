import pygame
import random
from queue import PriorityQueue

pygame.init()

WIDTH = 600
GRID_SIZE = 30
CELL_SIZE = WIDTH // GRID_SIZE

window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A*")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

EMPTY = 0
OBSTACLE = 1
START = 2
END = 3
PATH = 4
VISITED = 5
OPEN = 6


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE
        self.type = EMPTY
        self.neighbors = []

    def reset(self):
        self.type = EMPTY

    def is_start(self):
        return self.type == START

    def is_end(self):
        return self.type == END

    def is_barrier(self):
        return self.type == OBSTACLE

    def make_start(self):
        self.type = START

    def make_end(self):
        self.type = END

    def make_barrier(self):
        self.type = OBSTACLE

    def make_path(self):
        self.type = PATH

    def make_visited(self):
        self.type = VISITED

    def make_open(self):
        self.type = OPEN

    def update_neighbors(self, grid):
        self.neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            row = self.row + dr
            col = self.col + dc

            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                neighbor = grid[row][col]

                if not neighbor.is_barrier():
                    self.neighbors.append(neighbor)

    def draw(self, win):
        color = WHITE

        if self.type == OBSTACLE:
            color = BLACK
        elif self.type == START:
            color = ORANGE
        elif self.type == END:
            color = TURQUOISE
        elif self.type == PATH:
            color = PURPLE
        elif self.type == VISITED:
            color = RED
        elif self.type == OPEN:
            color = GREEN

        pygame.draw.rect(win, color, (self.x, self.y, CELL_SIZE, CELL_SIZE))


def h(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def make_grid():
    grid = []

    for i in range(GRID_SIZE):
        grid.append([])

        for j in range(GRID_SIZE):
            grid[i].append(Cell(i, j))

    return grid


def draw_grid(win, grid):
    for row in grid:
        for cell in row:
            cell.draw(win)

    for i in range(GRID_SIZE):
        pygame.draw.line(win, GREY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
        pygame.draw.line(win, GREY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH))

    pygame.display.update()


def redraw(grid):
    draw_grid(window, grid)


def reconstruct_path(came_from, current, grid):
    while current in came_from:
        current = came_from[current]

        if not current.is_start():
            current.make_path()

        redraw(grid)


def a_star_algorithm(grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    open_set_hash = {start}
    came_from = {}

    g_score = {}
    f_score = {}

    for row in grid:
        for cell in row:
            g_score[cell] = float("inf")
            f_score[cell] = float("inf")

    g_score[start] = 0
    f_score[start] = h((start.row, start.col), (end.row, end.col))

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, grid)
            start.make_start()
            end.make_end()
            return True

        for neighbor in current.neighbors:
            new_g_score = g_score[current] + 1

            if new_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = new_g_score
                f_score[neighbor] = new_g_score + h(
                    (neighbor.row, neighbor.col),
                    (end.row, end.col)
                )

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)

                    if neighbor != end:
                        neighbor.make_open()

        if current != start:
            current.make_visited()

        redraw(grid)

    return False


def generate_random_grid(grid):
    for row in grid:
        for cell in row:
            cell.reset()

    start_row = random.randint(0, GRID_SIZE - 1)
    start_col = random.randint(0, GRID_SIZE - 1)

    end_row = random.randint(0, GRID_SIZE - 1)
    end_col = random.randint(0, GRID_SIZE - 1)

    while (start_row, start_col) == (end_row, end_col):
        end_row = random.randint(0, GRID_SIZE - 1)
        end_col = random.randint(0, GRID_SIZE - 1)

    start = grid[start_row][start_col]
    end = grid[end_row][end_col]

    start.make_start()
    end.make_end()

    obstacle_count = int(GRID_SIZE * GRID_SIZE * 0.2)

    for _ in range(obstacle_count):
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)

        cell = grid[row][col]

        if not cell.is_start() and not cell.is_end():
            cell.make_barrier()

    return start, end


def main():
    grid = make_grid()
    start, end = generate_random_grid(grid)

    running = True

    while running:
        draw_grid(window, grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                    a_star_algorithm(grid, start, end)

                if event.key == pygame.K_r:
                    grid = make_grid()
                    start, end = generate_random_grid(grid)

    pygame.quit()


main()