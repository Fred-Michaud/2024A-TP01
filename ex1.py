# TODO: Créer un script permettant le formattage du livre des records des JO.


#relever le nouveau record
country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom ? ")
date = input("Date du record ? ")
sport = input("Dans quelle discipline ? ")
category = input("Dans une catégorie spécifique ? ")
record = input("Quel est le record ? ")

#résumé du nouveau record
txt = f"\nNouveau Record:\n--------------------\n{date} - {sport} - {category}:\n\
\t{athlete} ({country}) - {record}"

print(txt)


