import pygame

pygame.init()

# ----------------- SETTINGS -----------------


WIDTH = 1920
HEIGHT = 1080
CELL_SIZE = 30

cols = WIDTH // CELL_SIZE  
rows = HEIGHT // CELL_SIZE


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life - Draw & Play")
clock = pygame.time.Clock()

# Empty grid at start
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Font for PAUSED text
font = pygame.font.SysFont('Arial', 50)

# Optional: load small pause icon (replace 'pause_icon.png' with your file)
# Make sure the image exists in your working directory
try:
    pause_icon = pygame.image.load('pause_icon.png')
    pause_icon = pygame.transform.scale(pause_icon, (50, 50))  # resize
except:
    pause_icon = None  # fallback if no image

# ----------------- FUNCTIONS -----------------
def count_neighbors(x, y):
    total = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                total += grid[nx][ny]
    return total

def next_generation():
    global grid
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(x, y)
            if grid[x][y] == 1 and neighbors in [2, 3]:
                new_grid[x][y] = 1
            elif grid[x][y] == 0 and neighbors == 3:
                new_grid[x][y] = 1
    grid = new_grid

# ----------------- MAIN LOOP -----------------
running = True
paused = True  # Start paused (drawing mode)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Toggle pause/play with SPACE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    # Draw / erase cells with mouse ONLY when paused
    if paused:
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # Left click = draw
            mx, my = pygame.mouse.get_pos()
            y = mx // CELL_SIZE
            x = my // CELL_SIZE
            if 0 <= x < rows and 0 <= y < cols:
                grid[x][y] = 1
        if mouse_buttons[2]:  # Right click = erase
            mx, my = pygame.mouse.get_pos()
            y = mx // CELL_SIZE
            x = my // CELL_SIZE
            if 0 <= x < rows and 0 <= y < cols:
                grid[x][y] = 0

    # Update simulation only when unpaused
    if not paused:
        next_generation()

    # Draw grid
    screen.fill((0, 0, 0))
    for x in range(rows):
        for y in range(cols):
            color = (0, 200, 255) if grid[x][y] else (30, 30, 30)
            pygame.draw.rect(screen, color,
                             (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

    # Draw PAUSED text + icon if paused
    if paused:
        text_surface = font.render('PAUSED', True, (255, 50, 50))
        screen.blit(text_surface, (10, 10))
        if pause_icon:
            screen.blit(pause_icon, (10, 70))  # below text

    pygame.display.flip()
    clock.tick(5)  # speed (frames per second)

pygame.quit()
