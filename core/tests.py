from django.test import TestCase

# Create your tests here.
cursos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data = {
    'lista1': [],
    'lista2': [],
    'lista3': [],
}

i = 0
for curso in cursos:
    if i == 0:
        data['lista1'].append(curso)
        i += 1
    elif i == 1:
        data['lista2'].append(curso)
        i += 1
    elif i == 2:
        data['lista3'].append(curso)
        i = 0


print(data)