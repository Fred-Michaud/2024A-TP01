#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays conserné? ")
code_medals = input("Chaine représentant les médailles? ").upper()
string_valid=True
for letter in code_medals:
    if letter != "G" and letter != "S" and letter != "B":
        print("Ceci est une chaine invalide.\n")
        string_valid=False

if(string_valid==True):
    print(f"""{country}:
    -{code_medals.count('G')} Or
    -{code_medals.count('S')} Argent
    -{code_medals.count('B')} Bronze""")


