import pygame
import time
from random import *

black = (0, 0, 0)
white = (250, 250, 250)
sunset = (253, 72, 47)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500
imageHeight = 51
imageWidth = 72

surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Jocu in care te dai cu elicopteru mancatz-ash')
clock = pygame.time.Clock()

img = pygame.image.load('img/helicopter.png')

def score(current_score):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score: '+str(current_score), True, white)
    surface.blit(text, [0, 0])

def blocks(x_block, y_block, block_width, block_height, gap): 
    pygame.draw.rect(surface, white, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, white, [x_block, y_block+block_height+gap, block_width, surfaceHeight])
    
def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf',150)
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(2)

    while replay_or_quit() == None:
        clock.tick()

    main()
    
def gameOver():
    msgSurface('Kaboom!')

def helicopter(x, y, image):
    surface.blit(img, (x,y))

def main():
    x = 150
    y = 200
    y_move = 0
    x_block = surfaceWidth
    y_block = 0
    block_width = 75
    block_height = randint(0, (surfaceHeight/2))
    gap = imageHeight * 3
    block_move = 5
    current_score = 0
            
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
                    
        y += y_move                            
        surface.fill(black)
        helicopter(x, y, img)        
        blocks(x_block, y_block, block_width, block_height, gap)
        score(current_score)
        x_block -= block_move

        if y > (surfaceHeight - 40) or y < 0:
            gameOver()

        if x_block < (-1 * block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight/2))
            
        if x + imageWidth > x_block:
            if x < x_block + block_width:
                print 'Possibly between boundaries of x'
                if y < block_height:
                    print 'y crossover UPPER!'
                    if x - imageWidth < block_width + x_block:
                        print 'game over hit upper'
                        gameOver()
        if x + imageWidth > x_block:
            print 'x crossover'
            if y + imageHeight > block_height + gap:
                print 'y crossover lower'
                if x < block_width + x_block:
                    print 'game over LOWER'
                    gameOver()

        if (x < x_block) and (x > (x_block - block_width)):
            current_score += 1
                  
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()



    
