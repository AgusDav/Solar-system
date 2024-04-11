import pygame
from Classes import CelestialBody
from Consts import *
from Functions import *
pygame.init()

def main():
    run = True
    clock = pygame.time.Clock()

    bodies = initialize_bodies()
    
    while run:
        clock.tick(60)      #Para que vaya a 60 fps máx
        WINDOW.fill((0, 0, 0))      #Fondo negro

        for event in pygame.event.get():    #Se fija copnstantemente los eventos 
            if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana termina el prog
                run = False
 
        draw_grid(bodies)

        for body in bodies:      #Actualzia la posición de los planeta y los dibuja/mueve
            body.update_position(bodies)
            draw_bodies(body, WINDOW)
        
        pygame.display.update()

    pygame.quit()

main()