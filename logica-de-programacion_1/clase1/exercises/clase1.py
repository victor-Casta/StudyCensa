def addittion(a, b):
 print(a + b)

def substract(a, b):
 print(a - b)

def multiply(a, b):
 print(a * b)

def division(a, b):
 if b == 0:
  print("Error: No se puede dividir por cero.")
 else:
  print(a / b)

def area(base, height):
 print((base * height) / 2)

print('1 -> Suma')
print('2 -> Resta')
print('3 -> Multiplicación')
print('4 -> División')
print('5 -> rectangle area')
user_option = int(input('Ingresa una opción: '))

if user_option == 1:
 number_one = int(input('Ingresa el primer número: '))
 number_two = int(input('Ingresa el segundo número: '))
 addittion(number_one, number_two)
elif user_option == 2:
 number_one = int(input('Ingresa el primer número: '))
 number_two = int(input('Ingresa el segundo número: '))
 substract(number_one, number_two)
elif user_option == 3:
 number_one = int(input('Ingresa el primer número: '))
 number_two = int(input('Ingresa el segundo número: '))
 multiply(number_one, number_two)
elif user_option == 4:
 number_one = int(input('Ingresa el primer número: '))
 number_two = int(input('Ingresa el segundo número: '))
 division(number_one, number_two)
elif user_option == 5:
 number_one = int(input('Ingresa el primer numero'))
 number_two = int(input('Ingresa el segunfo numero'))
 area(8, 9)
else:
 print('Opción incorrecta')