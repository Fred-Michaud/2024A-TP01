# TODO: Créer un script permettant le formattage du livre des records des JO.


#différentes questions a répondre
country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom?")
date = input("Quelle est la date du record?")
sport = input("Quelle est la discipline?")
category = input("Quelle est la catégorie?")
record = input("Quel est le record?")

#record

txt = f"Nouveau record \n ------------- \n Pays: {country} \
Discipline: {sport} \n Catégorie: {category} \n Date: {date} \
\n Nom: {athlete} \n Record: {record}"

print(txt)


