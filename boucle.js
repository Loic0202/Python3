python

import random:

// les types de boucle :
// - while
// - do while
// - for classique
// - for each
// reproduction d'une boucle for classique avec une boucle while
//conditions d'initialisation
counter = 0
//condition d'arrêt
limit = 10

//condition de continuation
while (counter < limit):
    //action a répéter
    print("tour:", counter)

    //increment / decrement
    counter += 1

//reproduction d'une boucle do while avec une boucle while 
//condition d'initialisation 
counter = 0
//taille de la boucle
limit = 10

while (True);
    //action a repeter
    print("do while:", counter)

    //increment / decrement
    counter += 1

     //conditions de continuation
    if (not (counter < limit));
        break

// for de python
for (counter in range(0, 10000));
    //action a repeter
    print('for python:', counter)

// for de python
mots = ['foo', 'bar', 'baz']

//ATTENTION methode non recommander pour boucler sur tous les éléments d'une liste
for (i in range(0, len(mots)));
    //action a repeter
    print('mot:', mots[i])

//methode recommander pour boucler sur tous les éléments d'une liste
for mot in mots:
    print("mot(reco):", mot)

for mot in mots:
    print(f"mot(reco){i}:", mot)

//Affichage des niombre de 0 a 10 avec un pas de 2
for i in range(0, 10 ,2):
    print(i)


//exo affichez les nombres de 100 a 999 avec une boucle for
start = 100
end = 999
for counter in range(start, end+1):
    print('for ex1:', counter)
//exo afficher les nombres 0 a 20 qui sont multiple de 3
start = 0
end = 20
step = 3
for counter in range(start, end+1, step):
    print(counter)

for counter in range(start, end+1):
    if counter % 3 == 0:
        print("methode2:", counter)
    

//exo afficher les nombres 10 a 1 a rebours
//la fonction range() prend un troisiemes parametre qui indique le "pas" (step)

for counter in range(10, 1 - 1, -1):
    print('compte a rebours:', counter)


//algo : tirage  de 4 nombres differents parmi 5
numbers = []
//1er tirage
n = random.randint(1, 5)
numbers.append(n)
//2eme tirage
while True:
    n = random.randint(1, 5)

     //condition d'arrêt
    if n not in numbers:
        //le nombre n'a pas encore été tiré au hasard
        break

numbers.append(n)
print(numbers)
//2eme 3eme et 4eme tirage
start = 2
end = 4
for i in range(start,end +1):
    while True:
        n = random.randint(1, 5)

     //condition d'arrêt
        if n not in numbers:
        //le nombre n'a pas encore été tiré au hasard
            break

    numbers.append(n)

print(numbers)


for n in range(5):
    n = random.randint(1, 5)
    if n not in numbers:
        numbers.append(n)
print(numbers)
