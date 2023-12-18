#Un nombre entier N>1 est dit parfait s’il est égal à la somme de tous ses diviseurs
#autres que lui-même. Par exemple le nombre 28 est parfait car ses diviseurs
#sont 1,2,4,7,14 et 28 et on a 28=1+2+4+7+14.


            
   
# Fonction li(n) pour obtenir la liste des diviseurs de n
def li(n):
    L = []
    for k in range(1, n + 1):
        if n % k == 0:
            L.append(k)
    return L

# Fonction estparfait(n) pour vérifier si un nombre est parfait
def estparfait(n):
    diviseurs = li(n)
    somme_diviseurs = sum(diviseurs)
    return somme_diviseurs - n == n

# Algorithme pour trouver le seul nombre parfait de trois chiffres
def trouver_nombre_parfait_trois_chiffres():
    for n in range(100, 1000):
        if estparfait(n):
            print(f"Le seul nombre parfait de trois chiffres est : {n}")

# Demander à l'utilisateur de saisir un nombre pour vérifier s'il est parfait
n = int(input("Choisissez un nombre pour vérifier s'il est parfait : "))
if estparfait(n):
    print(f"{n} est un nombre parfait.")
else:
    print(f"{n} n'est pas un nombre parfait.")

trouver_nombre_parfait_trois_chiffres()

