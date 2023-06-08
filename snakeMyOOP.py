import pygame, sys, random
from pygame.math import Vector2

pygame.init()

title = pygame.font.Font(None, 60)
score = pygame.font.Font(None, 60)
menu = pygame.font.Font(None, 75)
info = pygame.font.Font(None, 36)

BLUE = (39, 58, 93)
ORANGE = (255, 213,128)
RED = (136, 8, 8)
LIME_GREEN = (50, 205, 50)

FRAME = 75
cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
        self.position = self.random_position()
    
    def draw(self):
        food_rect = pygame.Rect(FRAME + self.position.x * cell_size, FRAME + self.position.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(window, ORANGE, food_rect, 0 , 7)
    
    def random_position(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)

        position = Vector2(x, y)
        return position
    
class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
        self.add_segment = False

    def draw(self):
        for segment in self.body:
            segment_rect = (FRAME + segment.x * cell_size, FRAME + segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(window, RED, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment == True:
            self.add_segment = False
        else:
            self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)     


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.state = "RUNNING"
        self.score = 0


    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        if self.state == "RUNNING" :
            self.snake.update()
            self.food_collision()
            self.out_of_window()
            self.tail_collision()

    def food_collision(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.random_position()
            self.snake.add_segment = True
            self.score += 1
    
    def out_of_window(self):
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()
    
    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.random_position()
        self.state = "STOPPED"
        self.score = 0
    
    def tail_collision(self):
        tail = self.snake.body[1:]
        if self.snake.body[0] in tail:
            self.game_over()

    def show_menu(self):
        menu_options = ["Start Game", "Options", "Quit"]
        option_positions = [(number_of_cells * cell_size // 2 + 75, number_of_cells * cell_size // 2 - 75),
                            (number_of_cells * cell_size // 2 + 75, number_of_cells * cell_size // 2),
                            (number_of_cells * cell_size // 2 + 75, number_of_cells * cell_size // 2 + 75)]
        option_rects = []

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for option_rect in option_rects:
                        if option_rect.collidepoint(mouse_pos):
                            if option_rects.index(option_rect) == 0:
                                return
                            elif option_rects.index(option_rect) == 1:
                                print("To be continued...")
                            elif option_rects.index(option_rect) == 2:
                                pygame.quit()
                                sys.exit()

            window.fill(BLUE)

            option_rects = []
            for option, position in zip(menu_options, option_positions):
                text_surface = menu.render(option, True, ORANGE)
                text_rect = text_surface.get_rect(center=position)
                option_rects.append(text_rect)
                window.blit(text_surface, text_rect)

            pygame.display.flip()
            pygame.event.wait()
    

 
window = pygame.display.set_mode((2 * FRAME + cell_size * number_of_cells, 2 * FRAME + cell_size * number_of_cells))
pygame.display.set_caption("SSSSSnnnaake")
fps_controller = pygame.time.Clock()

game = Game()


SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)



game.show_menu()
while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.state == "STOPPED":
                game.state = "RUNNING"
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0) 
            if event.key == pygame.K_ESCAPE:
                game.snake.reset()
                game.score = 0
                game.show_menu()



    window.fill(BLUE)
    pygame.draw.rect(window, LIME_GREEN, (FRAME - 5, FRAME -5, cell_size * number_of_cells + 10, cell_size * number_of_cells + 10), 5)
    game.draw()
    title_surface = title.render("SSSSSnnnaake", True, ORANGE)
    score_surface = score.render("Score: " + str(game.score), True, ORANGE)
    info_surface = info.render("Press ESC to get to the menu", True, ORANGE)
    window.blit(title_surface, (FRAME - 5, 20))
    window.blit(score_surface, (cell_size * number_of_cells - 100, FRAME - 55))
    window.blit(info_surface, (FRAME, cell_size * number_of_cells  + 100))

    pygame.display.update()
    fps_controller.tick(60)
