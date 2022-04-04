# la liste qui contiendra nos réponse
resultats = []


# carré de 2 chiffres : 4 à 9 
carres_2_chiffres = []

for i in range(4, 10):
    carres_2_chiffres.append(i ** 2)
    
print(carres_2_chiffres)

# carré de 4 chiifres : 32 à 99 
carres_4_chiffres = []

for i in range(32, 100):
    carres_4_chiffres.append(i ** 2)

print(carres_4_chiffres)

# construisons des nombres à 4 chiffres
for i in carres_2_chiffres:
    for j in carres_2_chiffres:
        nombre = i * 100 + j 

        if nombre in carres_4_chiffres:
            resultats.append(nombre)

print(resultats)

#2. Carré formé de deux nombres consécutifs
#183 184 est le carre a six chiffres de 42S. On remarque que ses trois
#premiers chiffres et ses trois derniers forment deux nombres consécutifs
#183 et 184.
#Trouver 1'unique carré a huit chiffres tel que ses quatre premiers
#chiffres et ses quatre derniers représentent deux nombres consécutifs.