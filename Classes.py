from Consts import *
import math

#   CLASES
class CelestialBody:
    def __init__ (self, name, x_ini, y_ini, radius, color, mass):
        self.name = name
        self.x_ini = x_ini      #metros
        self.y_ini = y_ini      #metros
        self.radius = radius    #Radio del circulo, no es a escala
        self.color = color
        self.mass = mass
        self.x = x_ini      #metros
        self.y = y_ini      #metros
        self.apoapsis_distance = math.sqrt(self.x_ini ** 2 + self.y_ini ** 2)     #La distancia máxima del sol que está el cuerpo celeste
        self.lap = 0        #Vueltas al sol

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0      #m/s
        self.y_vel = 0      #m/s

    def attraction(self, other):
        #Calcula la fuerza que ejerce un cuerpo externo sobre este

        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x       #Variacion en eje X
        distance_y = other_y - self.y       #Variacion en eje Y
        distance = math.sqrt(distance_x ** 2 +distance_y ** 2)      #Distancia (hipotenusa)

        if other.sun:
            self.distance_to_sun = distance

        force = G * self.mass * other.mass / distance**2 
        alpha = math.atan2(distance_y, distance_x)      #Uso atan2 porque atan da error si no se usan datos en radianes
        force_x = math.cos(alpha) * force
        force_y = math.sin(alpha) * force
        
        return force_x, force_y
    
    def update_position(self, bodies):
        total_fx = total_fy = 0
        for body in bodies:
            if(self.sun != 1):
                if self == body:        #Cuando se encuentra a si mismo en el array lo saltea para que no de error de calculo
                    continue

                fx, fy = self.attraction(body)
                total_fx += fx
                total_fy += fy

        self.x_vel += total_fx * TIMESTEP / self.mass 
        self.y_vel += total_fy * TIMESTEP / self.mass 

        self.x += self.x_vel * TIMESTEP
        self.y += self.y_vel * TIMESTEP
        self.orbit.append((self.x, self.y))

 #       if((self.x, self.y) == (self.x_ini, self.y_ini)):
#            self.lap += 1

        distance_from_sun = math.sqrt(self.x ** 2 + self.y ** 2)
        if distance_from_sun > self.apoapsis_distance:
            self.apoapsis_distance = distance_from_sun  
            self.lap += 1   

        