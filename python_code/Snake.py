import pygame
import random

pygame.init()

purple = (210, 210, 230)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
start_color = (0, 153, 153)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
# snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score: int) -> None:
    value = score_font.render("Score: " + str(score), True, purple)
    dis.blit(value, [0, 0])


def random_food(length) -> float:
    return round(random.randrange(0, length - snake_block) / 10.0) * 10.0


def our_snake(snake_block, snake_list) -> None:
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])


def message(msg, color, extra) -> None:
    words = font_style.render(msg, True, color)
    dis.blit(words, [dis_width / 6, dis_height / 3 + extra])


def start_screen() -> None:
    start = True
    while start:
        dis.fill(start_color)
        message("Snake Game!", black, 0)
        message("Press E-easy mode or H-hard mode", black, 35)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    snake_speed = 15
                    play_game(snake_speed)
                if event.key == pygame.K_h:
                    snake_speed = 30
                    play_game(snake_speed)


def play_game(snake_speed: int) -> None:
    # pygame.display.update()

    playing = True
    game_over = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = random_food(dis_width)
    food_y = random_food(dis_height)

    while playing:

        while game_over:
            dis.fill(black)
            message("You Lost!", red, 0)
            message("Press P-Play Again or Q-Quit", red, 30)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        playing = False
                        game_over = False
                    if event.key == pygame.K_p:
                        start_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = random_food(dis_width)
            food_y = random_food(dis_height)
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


start_screen()
