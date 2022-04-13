# le scores de 5 jouers
import numbers


scores = [433, 562, 574, 800, 953]

# données en entrée ; une liste d'int
# données en sorties ; un int

def int_average(numbers: list) -> int:   
    #"""
    #Cette fonction renvoit un arrondi de la moyenne des nombre passé en paramètres.

    #numbers: list cette liste contient les nombre (int ou foat) dont il faut calculer la moyenne 
    #return: int la fonction renvoit la moyenne arrondie au format int 
    #"""


    # le nombre d'élément
    n = len(numbers)

    # existe mais pas pédagogique !
    #total = sum(scores)

    # initialisation de l'accumulateur
    total = 0 

    for numbers in numbers:
        total += numbers
        

    # moyenne = total / nombre d'élément
    average = total / n 

    # arrondi du resultat
    average = round(average)


    return average

# le scores de 5 jouers
scores = [433, 562, 574, 800, 953]
average = int_average(scores)


# le scores de 5 jouers
scores = [302, 102, 956, 987, 931]
average = int_average(scores)
print(average)

