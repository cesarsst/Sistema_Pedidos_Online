from django.test import TestCase

# Create your tests here.
comandas = [1, 2, 3, 1, 5, 6, 8, 8, 8 , 8]



aux = []

for item in comandas:
    if item not in aux:
        aux.append(item)


print(aux)
