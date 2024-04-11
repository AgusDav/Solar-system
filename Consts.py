import pygame
pygame.init()

#   VENTANA
WIDTH, HEIGHT = 1200, 1000 
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistema solar")      #Titulo de la ventana
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

WHITE = (255, 255, 255)
VENUS = (183, 149, 11)
SUN = (255, 202, 51)
EARTH = (27, 212, 233)
MARS = (233, 57, 27)
MERCURY = (229, 227, 219)

FONT = pygame.font.SysFont("comicsans", 16)

#   CONSTANTES CUERPOS CELESTES
AU = 149.6e6 * 1000 #Astronomical Unit: Distancia aprox entre la Tierra y el Sol (en metros). 149.6 millones km
G = 6.67428e-11     #Constante gravitacional
SCALE = 250 / AU    #1AU = 100 pixels
TIMESTEP = 3600*24  #1 dia 