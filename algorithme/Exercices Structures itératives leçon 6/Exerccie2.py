#Ecrire un algorithme demandant un nombre N à l’utilisateur et qui affiche (avec une phrase) :
#- le quotient de la division de N par 12 dans le cas où N est divisible par 12.
#- le quotient et le reste de la division euclidienne de N par 12 dans le cas où N n’est pas
#divisible par 12.

quotient = int
reste = int
n=int(input("Choisir un nombre : "))

if n%12==0 :
    quotient = n//12
    print("le quotien de la division de ", (n), "par 12 est",(quotient))
else :
    quotient = n//12
    reste = n%12
    print("le quotien de la division de ", (n), "par 12 est",(quotient), " et le reste est égal à ", (reste))