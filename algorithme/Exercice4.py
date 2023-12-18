#Ecrire un algorithme demandant à l'utilisateur d'entrer un speudo de 4 caractères commençant par Z et qui afficher:
#"speudo invalide" si l'utilisateur ne respect pas la consigne

# Demander à l'utilisateur de saisir un pseudo
pseudo = input("Entrez un pseudo de 4 caractères commençant par 'Z' : ")

# Vérifier si le pseudo est valide
if len(pseudo) == 4 and pseudo[0] == 'Z':
    print("Bonjour  Zeus" + (pseudo))
else:
    print("Pseudo invalide")
