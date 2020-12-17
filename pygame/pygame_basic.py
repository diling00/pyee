import pygame

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

WHITE =(255, 255, 255)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(WHITE)
    
    pygame.draw.polygon(screen, (0, 100, 0), [[400, 50], [300, 250], [500, 250]])
    pygame.draw.polygon(screen, (0, 100, 0), [[400, 150], [250, 400], [550, 400]])
    pygame.draw.rect(screen, (100, 40, 40), (375, 375, 50, 125))
    
    pygame.display.flip()

    clock.tick(60)
    print("fps = " +  str(clock.get_fps()))

pygame.quit()
