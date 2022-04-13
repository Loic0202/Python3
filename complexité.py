# complexité == efficacité
# effocacité
# temps d'exécution
# espace mémoire

# notation de landau : o() (lettre o, pas le chiffre 0)
# pas une foction mais un ensemble

# o(c) (c == constante)
# o(1)
# + - * / //
# result = 123 + 42
# print(result)


# recherche par dicothomie
# rechercher d'un fruit dont la letrre démarre par une lettre
# o(log(n))
# log == logarithme naturel
words = ['ananas', 'banane', 'cerise', 'kiwi', 'durion', 'orange', 'pomme']

# o(n)
# n est la quantité de donnés à traiter
numbers = [123, 42, 3, 14]

for number in numbers:
    result = number * 2
    print(result)

# recherche par dicothomie dasn une liste
# o(n * log(n))
my_list = [
    
    ['ananas', 'banane', 'cerise', 'kiwi', 'durion', 'orange', 'pomme']
    [1, 2, 3, 4, 15, 20, 25, 100; 999]
]
# o(n * n)
# n est la quantité de données à traiter de la premiere liste 
# n est la qauntité de données à traiter de la deuxième liste

numbers = [123, 42, 3,14]
more_numbers = [2,71, 3,14, 0, 53]
common_numbers = []

for number in numbers:
    # number == 42 
    for more_number in more_numbers:
        if number == more_numbers:
            common_numbers.append(number)

# o(n au carrré)
matrix = [
    [123, 42, 3, 14]
    [2,71, 3,14, 0]
    [1, 2, 3]
]

for line in matrix:
    for number in line:
        result = number * 2
        print(result)

# o(n au carré)
cube = [
    [
        ['a1', 'a2', 'a3'],
        ['a4', 'a5', 'a6'],
        ['a7', 'a8', 'a9'],
    ],
    [
        ['b1', 'b2', 'b3'],
        ['b4', 'b5', 'b6'],
        ['b7', 'b8', 'b9'],

    ],
    [
        ['c1', 'c2', 'c3'],
        ['c4', 'c5', 'c6'],
        ['c7', 'c8', 'c9'],
    ]
]

for square in cube:
    for line in square:
        for spot in line:
            print(spot)

# Algo qui ne sont pas efficase du tout !!!
# o(n ** n)
# o(n!) == o(n * (n - 2) * ... * 2)
# 5! == 5 * 4 *3 *2

# exemple d'optimisation
numbers = [4, 10, 42, 3.14]
# initalisation du compteur
i = 0
# sauver la taille du tableau dans une vatiable
size = len(numbers)
# vérification de la condition de continuation
while i < size:
    # action à repeter
    print(numbers[i])
    # incrémentation du compteur
    i += 1

# exo 2 : déterminer la complexité algorithmique de ce programme
# o(?)
numbers = [4, 10, 42, 3.14]
my_list = []

while True:
    number = numbers.pop()
    my_list.append(number)

    if len(numbers) == 0:
        break




# exo 1 : déterminer la complexité algorithmique de ce programme
# o(?)
numbers = [4, 10, 42, 3.14]
my_list = []

for n in numbers:
    #puissance 2
    result = n ** 2
    my_list.append(result)

