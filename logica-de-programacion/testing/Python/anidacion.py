#Jerarquia
for i in range(3):
  for j in range(2):
    print(f'valor de i: {i} valor de j: {j}')

#Iteración multiple
for i in range(1, 4):
  for j in range(1, 4):
    print(f'{i} * {j} = {i*j}')

#Flexibilidad
for i in range(1, 4):
  for j in range(1, i + 1):
    print(j, end=" ")
  print()


'''
  Datos o listas complejos
  Normalmente es utilizado para recorrer matrices o listas multidimencionales
'''

matrix = [[0, 1], [2, 3], [4, 5]]

for i in matrix:
  for element in i:
    print(i, end=" ")

#Generacion de permutaciones y combinaciones

#combinaciones

print("combinaciones")
data = [0, 1, 2, 3, 4, 5]
for i in range(len(data)):
  for j in range(i + 1, len(data)):
    print(data[i], data[j])

#Permutaciones
print('permutaciones')
for i in range(len(data)):
  for j in range(len(data)):
    if i != j:
      print(data[i], data[j])


#Datos compuestos
students = [
  {'name': 'victor', 'grades': [1, 2, 3]},
  {'name': 'Bob', 'grades': [1, 2, 3]},
  {'name': 'George', 'grades': [1, 2, 3]}
]

for student in students:
  total_grade = sum(student['grades'])
  average_grade = total_grade / len(student['grades'])
  print(f'{student['name']} tiene un promedio de {average_grade}')