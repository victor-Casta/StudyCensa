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
  while counter <= 100:
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

def addition_digits():
  user_number = int(input('Ingresa un numero: '))
  suma = 0
  while user_number > 0:
    suma += user_number % 10
    user_number //= 10
  print(f'la suma de los digitos de {user_number} es igual a: {suma}')


while True:
  print('Selecciona una opcion: ')
  print('1 -> Numeros del 1 al 10')
  print('2 -> Suma de los 100 primeros numeros naturales')
  print('3 -> Numeros de 1 hasta un numero ingresado por el usuario')
  print('4 -> Primeros 100 numeros pares')
  print('5 -> Numeros pares hasta un numero ingresado por el usuario')
  print('6 -> Factorial de un numero')
  print('7 -> Suma de los digitos de un numero')
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
  elif option == 0:
    print('saliendo...')
    break
  else:
    print('opcion no valida')