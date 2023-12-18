#L'algorithme vérifiee si un nombre entier donné par l'utilisateur est à la fois divisible par 3 et supérieur à 100, 
# auquel cas il affiche "c'est bon !".

# Demander à l'utilisateur de saisir un nombre entier
n = int(input("Entrez un nombre entier : "))

# Vérifier si n est divisible par 3 et n est supérieur à 100
if n % 3 == 0 and n > 100:
    print("C'est bon !")
else:
    print("Ce n'est pas bon")


