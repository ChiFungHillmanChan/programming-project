import pygame
import os 
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()

#Local veriable 
FPS = 60
WIDTH = 864
HEIGHT = 936
GRAVITY = 10
GAME_SIZE = 768
PIPE_GAP = 100
MILLISECOND = 1000

#font for score
font = pygame.font.SysFont('Bauhaus 93', 60)

#window screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

#load images
bg = pygame.image.load(os.path.join("assets", "bg.png"))
ground = pygame.image.load(os.path.join("assets", "ground.png"))
button_img = pygame.image.load(os.path.join("assets", "restart.png"))

#classes
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(os.path.join("assets", f"bird{num}.png"))
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False
    
    def update(self, game_over):
        self.vel += 0.5
        if self.vel > GRAVITY:
            self.vel = GRAVITY
        if self.rect.bottom < GAME_SIZE:
            self.rect.y += int(self.vel)

        #jump cannot hold 
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            self.vel = -GRAVITY
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #handle eanimation
        self.counter += 1
        flappy_cooldown = 5

        if self.counter > flappy_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        #rotate the bird when up and down
        if not game_over:
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("assets", "pipe.png"))
        self.rect = self.image.get_rect()

        #position 1 is from top, -1 is from the bottom 
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - (PIPE_GAP)]
        if position == -1:
            self.rect.topleft = [x, y + (PIPE_GAP)]

    def update(self, scroll_speed):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        #check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        #draw button
        WIN.blit(self.image, (self.rect.x, self.rect.y))

        return action

#text for score
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))

#main function
def main():
    run = True

    #variables
    ground_scroll = 0
    scroll_speed = 4
    flying = False
    game_over = False

    pipe_frequency = 1.5 * MILLISECOND
    last_pipe = pygame.time.get_ticks() - pipe_frequency

    score = 0
    pass_pipe = False
    #bird variable
    bird_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()

    flappy = Bird(100, int(HEIGHT / 2))
    bird_group.add(flappy)

    button = Button(WIDTH//2 - 50, HEIGHT // 2 - 100, button_img)

    
    while run:

        #clock tick and window screen
        clock.tick(FPS)
        WIN.blit(bg, (0,0))

        #ground image
        bird_group.draw(WIN)
        pipe_group.draw(WIN)
        WIN.blit(ground, (ground_scroll, GAME_SIZE))

        #check lose
        if flappy.rect.bottom >= GAME_SIZE:
            game_over = True
            flying = False

        #hit top or hit pipe
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
            game_over = True

        # execption
        if not game_over and flying:
            #generate pipes with random number
            pipe_height = random.randint(-100, 100)
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                btm_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, -1)
                top_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, 1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)

                last_pipe = time_now
            #scroll ground if not losing 
            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 35:
                ground_scroll = 0
            #update the pipe
            pipe_group.update(scroll_speed)

        elif game_over:
            bird_group.update(game_over)
            if button.draw():
                game_over = False

                #reset game
                pipe_group.empty()
                flappy.rect.x = 100
                flappy.rect.y = int(HEIGHT / 2)
                flappy.vel = 0
                score = 0
                bird_group.update(game_over)
        
        #bird place
        if flying:
            bird_group.update(game_over)  

        #check score 
        if len(pipe_group) > 0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                and pass_pipe == False:
                pass_pipe = True
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False
        draw_text(str(score), font, (255,255,255), int(WIDTH / 2), 20)

        #close game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not flying  and  not game_over:
                flying = True
        
        #update always at last
        pygame.display.update()

    #quit game
    pygame.quit()

main()