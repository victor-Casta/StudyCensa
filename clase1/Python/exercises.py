# Escribe un programa que imprima los números del 1 al 10 en una línea separada.
counter = 1
while counter <= 10:
  print(counter)
  counter += 1

#Crea un programa que calcule la suma de los primeros 100 números naturales.
suma = 0
contador = 1
while contador <= 100:
  suma += contador
  contador += 1
print(f'La suma de los primeros 100 números naturales es: {suma}')


#Desarrolla un programa que solicite al usuario un número entero positivo y luego imprima todos los números pares desde 2 hasta ese número.

number = input('Ingresa un numero entero positivo: ')
counter = 2
while counter <= int(number):
  print(counter)
  counter += 2

#Crea un programa que calcule el factorial de un número ingresado por el usuario.
factorialNumber = input('Ingresa un numero entero: ')
counter = 1
factorial = 1
while counter <= int(factorialNumber):
  factorial *= counter
  counter += 1
print(f'El numero factorial de {factorialNumber}: {factorial}')

#Desarrolla un programa que pida al usuario un número entero positivo y luego imprima todos los números primos menores o iguales a ese número.