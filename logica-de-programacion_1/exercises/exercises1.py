# 1. Crea un algoritmo que de un numero, le sume 30 y muestre el resultado en pantalla
def addittion_number(number_a):
  print(f'El resultado de la suma es de: {number_a + 30}')

addittion_number(int(input('Ingresa un numero: ')))

# 2. hacer un programa que te pida un nombre, por ejemplo 'PEDRO' e imprima en pantalla "Mucho gusto PEDRO", si te llamas rosa que imprima mucho gusto Rosa
def greetings(name):
  print(f'Mucho gusto {name}')

greetings(input('Ingresa tu nombre: '))

# 3. Hacer un programa que lea dos numeros e imprima cual de los dos numeros es menor
def is_menor(numberA, numberB):
  if numberA < numberB:
    print(f'El numero {numberA} es menor que {numberB}')
  if numberB < numberA:
    print(f'El numero {numberB} es menor que {numberA}')
  if(numberA == numberB):
    print('Los numeros son iguales')

number_a = int(input('Ingresa un numero A: '))
number_b = int(input('Ingresa un numero B: '))
is_menor(number_a, number_b)

# 4. Hacer un programa que calcule el promedio de tres numeros leidos en pantalla
def prom(listNumbers):
  addittion_number = 0
  for i in range(len(listNumbers)):
    addittion_number += listNumbers[i]
  prom = addittion_number / 3
  print(f'El promedio de numeros es de: {prom}')

numbersList = []
while(True):
  print('Digite 0 para dejar de insertar numeros')
  item = int(input('Ingrese un nuevo numero a la lista: '))
  numbersList.append(item)
  if item == 0:
    break

prom(numbersList)

# 5. hacer un programa que lea dos numeros y muestre la suma y la multiplicacion de ellos
def addition_and_multiply(number_a, number_b):
  addtion = number_a + number_b
  multiply = number_a * number_b
  print(f'La suma de los dos numeros es: {addtion}')
  print(f'La multiplicacion de los dos numeros es: {multiply}')

number_a = int(input('Ingrese el numero A: '))
number_b = int(input('Ingrese el numero B: '))
addition_and_multiply(number_a, number_b)

# 6. Hacer un algoritmo que lea un numero, y que imprima en pantalla si el numero es positivo, negativo o nulo
def cuestions_to_number(number):
  if number == 0:
    print('El numero es nulo')
  if (number < 0):
    print('El numero es negativo')
  if (number > 0):
    print('El numero es positivo')

option_number = int(input('Ingresa un numero: '))
cuestions_to_number(option_number)

# 7. Hacer un algoritmo que lea 5 notas y me imprima en pantalla la definitiva donde las 4 primeras notas valen el 70% y la ultima el 30%
def total_notes():
  note1 = float(input("Ingrese la primera nota: "))
  note2 = float(input("Ingrese la segunda nota: "))
  note3 = float(input("Ingrese la tercera nota: "))
  note4 = float(input("Ingrese la cuarta nota: "))
  note5 = float(input("Ingrese la quinta nota: "))

  first_notes = (note1 + note2 + note3 + note4) / 4 * 0.7

  final_note = first_notes + note5 * 0.3

  print("La nota final es:", final_note)

total_notes()

# 8. Hacer un algoritmo que lea la edad de un persona y me imprima en pantalla si esa persona es mayor de edad
def is_adult(age):
  if (age < 18):
    print(f'La persona es menor de edad')
  if (age >= 18):
    print(f'La persona es mayor de edad')

user_age = int(input('Ingresa un tu edad: '))
is_adult(user_age)

# 9. Hacer un algoritmo que lea 4 numeros e imprima la sumatoria y el promedio de los numeros
def prom_numbers(listNumbers):
  addition = 0
  for number in listNumbers:
    addition += number
  prom = addition / len(listNumbers)
  print(f'El promedio de numeros es: {prom}')

list_numbers_1 = []

while True:
  print('Ingresa 0 para dejar de insertar numeros')

  item = int(input('Ingresa un nuevo numero a la lista: '))
  if item == 0:
    break
  list_numbers_1.append(item)

prom_numbers(list_numbers_1)

# 10. Hacer un algoritmo que lea el nombre de un empleado, su salario basico, y las horas extras trabajadas. calcular su salario mensual e imprimir tanto el nombre del empleado  como su salario mensual, donde cada hora extra se paga a 40.000
def calcular_salario():
  name = input('Ingrese su nombre: ')
  base_salary = float(input('Ingrese su salario base: '))
  extra_hours = int(input('Ingrese la cantidad de horas extras trabajadas: '))
  extra_hours_count = extra_hours * 40000
  month_salary = base_salary + extra_hours_count
  print(f'Nombre: {name}, Salario mensual: {month_salary}')

calcular_salario()

# 11. Hacer un algoritmo que lea el salario base de un empleado, y la cantidad de hijos, se debe calcular el salario mensual de la siguiente manera, si la cantidad de hijos es 1, el auxilio es del 5% sobre el salario, si tiene 2 hijos es de 10% y si tiene 3 es del 15%
def calcular_salario_mensual():
  name = input('Ingresa tu nombre: ')
  base_salary = int(input('Ingrese tu salario base: '))
  count_children = int(input('Ingrese la cantidad de hijos: '))

  if count_children == 1:
    percentage = (5 * base_salary) / 100
    total_salary = base_salary + percentage
    print(f'El salario mensual de {name} es: {total_salary}')
  elif count_children == 2:
    percentage = (10 * base_salary) / 100
    total_salary = base_salary + percentage
    print(f'El salario mensual de {name} es: {total_salary}')
  elif count_children >= 3:
    percentage = (15 * base_salary) / 100
    total_salary = base_salary + percentage
    print(f'El salario mensual de {name} es: {total_salary}')
  else:
    print('Por favor ingrese un número válido de hijos.')


calcular_salario_mensual()


# 12. hacer un algoritmo que lea un numero e imprima si ese numero es par o impar
def is_pair(number):
  if (number == 0):
    {
      print(f'El numero {number} es nulo')
    }
  elif (number % 2 == 0):
    print(f'EL numero {number} es par')
  else:
    print(f'El numero {number} es impar')

user_number_a = int(input('Ingresa un numero: '))
is_pair(user_number_a)


# 13. Hacer un algoritmo que lea edad de cualquier persona e imprima solo si la persona es mayor de edad, de lo contrario, imprima un mensaje que diga no puede votar
def can_vote(name, age):
  if age >= 18:
    print(f'La persona {name} puede votar')
  elif age < 18:
    print(f'La persona {name} no puede votar')
  else:
    print('La edad es incorrecta')

user_name = input('Ingrese su nombre: ')
user_age = int(input('Ingrese su edad: '))
can_vote(user_name, user_age)

"""
  14. Hacer un algoritmo que lea el total de ventas de los vendedores de un supermercado donde se deberá controlar e imprimir la comisión del vendedor de la siguiente manera:

  a. Si la venta del vendedor está entre 2.000.000 y 3.000.000 se deberá entregar al vendedor una comision del 3% sobre el total de la ventas
  b. Si la venta del vendedor está entre 3.000.000 y 4.000.000 se deberá entregar al vendedor una comision del 4% sobre el total de las ventas
  c. Si la venta del vendedor está entre 5.000.000 y 6.000.000 se deberá entregar al vendedor una comision del 5% sobre el total de las ventas
"""


def total_sales():
  total_sales = int(input('Ingrese el total de ventas este mes: '))
  commission = 0

  if total_sales >= 2000000 and total_sales <= 3000000:
    commission = (3 * total_sales) / 100
    print(f'El salario total con comision es de {total_sales + commission}')
  elif total_sales >= 3000000 and total_sales <= 4000000:
    commission = (4 * total_sales) / 100
    print(f'El salario total con comision es de {total_sales + commission}')
  elif total_sales >= 5000000 and total_sales <= 6000000:
    commission = (5 * total_sales) / 100
    print(f'El salario total con comision es de {total_sales + commission}')
  else:
    print('No aplica para comision')


total_sales()
