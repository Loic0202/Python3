text = "foo bar baz"
splitted_text = text.split(' ')

print(splitted_text)
print(len(splitted_text))
result = splitted_text[0] = 'toto'
print(splitted_text[0])
print(splitted_text[1])
print(splitted_text[2])
# print(splitted_text[3]) 
# print(splitted_text[3]) # erreur
# splitted_text[3] = 123 # erreur

# intervention de valeur dans une liste (version python) on peut remplacer les chiffre par (inidex)
splitted_text[0] = 42
splitted_text[1] = 123

splitted_text[0], splitted_text[1] = splitted_text[1], splitted_text[0]

# intervention de valeur dans une liste (version classique)
tmp = splitted_text[0]
splitted_text[0] = splitted_text[1]
splitted_text[1] = tmp

splitted_text.append(123)
print(splitted_text)

#help(splitted_text.append)

# [star:end:step]
# start inclus
# end exclus
result = splitted_text[0:2]
print(result)

text ="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer consectetur est sed elit venenatis, nec dictum mi semper. Nam nec nisl venenatis, pulvinar turpis ac, elementum felis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed efficitur nunc eu nunc malesuada posuere id a eros. Phasellus nec facilisis ligula, et molestie libero. Vestibulum nisl orci, imperdiet non leo et, volutpat consectetur nisl. Duis consequat vitae sapien in dapibus."
# suppresion des virgules ( remplacement par une chîne de caractères vide)
splitted_text = text.split(',')
# suppresission des points (remplacement par une chîne de caractèeres vide)
text = ''.join(splitted_text)
splitted_text = text.split('.')
text = ''.join(splitted_text)
print(text)
text = text.replace('.', '')

splitted_text = text.split(' ')
print(len(splitted_text))

# tous les mots de l'index 10 inclus à l'index 20 exclus 
partial_list = splitted_text [3:7:2]
print(partial_list)
print(splitted_text)

# ATTENTION ne fonctionne pas dans l'autre sens
# tous le mots de l'index 7 inclus à l'index 3 exclus 
# l'index start doit être strictement inférieur à l'index end 
partial_list = splitted_text[7:3]
print(partial_list)
print(splitted_text)

#start = 7 
#end = 3

#if start >= end :
    #start, end = end, start

#print(start, end)
    
#splitted_text = splitted_text[start:end]

partial_list = splitted_text[-7:-3:2]
print(splitted_text)
print(partial_list)

# exo 
# récupérez dans splitted_text les mots de l'index 35 à 49 inclus 
#2 afficher le numéro du dernier index
#3 récupérez 1 mot sur 2 de l'index 0 au dernier index

# exo 1
start = 35
end = 49
result =  splitted_text[start:end+1]

# exo 2 
last_index = len(splitted_text)-1

# exo 3 
result = splitted_text[0:last_index+1:2]

taille_liste = len(splitted_text)
result = splitted_text[0:taille_liste:2]


#4 créer trois listes contenant :
# - le premier mot sur trois 
# - le deuxième mot sur tois 
# - le troisième mot sur trois 
#
# Exemple :
# listes_originale = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
# listes_partielle1 == ['foo', 'lorem']
# listes_partielle2 == ['bar', 'ipsum']
# listes_partielle3 == ['baz']

liste1 =splitted_text[0:last_index+1:3]
liste2 =splitted_text[1:last_index+1:3]
liste3 =splitted_text[2:last_index+1:3]

# tous les éléments
# valeurs par défaut :
# - start = 0
# - end = len()
# - step = 1

result = splitted_text[::]

# copie de tous les élément en ordre inverse 
result = splitted_text[::-1]

# copis de tous les éléments à partir de start jusqu'à la fin 
start = 3
result = splitted_text[start:]

# copie de tous les éléments du début jusqu'à end 
end = 10 
result = splitted_text[:end]

# Mode pile
my_list = []
print(my_list)
# équivalent d'un push()
my_list.append("foo")
print(my_list)
my_list.append(123)
print(my_list)
my_list.append(3.14)
print(my_list)

last_element = my_list.pop()
print(my_list)
print(last_element)

# Mode file
my_list = ["toto", "titi", "tata", "tutu"]
client = my_list.pop(0)
print(my_list)
print(client)

# Mode liste
print(my_list[0])
del(my_list[0])
print(my_list)

my_list.insert(0, "mémé")
print(my_list)

# conccaténation de listes
list_a = ["a", "b", "c"]
list_b = [1, 2, 3]

list_c = list_a + list_b
print(list_c)

# fussion de liste (modification de l'originale)
list_a.extend(list_b)
print(list_a)