import pygame
import random
import os

pygame.init()
pygame.mixer.init()



# Colors
White = (255, 255, 255)
Red = (255, 0, 0)
Black = (0, 0, 0)
Green = (0, 255, 0)






screen_width = 1200
screen_height = 600



pygame.display.set_caption("Snakes 3.O")
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.update()


# Images
Home_Page = pygame.image.load("Images/SnakeHome.png")
Home_Page = pygame.transform.scale(Home_Page, (screen_width, screen_height)).convert_alpha()
Main_Page = pygame.image.load("Images/SnakeMain.png")
Main_Page = pygame.transform.scale(Main_Page, (screen_width, screen_height)).convert_alpha()
Game_Over_Page = pygame.image.load("Images/Game Over.png")
Game_Over_Page = pygame.transform.scale(Game_Over_Page, (screen_width, screen_height)).convert_alpha()



# Creating some specific variables outside of gameloop
exit_game = False
game_over = False
fps = random.randint(50, 70)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])




def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

snk_list = []
snk_length = 1


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(Black)
        gameWindow.blit(Home_Page, (0, 0))
        text_screen("Welcome to Snakes! Press Enter to Play", Red, 260, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(fps)




# Game Loop
def gameloop():
    # Playing Background Music
    pygame.mixer.music.load("Music/Background.mp3")
    pygame.mixer.music.play(-1)
    # Game Specific variables
    exit_game = False
    game_over = False
    Snake_x = 31
    Snake_y = 34
    snake_size = 25
    fps = random.randint(50, 70)
    clock = pygame.time.Clock()
    init_velocity = 6
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(225, 450)
    food_y = random.randint(150, 300)
    score = 0
    snk_list = []
    snk_length = 1
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            hiscore = f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    food_range = 18
    font = pygame.font.SysFont(None, 55)
    while not exit_game:
        if game_over:
            gameWindow.fill(Red)
            gameWindow.blit(Game_Over_Page, (0, 0))
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))


            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    exit_game = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    

                    if event.key == pygame.K_q:
                        score+=10
                        snk_length+=5
                    

                    if event.key == pygame.K_RCTRL:
                        food_range = 18
                    

                    if event.key == pygame.K_LCTRL:
                        food_range = 36
                    

                    



            Snake_x += velocity_x
            Snake_y += velocity_y


            if abs(Snake_x - food_x)<food_range and abs(Snake_y - food_y)<food_range:
                score +=10
                food_x = random.randint(50, 1000)
                food_y = random.randint(20, 550)
                snk_length+=5
                if score>int(hiscore):
                    hiscore = score
            



            gameWindow.fill(Black)
            gameWindow.blit(Main_Page, (0, 0))
            text_screen("Score: "+ str(score), Red, 5, 5)
            text_screen("Score: "+ str(score), Red, 5, 5)
            text_screen("High Score: "+ str(hiscore), Red, 350, 5)
            pygame.draw.rect(gameWindow, Green, [food_x, food_y, snake_size, snake_size])
            text_screen("FPS: "+ str(fps), Red, 5, 55)
            text_screen("X: "+ str(Snake_x), Red, 1060, 5)
            text_screen("Y: "+ str(Snake_y), Red, 1060, 55)

            head = []
            head.append(Snake_x)
            head.append(Snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            


            if head in snk_list[:-1]:
                # Playing Game Over Music
                pygame.mixer.music.load("Music/Big Explosion Cut Off.mp3")
                pygame.mixer.music.play(-1)
                game_over = True
                
            if Snake_x<0 or Snake_x>screen_width or Snake_y<0 or Snake_y>screen_height:
                # Playing Game Over Music
                pygame.mixer.music.load("Music/Big Explosion Cut Off.mp3")
                pygame.mixer.music.play(-1)
                game_over = True
            
            



            plot_snake(gameWindow, Red, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()
