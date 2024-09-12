#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays conserné? ")
code_medals = input("Chaine représentant les médailles? ").upper()
print(f"""{country}:
-{code_medals.count('G')} Or
-{code_medals.count('S')} Argent
-{code_medals.count('B')} Bronze""")
