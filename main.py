
import pygame
import os
# display
WIDTH, HEIGHT = 1500, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Laivu Musis')
# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
# variables
EXPLOSION_PLACE = (WIDTH/2, HEIGHT/2)
EXPLOSION_SIZE = (20, 20)
FPS = 60
IMAGE_STATUS = 0
images = []
for i in range(6):
    image = pygame.image.load(os.path.join('assets', ('blowup' + str(i) + '.png')))
    image = pygame.transform.scale(image, EXPLOSION_SIZE)
    images.append(image)


def draw_window():
    WIN.fill(BLACK)
    WIN.blit(images[IMAGE_STATUS], EXPLOSION_PLACE)
    pygame.display.update()

def sprogimas():
    pass


def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
        draw_window()

    pygame.quit()

if __name__ == '__main__':
    main()