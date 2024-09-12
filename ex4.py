# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input("Quel est le pourcentage de batterie du bateau?: "))
number_km_per_litter=0
substitute=battery_level
number_km_possible=0

while substitute !=0:
    if substitute>=50 and substitute <= 100:
        number_km_per_litter=2
    elif substitute>=25 and substitute <= 50:
        number_km_per_litter=0.5
    elif substitute>=10 and substitute <= 25:
        number_km_per_litter=1
    elif substitute>=5 and substitute <= 10:
        number_km_per_litter=2.5
    elif substitute>=0 and substitute <= 5:
        number_km_per_litter=6
    
    if(substitute >=1 ):
        number_km_possible+=number_km_per_litter
        substitute-=1
    else:
     number_km_possible=number_km_possible+number_km_per_litter*substitute
     substitute=0
    

print(f"La distance possible est de {round(number_km_possible, 1)} km")
