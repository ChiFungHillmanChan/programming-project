import pygame
import pickle
from pygame.locals import *
import os

pygame.init()
clock = pygame.time.Clock()
FPS = 60

GAME_OVER = -1
MAX_LEVEL = 3
tile_size = 40
rows = 25
cols = 16 
margin = 40
WIDTH = 1000  #1000
HEIGHT = 640 # 640
PLAYER_SIZE = 26

#define game
game_over = 0
game_over_count = 0
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I wanna")

game_menu = True
save_point = [0, 0]

def load_level_map():
    world_data = []
    if os.path.exists(f'level{level}'):
        pickle_in = open(f'level{level}', 'rb')
        world_data = pickle.load(pickle_in)
        return world_data

level = 1
saved_level = 1

player_vel = 3

#load images
apple_img = pygame.image.load( os.path.join("assets", "traps/apple.png"))
banana_img = pygame.image.load( os.path.join("assets", "traps/banana.png"))
square_img = pygame.image.load( os.path.join("assets", "traps/square.png"))
trap_down_img = pygame.image.load( os.path.join("assets", "traps/trap_down.png"))
trap_left_img = pygame.image.load( os.path.join("assets", "traps/trap_left.png"))
trap_top_img = pygame.image.load( os.path.join("assets", "traps/trap_top.png"))
trap_right_img = pygame.image.load( os.path.join("assets", "traps/trap_right.png"))
glass_block_img = pygame.image.load( os.path.join("assets", "traps/glass_block.png"))
noglass_block_img = pygame.image.load( os.path.join("assets", "traps/noglass_block.png"))
long_bar_img = pygame.image.load( os.path.join("assets", "traps/long_bar.png"))

#click btn
save_img = pygame.image.load( os.path.join("assets", "level_edit/save_btn.png"))
load_img = pygame.image.load( os.path.join("assets", "level_edit/load_btn.png"))
restart_img = pygame.image.load( os.path.join("assets", "level_edit/restart_btn.png"))
start_img = pygame.image.load( os.path.join("assets", "level_edit/start_btn.png"))
exit_img = pygame.image.load( os.path.join("assets", "level_edit/exit_btn.png"))


# button
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        WIN.blit(self.image, self.rect)
        return action

restart_button = Button(WIDTH//2 - 50, HEIGHT//2 + 25, restart_img)
start_button = Button(WIDTH//2 - 400, HEIGHT//2 + 100, start_img)
exit_button = Button(WIDTH//2 + 150, HEIGHT//2 + 100, exit_img)

#traps
class Trap_Top(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(trap_top_img, (tile_size, tile_size)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y      

class Trap_Down(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(trap_down_img, (tile_size, tile_size)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y      



class Trap_Right(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(trap_right_img, (tile_size, tile_size)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y      


class Trap_left(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(trap_left_img, (tile_size, tile_size)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y      


#save_point 
class Savepoint(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(long_bar_img, (tile_size, tile_size)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  

trap_top_group = pygame.sprite.Group()
trap_down_group = pygame.sprite.Group()
trap_right_group = pygame.sprite.Group()
trap_left_group = pygame.sprite.Group()
save_point_group = pygame.sprite.Group()

# world class
class World():
    def __init__(self, data):
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row :
                if tile == 1:
                    save = Savepoint(col_count * tile_size, row_count * tile_size)
                    save_point_group.add(save)
                if tile == 2:  
                    img = pygame.transform.scale(banana_img, (tile_size, tile_size)) 
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(apple_img, (tile_size, tile_size)) 
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    trap_down = Trap_Down(col_count * tile_size, row_count * tile_size)
                    trap_down_group.add(trap_down)
                if tile == 5:
                    img = pygame.transform.scale(glass_block_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(noglass_block_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 7:
                    trap_left = Trap_left(col_count * tile_size, row_count * tile_size)
                    trap_left_group.add(trap_left)
                if tile == 8:    
                    trap_top = Trap_Top(col_count * tile_size, row_count * tile_size)
                    trap_top_group.add(trap_top)
                if tile == 9:
                    trap_right = Trap_Right(col_count * tile_size, row_count * tile_size)
                    trap_right_group.add(trap_right)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            WIN.blit(tile[0], tile[1])

            # test self check sizes
            # pygame.draw.rect(WIN, (255,255,255), tile[1], 2)


# Player class
class Player():
    def __init__(self, x, y):
        self.reset(x, y)
        for num in range(0, 6):
            img_right = pygame.image.load( os.path.join("assets", f"player/run/{num}.png")) 
            img_right = pygame.transform.scale(img_right, (PLAYER_SIZE,PLAYER_SIZE))
            self.images_right.append(img_right)

            img_left = pygame.transform.flip(img_right , True, False)
            self.images_left.append(img_left)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, game_over, level):
        dx = 0
        dy = 0
        cool_down = 4

        if game_over == 0:

            # keys
            key = pygame.key.get_pressed()
            #left
            if  key[pygame.K_a]: 
                dx -= player_vel
                self.counter += 1
                self.direction = -1
            # right
            if key[pygame.K_d]: 
                dx += player_vel
                self.counter += 1
                self.direction = 1

            #jump
            if key[pygame.K_SPACE] and self.jumped == False and self.landed < 2: #jump
                self.vel_y = -13
                self.jumped = True
                self.landed += 1
            if not key[pygame.K_SPACE]:
                self.jumped = False
            if not key[pygame.K_a] and not key[pygame.K_d]:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # jump velocity
            self.vel_y += 0.8
            if self.vel_y > 8:
                self.vel_y = 8
            dy += self.vel_y

            # check collision
            for tile in world.tile_list:
                # check x coordinate
                if tile[1].colliderect(self.rect.x + dx, self.rect.y,self.width, self.height):
                    dx = 0

                # cehck y coordinate
                if tile[1].colliderect(self.rect.x, self.rect.y + dy,self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if below the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.landed = 0

            # check collision with traps 
            if pygame.sprite.spritecollide(self, trap_top_group, False):
                game_over = GAME_OVER 
            if pygame.sprite.spritecollide(self, trap_left_group, False):
                game_over = GAME_OVER 
            if pygame.sprite.spritecollide(self, trap_right_group, False):
                game_over = GAME_OVER 
            if pygame.sprite.spritecollide(self, trap_down_group, False):
                game_over = GAME_OVER 
            elif pygame.sprite.spritecollide(self, save_point_group, False):
                if 40 * round(self.rect.left // 40) == 40 * round(self.rect.right // 40):
                    save_point[0] = 40 * round(self.rect.x // 40) + 10
                save_point[1] = 40 * round(self.rect.y // 40)
                game_over = 3

            # player coordinate 
            self.rect.x += dx
            self.rect.y += dy
            if self.rect.bottom > HEIGHT:
                game_over = GAME_OVER 

            if self.rect.top < 0:
                self.rect.top = 0

            if self.rect.left < 0 and level == 1:
                self.rect.left = 0

            if self.rect.left < 0 and level > 1:
                self.rect.left = WIDTH - 5
                game_over = -2

            if self.rect.left > WIDTH:
                self.rect.left = 20
                game_over = 1
                
            # animation
            if (self.counter > cool_down):
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

        elif game_over == -1 :
                self.image = pygame.transform.flip(self.images_right[0] , False, True)
                self.rect.y += 15
            
        WIN.blit(self.image, self.rect)

        # testing for rectangle
        # pygame.draw.rect(WIN, (255,255,255),self.rect, 2)       
        return game_over

    def reset(self, x, y):
        # run 
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.vel_y = 0
        self.jumped = False
        self.direction = 1
        self.landed = 0

        # image loading
        img = pygame.image.load( os.path.join("assets", "player/idle/0.png"))
        img_right = pygame.transform.scale(img, (PLAYER_SIZE , PLAYER_SIZE))

        img_left = pygame.transform.flip(img_right , True, False)
        self.images_right.append(img_right)
        self.images_left.append(img_left)

        # initial image
        self.image = self.images_right[0]
        # rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player = Player(save_point[1], save_point[1])
world = World(load_level_map())

# main funcrion
def draw_map():
    world.draw()
    trap_top_group.draw(WIN)
    trap_left_group.draw(WIN)
    trap_down_group.draw(WIN)
    trap_right_group.draw(WIN)
    save_point_group.draw(WIN)

run = True
while run:
    clock.tick(FPS)
    WIN.fill((135,206,250))

    if game_menu:
        if start_button.draw():
            game_menu = False
        if exit_button.draw():
            run = False
    else :
        draw_map()
        game_over = player.update(game_over, level)
        if game_over == -1:
            if restart_button.draw():
                level = saved_level
                trap_top_group = pygame.sprite.Group()
                trap_down_group = pygame.sprite.Group()
                trap_right_group = pygame.sprite.Group()
                trap_left_group = pygame.sprite.Group()
                save_point_group = pygame.sprite.Group()
                world = World(load_level_map())
                draw_map()
                player = Player(save_point[0], save_point[1])
                game_over = 0

        if game_over == 1:
            level += 1   
            if level > MAX_LEVEL:
                run = False
                continue
            trap_top_group = pygame.sprite.Group()
            trap_down_group = pygame.sprite.Group()
            trap_right_group = pygame.sprite.Group()
            trap_left_group = pygame.sprite.Group()
            save_point_group = pygame.sprite.Group()
            world = World(load_level_map())
            draw_map()
            game_over = 0

        if game_over == -2:
            level -= 1
            trap_top_group = pygame.sprite.Group()
            trap_down_group = pygame.sprite.Group()
            trap_right_group = pygame.sprite.Group()
            trap_left_group = pygame.sprite.Group()
            save_point_group = pygame.sprite.Group()
            world = World(load_level_map())
            draw_map()
            game_over = 0

        if game_over == 3:     
            saved_level = level
            game_over = 0

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()