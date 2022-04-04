import random

# Les type de boucle :
# - While
# - Do while
# - For classique 
# - For each

# Reproduction d'une boucle for classique avec une boucle while
# Condition d'intialisation
counter = 0
# Taille de la boucle
limit = 10

 # Condition de continuation
while counter < limit:
    # Action à répéter
    print("tour", counter)

    # incrémentation / décrementation
    counter +=1

# Reproduction d'une boucle for classique avec une boucle while
# COndition d'initialisation
counter = 0
# Taille de la boucle 
limit = 10

while True:
    # Action à répéter
    print("do while", counter)

     # incrémentation / décrementation
    counter +=1

    # Condition de continuation
    if not (counter < limit):
        break

# For de python
for counter in range(0, 10):
    # Action à répéter
    print('for python:', counter)

# For de python
mots = ['foo', 'bar', 'baz']

# Méthode non recommandée pour boucler sur tous les élément d'une liste
for i in range(0, len(mots)):
    # Action à répéter
    print(f'mots (non reco) {i}:', mots[i])

# Méthode recommanndée, pour boucler sur tous les éléments d'une liste
for mot in mots:
    # Action à répéter
    print("mot (reco)", mot)

for i, mot in enumerate(mots):
    # Action à répéter
    print(f'mot (reco) {i}:', mot)

# Affichage des nombre de 0 à 10 avec un "pas" (step) de 2
for i in range(0, 10, 2):
    print(i)

# Exo : affichez les nombres de 100 à 999 avec une boucle for
# Exo : affichez les nombres de 0 à 20 qui sont multiple de 3
# Exo : Affichez les nombre de 10 à 1 à rebours
# Info : la fonction range() prend un troisuème paramètre qui indique le "pas" (step)

# Exo 1
for counter in range(100, 1000, 1):
    print("exo1", counter)

# Exo 2 
for counter in range(0, 21, 3):
    print("exo2", counter)

# Exo 3
for counter in range(10, 0, -1):
    print("exo3", counter)

# Algo : tirage de 4 nombres different parmi 5
numbers = []

# 1 er 2eme 3eme et 4eme tirage
for i in range(4):
    while True:
        n = random.randint(1, 5)

    # Condition d'arrêt
        if n not in numbers:
        # le nombre n'a pas encore été tiré au hasard
        # on peut sortir de la boucle
            break

    numbers.append(n)
print(numbers)
