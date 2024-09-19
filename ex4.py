# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ?"))
number_km_per_litter=0
battery_level_left=battery_level
number_km_possible=0

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
    
    if(battery_level_left >= 1 and type(battery_level_left) == int):
        number_km_possible+=number_km_per_litter
        battery_level_left-=1
    else:
     x=battery_level_left-int(battery_level_left)
     battery_level_left=int(battery_level_left)
     number_km_possible=number_km_possible+number_km_per_litter*(x)

if battery_level != 0:
    print(f" {round(number_km_possible, 1)} km")
else:
      print(" La batterie est vide")  
    


