import pygame
import os
import time 
import random

pygame.font.init()

#set health and width height 
WIDTH, HEIGHT = 1000,750
MAX_HEALTH = 100

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

#Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


# classes
# laser detail 
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    #show the laser
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    # movement adding by velosity 
    def move(self, vel):
        self.y += vel

    #set off screen
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)
    
    #set collision
    def collision(self, obj):
        return collide(self, obj)

#ships detail
class Ship:
    #set cooldown 
    COOLDOWN = 15

    def __init__(self, x, y, health=MAX_HEALTH):
        self.x = x
        self.y = y
        self.health = health 
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    #show the ships
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    #shot lazer speed and collision details
    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    # calculate cool down
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    
    #shoot action
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


#player ship detail
class Player(Ship):
    def __init__(self, x, y, health=MAX_HEALTH):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    #show player laser
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    # show the healthbar and ship
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    #health bar place
    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10, (self.ship_img.get_width() * (1 -(self.max_health - self.health)/self.max_health)), 10))

    #ability to clear all 
    def superclear(self):
        for i in range(100):
            laser = Laser(self.x + i * 10, self.y, self.laser_img)
            laser2 = Laser(self.x - i * 10, self.y, self.laser_img)

            self.lasers.append(laser)
            self.lasers.append(laser2)
    
class Enemy(Ship): 
    COOLDOWN = 30
    COLOR_MAP = {
                "red":(RED_SPACE_SHIP, RED_LASER),
                "green":(GREEN_SPACE_SHIP, GREEN_LASER),
                "blue":(BLUE_SPACE_SHIP, BLUE_LASER)
                }
    def __init__(self, x, y, color, health=MAX_HEALTH):
        super().__init__(x, y, health) 
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    #the ship moves itself
    def move(self, vel):
        self.y += vel
    
    #enemies shot 
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 19, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    #cool down
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

#function for collide
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y

    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


# main
def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 5

    #ship and laser speed
    enemy_vel = 1
    player_vel = 5
    laser_vel = 5
    
    #set the original starting place for player ship
    player = Player(450, 600)

    #lost variable
    lost = False
    lost_count = 0

    #ability variable
    superclear = True

    #cool down variable
    cool_down = 0

    #use to run the clock
    clock = pygame.time.Clock()

    # sub function for window
    def redraw_window():
        WIN.blit(BG, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        #show the level and lives
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)        
        player.draw(WIN)

        #show lose if lost
        if lost:
            lost_label = lost_font.render("YOU LOST!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
        
        pygame.display.update()

    #run function
    while run:
        clock.tick(FPS)
        redraw_window()
        if cool_down > 0:
            cool_down -= 1

        #count lost
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1
        
        #if lost, show label for 3 second and back to main page
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue 

        #if no enemies for current level, upgrade level 
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            enemy_vel += 0.2

            #recover health and ability 
            player.health = MAX_HEALTH
            superclear = True

            #summon enemies
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # wasd moving
        keys = pygame.key.get_pressed()
        if  keys[pygame.K_a] and player.x - player_vel > 0: #left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        if keys[pygame.K_q]:
            if(superclear):
                player.superclear()
                superclear = False
        
        # check enemies movement and laser tile 
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2 * FPS) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)  

        player.move_lasers(-laser_vel, enemies) 

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 40)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_lable = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_lable, (WIDTH/2 - title_lable.get_width()/2, 350))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()

main_menu()