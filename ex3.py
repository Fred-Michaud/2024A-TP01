# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

#Caractéristiques uniques des lancers
speed = float(input("Vitesse initiale (m/s): "))
angle = float(input("Angle de lancement (degrés): "))

#Constantes
g = 9.8
distance = ((speed**2)*(math.sin(math.radians(2*angle))))/9.8
distance_arrondie = round(distance, 2)
print ( f" La distance parcourue est : {distance_arrondie} mètres")


