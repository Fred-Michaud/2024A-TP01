# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

#Caractéristiques uniques des lancers
speed = float(input("Vitesse initiale (m/s)"))
angle = float(input("Angle de lancement (degrés)"))

#Constantes
height = 2
g = 9.81

#Composantes horizontale et verticale de la vitesse
speed_x = speed * math.cos(math.radians(angle))
speed_y = speed * math.sin(math.radians(angle))

#Utilisation d'une formule qui tient compte de la hauteur initiale de 2m
distance = ((speed_x / g)*(speed_y+ math.sqrt(speed_y**2+2*g*height)))

distance_arrondie = round(distance, 2)

print ( f" La distance parcourue est : {distance_arrondie} mètres")


