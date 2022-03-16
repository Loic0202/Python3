# swap


a = 42
b = 123

# interchanger les valeurs (faites un swap)
# a = 123
# b = 42

if a == 123 and b == 42:
    print("vous avez réussi à inverser les valeurs des variables")

# méthode clasique 

c = a
a = b 
b = c

# méthode arithmétique
a = a + b # a = 42 + 123
b = a - b # b = (42 + 123) - 123 = 42
a = a - b # a = (42 + 123) - 42 = 123

# destructured assignment
#avec python, js mais pas php
a, b = b, a

# arrondi
import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP


print(Decimal("0.5").quantize(Decimal("1")))
print(Decimal("1.5").quantize(Decimal("1")))

# encadrement
import random

a = 42
b = 123

c = random.randint(1, 100)

result = a < 50 < b 
print(result)

result = a < c < b 
print(c)
print(result)
