import random

firstname = "toto"
lastname = "pop"
number = random.randint(2, 10)

email = firstname + '.' + lastname + str(number) + '@exeample.com'
print(email)

new_emails = random.randint(0, 3)

if new_emails == 0:
    print("vous n'avez pas de nouveaux mail")
elif new_emails == 1:
    print("vous avez reçu <strong>1</strong> nouveau mail")
else:
    print("vous avez réçu <strong>" + str(new_emails) + "</strong> nouveaux mail")

stock = random.randint(0, 15)

if stock == 0:
    print("stock épuisé")
elif stock == 1:
    print("stock en tension : 1 pièce")
elif 1 < stock < 5:
    print(f"stock en tension : {stock} pièces")
elif 5 < stock < 10:
    print(f"stock confortable : {stock} pièces")   
elif 10 <= stock:
    print(f"stock en surnombre : {stock} pièces")

temperature = 10.1 + 0.1 + 0.1
print(temperature)

print(f"la température actuelle est de {temperature:.2f}° C ")

electricite = True

if electricite:
    print('electricite: vrai')
else:
    print('electricte: faux')


# @todo afficher àge à partir de l'année de naissance

print(f"le nombre tiré au hasard est : {random.randint(0, 10)}")

texte = "foo bar baz"
# len == length == longueur
print(len(texte))

print(texte.find("banana"))
print(texte.find("baz"))

texte = "bonjour toto"

keyword = "toto"
keyword = "titi"

# rédiger un bloc if qui indique si le keyword est présent ou non dans la chaîne de caractères

if texte.find("toto") >=0:
    print(texte.find("toto"))
    print("trouvé")

if texte.find("toto") >=0:
    print(texte.find("titi"))
    print("non trouvé")

texte = "Bnjour  Toto"
texte = texte.replace('Bnjour', 'Bonjour')
texte = texte.replace('  ', ' ')
texte = texte.replace('Toto', 'Titi')
print(texte)