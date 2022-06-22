import pygame
import pickle
import os
from os import path

pygame.init()

clock = pygame.time.Clock()
fps = 60

tile_size = 40
rows = 25
cols = 16 
margin = 40
WIDTH = 1000  #1000
HEIGHT = 640 # 640

WIN = pygame.display.set_mode((WIDTH, HEIGHT + 200))
pygame.display.set_caption("Level Editor")

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
save_img = pygame.image.load( os.path.join("assets", "level_edit/save_btn.png"))
load_img = pygame.image.load( os.path.join("assets", "level_edit/load_btn.png"))

#define game variables
clicked = False
level = 1

#define colours
white = (255, 255, 255)
green = (144, 201, 120)

world_data = []
for col in range(cols):
    r = [0]
    for row in range(rows-1):
        r += [0]
    world_data.append(r)

#create boundary
for tile_col in range(0, cols):
    for tile_row in range(0, rows):
        # buttom 
        world_data[cols-1][tile_row] = 6
        world_data[0][tile_row] = 5
        world_data[tile_col][0] = 5
        world_data[tile_col][rows-1] = 6
    
font = pygame.font.SysFont('Futura', 24)

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	WIN.blit(img, (x, y))

def draw_grid():
    for c in range(rows +1):
        #vertical lines
        pygame.draw.line(WIN, (255,255,255), (c * tile_size, 0), (c * tile_size, HEIGHT))

    for d in range(cols + 1):
        #horizontal lines
        pygame.draw.line(WIN, (255,255,255), (0, d * tile_size), (WIDTH, d * tile_size ))
    
def draw_world():
    for row in range(cols):
        for col in range(rows):
            if world_data[row][col] > 0:
                if world_data[row][col] == 1:
                    img = pygame.transform.scale(long_bar_img, (tile_size, tile_size)) 
                    WIN.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 2:  
                    img = pygame.transform.scale(banana_img, (tile_size, tile_size)) 
                    WIN.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 3:
                    img = pygame.transform.scale(apple_img, (tile_size, tile_size)) 
                    WIN.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 4:
                    img = pygame.transform.scale(trap_down_img, (tile_size, tile_size)) 
                    WIN.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 5:
                    img = pygame.transform.scale(glass_block_img, (tile_size, tile_size))
                    WIN.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 6:
                    img = pygame.transform.scale(noglass_block_img, (tile_size, tile_size))
                    WIN.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 7:
                    img = pygame.transform.scale(trap_left_img, (tile_size, tile_size)) 
                    WIN.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 8:    
                    img = pygame.transform.scale(trap_top_img, (tile_size, tile_size)) 
                    WIN.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 9:
                    img = pygame.transform.scale(trap_right_img, (tile_size, tile_size))
                    WIN.blit(img, (col * tile_size, row * tile_size))

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		WIN.blit(self.image, (self.rect.x, self.rect.y))
		return action


save_button = Button(WIDTH // 2 - 150, HEIGHT + 20, save_img)
load_button = Button(WIDTH // 2 + 50, HEIGHT + 20, load_img)

#main
run = True
while run:      
    clock.tick(fps)

    #draw background
    WIN.fill((135,206,250))

    #load and save level
    if save_button.draw():
        #save level data
        pickle_out = open(f'level{level}', 'wb')
        pickle.dump(world_data, pickle_out)
        pickle_out.close()
        print(world_data)
    if load_button.draw():
        #load in level data
        if path.exists(f'level{level}'):
            pickle_in = open(f'level{level}', 'rb')
            world_data = pickle.load(pickle_in)


    #show the grid and draw the level tiles
    draw_grid()
    draw_world()

    draw_text(f'Level: {level}', font, white, tile_size, HEIGHT + 80)
    draw_text('Press UP or DOWN to change level', font, white, tile_size, HEIGHT + 60)
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        #mouseclicks to change tiles
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0] // tile_size
            y = pos[1] // tile_size
            #check that the coordinates are within the tile area
            if x < rows and y < cols:
                #update tile value
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y][x] += 1
                    if world_data[y][x] > 9:
                        world_data[y][x] = 0
                elif pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] -= 1
                    if world_data[y][x] < 0:
                        world_data[y][x] = 9
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        #up and down key presses to change level number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            elif event.key == pygame.K_DOWN and level > 1:
                level -= 1

    #update game display window
    pygame.display.update()
    
pygame.quit()