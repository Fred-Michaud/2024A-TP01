# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input("Quel est le pourcentage de batterie du bateau?: "))
number_km_per_litter=0
battery_level_left=battery_level
number_km_possible=0
if battery_level == 0:
    print("Battery vide")
else:

    while battery_level_left !=0:
        if battery_level_left>50 and battery_level_left <= 100:
            number_km_per_litter=2
        elif battery_level_left>25 and battery_level_left <= 50:
            number_km_per_litter=0.5
        elif battery_level_left>10 and battery_level_left <= 25:
            number_km_per_litter=1
        elif battery_level_left>5 and battery_level_left <= 10:
            number_km_per_litter=2.5
        elif battery_level_left>0 and battery_level_left <= 5:
            number_km_per_litter=6
    
    if(battery_level_left >=1 ):
        number_km_possible+=number_km_per_litter
        battery_level_left-=1
    else:
     number_km_possible=number_km_possible+number_km_per_litter*battery_level_left
     battery_level_left=0
     
    print(f"La distance possible est de {round(number_km_possible, 1)} km")
    


