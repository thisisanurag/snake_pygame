import pygame
import random

# Game settings
WIDTH = 800
HEIGHT = 600
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake class


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.width = 20
        self.height = 20
        self.direction = random.choice(['up', 'down', 'left', 'right'])

    def move(self):
        x, y = self.body[0]
        if self.direction == 'up':
            y -= 20
        elif self.direction == 'down':
            y += 20
        elif self.direction == 'left':
            x -= 20
        elif self.direction == 'right':
            x += 20

        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, new_direction):
        if new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction
        elif new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction

    def draw(self, screen):
        x, y = self.body[0]
        for (x, y) in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, self.width, self.height))

# Food class


class Food:
    def __init__(self):
        self.x = random.randrange(0, WIDTH, 20)
        self.y = random.randrange(0, HEIGHT, 20)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, 20, 20))

    def newFood(self):
        self.x = random.randrange(0, WIDTH, 20)
        self.y = random.randrange(0, HEIGHT, 20)


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Game variables
snake = Snake()
food = Food()

# Game loop
running = True
while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('up')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('down')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('left')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('right')

    # Check collision with food
    if abs(snake.body[0][0] - food.x) < 20 and abs(snake.body[0][1] - food.y) < 20:
        snake.body.insert(0, snake.body[0])
        # print("NEW FOOD")
        food.newFood()
        # print("NEW FOOD DONE")

    # Check collision with the walls
    if snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT:
        # print("Collision with Walls")
        running = False
    # Move the snake
    snake.move()
    # Check collision with itself
    if snake.body[0] in snake.body[1:]:
        # print(snake.body)
        # print("Collision with self")
        running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw snake and food
    snake.draw(screen)
    food.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit the game
print("QUITTING")
pygame.quit()
