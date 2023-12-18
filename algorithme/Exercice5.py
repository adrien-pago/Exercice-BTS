#Lors de l'adoption du calendirer grégoren à la fin du XVIe siècle, l  a été décidé que certaines années auraient 366 jours.
# Ces années, appelées bissextiles, sont les années:
# - Soit multiple de 4 mais non multiple de 100;
# - Soit multiple de 400.

#Ecrire un algorithme qui permet de dire si une année est bissextille ou pas


AnneTest = int(input("Choisir une année pour savoir si elle est bissextile ou pas ?"))
if (AnneTest %4 ==0 and AnneTest %100 != 0)  or (AnneTest %400 ==0):
    print((AnneTest) ," est une année bissextille !")
else :
    print ((AnneTest) ," n'est pas une année bissextille !")
    
    