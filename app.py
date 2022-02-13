import pygame
import time
import random

# initializing pygame
pygame.init()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont("ubuntu", 21)
score_font = pygame.font.SysFont("ubuntu", 18)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0,0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size]) # draws pixel at 0,1 on x y axis with the size of snake

def run_game():

    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    # spawning random targets
    target_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0

    while not game_over:

        for event in pygame.even.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size # goes left for negatize size (left is decreasing x coordinate where as down is decreasing y coordinate)
                    y_speed = 0 # cannot move diagonally
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0: # when it hits the borders
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])
        snake_pixels.append([x,y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]