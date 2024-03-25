def one_to_ten_numbers():
  counter = 1
  while counter <= 10:
    print(counter)
    counter += 1

def natural_number_adittions():
  suma = 0
  counter = 0
  while counter <= 100:
    suma += counter
    counter += 1
  print(f'la suma de los 100 primeros numeros naturales es igual a: {suma}')

def user_numbers():
  user_number =  int(input('Ingresa un numero: '))
  counter = 1
  while counter <= user_number:
    print(counter)
    counter += 1

def pair_numbers():
  counter = 2
  while counter <= 10:
    print(counter)
    counter += 2

def pair_numbers_for_user():
  user_number = int(input('Ingresa un numero: '))
  counter = 2
  while counter <= user_number:
    print(counter)
    counter += 2

def factorial():
  user_number = int(input('Ingresa un numero: '))
  factorial = 1
  counter = 1
  while counter <= user_number:
    factorial *= counter
    counter += 1
  print(f'el factorial de {user_number} es igual a: {factorial}')

def multiply_numbers_three():
  counter = 1
  while counter <= 100:
    if counter % 3 == 0:
      print(counter)
    counter += 1

def addition_digits():
  user_number = int(input('Ingresa un numero: '))
  suma = 0
  while user_number > 0:
    suma += user_number % 10
    user_number //= 10
  print(f'la suma de los digitos de {user_number} es igual a: {suma}')

def odd_numbers_to_user_number():
  user_number = int(input('Ingresa un numero: '))
  counter = 1
  while counter <= user_number:
    if counter % 2!= 0:
      print(counter)
    counter += 1

def pair_number_to_one_hundred():
  addition = 0
  counter = 0
  while counter <= 100:
    print(counter)
    addition += counter
    counter += 2
  print(f'la suma de los 100 primeros numeros naturales es igual a: {addition}')

while True:
  print('Selecciona una opcion: ')
  print('1 -> Numeros del 1 al 10')
  print('2 -> Suma de los 100 primeros numeros naturales')
  print('3 -> Numeros de 1 hasta un numero ingresado por el usuario')
  print('4 -> Primeros 10 numeros pares')
  print('5 -> Numeros pares hasta un numero ingresado por el usuario')
  print('6 -> Factorial de un numero')
  print('7 -> Suma de los digitos de un numero')
  print('8 -> Multiplos de 3 hasta el numero 100')
  print('9 -> Numeros impares hasta el numero ingresado por el usuario')
  print('10 -> Suma de numeros pares del 2 al 100')
  print('0 -> salir')

  option = int(input('Selecciona una opcion: '))

  if option == 1:
    one_to_ten_numbers()
  elif option == 2:
    natural_number_adittions()
  elif option == 3:
    user_numbers()
  elif option == 4:
    pair_numbers()
  elif option == 5:
    pair_numbers_for_user()
  elif option == 6:
    factorial()
  elif option == 7:
    addition_digits()
  elif option == 8:
    multiply_numbers_three()
  elif option == 9:
    odd_numbers_to_user_number()
  elif option == 10:
    pair_number_to_one_hundred()
  elif option == 0:
    print('saliendo...')
    break
  else:
    print('opcion no valida')