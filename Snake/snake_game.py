import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colours
snake_colour = (216, 239, 211)
food_colour = (250, 112, 112)
background_colour = (69, 71, 75)
white = (255, 255, 255)
black = (0, 0, 0)

# Screen Dimensions
dis_width, dis_height = 800, 600

# Create display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Cooper Smith')

# Create display
clock = pygame.time.Clock()
snake_block, snake_speed = 20, 15

# Font style
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# High score tracking
high_score = 0


def display_score(score):
    # Render and display the current score
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])


def display_high_score(score):
    # Render and display the high score
    value = score_font.render("High Score: " + str(score), True, white)
    dis.blit(value, [dis_width - 200, 0])


def our_snake(snake_block, snake_list):
    # Draw each part of the snake with smooth edges
    for x in snake_list:
        pygame.draw.rect(dis, snake_colour, [x[0], x[1], snake_block, snake_block], border_radius=4)


def message(msg, colour):
    # Display a message in the center of the screen
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def game_over_animation():
    # Simple game over animation with flashing screen
    for _ in range(5):
        dis.fill(food_colour)
        pygame.display.update()
        time.sleep(0.1)
        dis.fill(background_colour)
        pygame.display.update()
        time.sleep(0.1)


def start_screen():
    # Display start screen with options to start or quit
    while True:
        dis.fill(background_colour)
        message("Press C to Start or Q to Quit", white)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


def gameLoop():
    global high_score

    # Initial snake and food positions
    x1, y1 = dis_width / 2, dis_height / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    score = 0
    paused = False

    while True:
        while paused:
            # Pause the game
            message("Paused. Press P to Resume", white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # Control the snake direction
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:
                    paused = True
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over_animation()
            start_screen()

        x1 += x1_change
        y1 += y1_change
        dis.fill(background_colour)
        pygame.draw.rect(dis, food_colour, [foodx, foody, snake_block, snake_block], border_radius=4)

        snake_Head = [x1, y1]
        snake_list.append(snake_Head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_over_animation()
                start_screen()

        our_snake(snake_block, snake_list)
        display_score(score)
        display_high_score(high_score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            score += 10
            if score > high_score:
                high_score = score

        clock.tick(snake_speed)


start_screen()
gameLoop()
