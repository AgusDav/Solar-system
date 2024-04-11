import pygame
import math
from Classes import CelestialBody
from Consts import *
pygame.init()

#   FUNCIONES
def initialize_bodies():
    #Crea los cuerpos celestes y setea sus valores

    sun = CelestialBody("Sol", 0, 0, 30, SUN, 1.98892 * 10**30)        #Masa en kg
    sun.sun = True

    #A todos los planetas se les asigna una velocidad inicial para que empiecen a hacer la elipse, sino se van de la imagen.
    earth = CelestialBody("Tierra",AU, 0, 16, EARTH, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000 

    mars = CelestialBody("Marte", 1.524 * AU, 0, 12, MARS, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    mercury = CelestialBody("Mercurio", 0.387 * AU, 0, 8, MERCURY, 3.30 * 10**23)
    mercury.y_vel = 47.4 * 1000

    venus = CelestialBody("Venus", 0.723 * AU, 0, 14, VENUS, 4.8685 * 10**24)
    venus.y_vel = 35.02 * 1000

    bodies = [sun, mercury, venus, earth, mars]

    return bodies

def draw_grid(bodies):
    #Dibuja la tabla con los datos de los planetas
    
    BEGINNING = 0  #Var para el comienzo de la tabla
    CELL_SIZE = 80

    title = FONT.render("Planetas", 1, WHITE)
    WINDOW.blit(title, (BEGINNING + 100,0))

    columns = FONT.render("Nombre       Distancia al Sol             Vueltas al sol", 1, WHITE)
    WINDOW.blit(columns, (BEGINNING, 20))

    i = 2
    for body in bodies:
        if not body.sun:
            planet_name = FONT.render(f"{body.name}", 1, WHITE)
            planet_distance = FONT.render(f"{body.distance_to_sun}", 1, WHITE)
            planet_laps = FONT.render(f"{body.lap}", 1, WHITE)
            WINDOW.blit(planet_name, (BEGINNING, i * 20))
            WINDOW.blit(planet_distance, (BEGINNING + CELL_SIZE, i * 20))
            WINDOW.blit(planet_laps, (BEGINNING + (CELL_SIZE * 4), i * 20))
            i += 1

def draw_bodies(planet, win):
    #Dibuja los cuerpos celestes y sus nombres

        x = planet.x * SCALE + WIDTH / 2     #Se suma la mitad de el ancho para centrar en la ventana
        y = planet.y * SCALE + HEIGHT / 2    #Se suma la mitad de la altura para centrar en la ventana

        if len(planet.orbit) > 2:
            updated_points = []
            for point in planet.orbit:
                x, y = point
                x = x * SCALE + WIDTH / 2
                y = y * SCALE + HEIGHT / 2
                updated_points.append((x, y))
            pygame.draw.lines(WINDOW, WHITE, 0, updated_points, 2)

        pygame.draw.circle(win, planet.color, (x, y), planet.radius)

        if not planet.sun:        #Imprime el nombre del planeta
            name_text = FONT.render(f"{planet.name}", 1, WHITE)
        else:
            name_text = FONT.render(f"{planet.name}", 1, (0, 0, 0))
        WINDOW.blit(name_text, (x - name_text.get_width()/2, y - name_text.get_height()/2)) #Centra el texto de distancia 