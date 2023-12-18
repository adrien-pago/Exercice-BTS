#Ecrire un algorithme (avec un en-tête) demandant à l’utilisateur de saisir un nombre puis
#affichant « Ce nombre est strictement positif », « Ce nombre est nul » ou « Ce nombre est
#strictement négatif » selon le cas.

n=int(input("Choisir un nombre : "))

if n>0:
    print((n), " est un nombre est strictement positif")
if n ==0:
    print((n), " est un nombre nul")
if n <0:
    print((n), "est un nombre strictement négatif")
    
    
