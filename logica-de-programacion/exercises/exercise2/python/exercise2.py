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

def decent_order():
  counter = 10
  while counter > 0:
    print(counter)
    counter -= 1

def fibonacci():
  user_number = int(input('Ingresa un numero: '))
  a = 0
  b = 1
  counter = 1
  print(a)
  print(b)
  while  counter <= user_number:
    temp = b
    b = a + b
    a = temp
    print(b)
    counter += 1

def fibonacci_user():
  n = int(input("Ingrese el número de términos de la secuencia de Fibonacci que desea generar: "))
  a, b = 0, 1
  contador = 0

  while contador < n:
    print(a, end=" ")
    a, b = b, a + b
    contador += 1

def divisors_numbers():
  number = int(input('Ingresa un numero: '))
  counter = 1
  while counter < number:
    if number % counter == 0:
      print(counter)
    counter += 1

def primos_numbers():
  i = 2
  while i <= 100:
    IsPrimo = True
    j = 2
    while j < i:
      if i % j == 0:
        IsPrimo = False
        break
      j += 1
    if IsPrimo:
      print(i)
    i += 1

def is_primo():
  user_number = int(input('Ingresa un numero: '))
  if user_number <= 1:
    print(f'El número {user_number} no es primo')
    return

  es_primo = True
  divisor = 2
  while divisor * divisor <= user_number:
    if user_number % divisor == 0:
      es_primo = False
    break
  divisor += 1

  if es_primo:
    print(f'El número {user_number} es primo')
  else:
    print(f'El número {user_number} no es primo')

def multiply_numbers():
  user_number = int(input('Ingresa un numero: '))
  counter = 1
  while counter <= 10:
    print(f'{user_number} * {counter} = {user_number * counter}')
    counter += 1

def perfect_numbers():
  user_number = int(input('Ingresa un numero: '))
  counter = 1
  temp = 0
  while counter <= user_number - 1:
      if user_number % counter == 0:
          temp += counter
      counter += 1
  if temp == user_number:
    print(f'el numero {user_number} es pefecto')
  else:
    print(f'el numero {user_number} no es pefecto')

def armonic_serie():
  n = int(input("Ingrese un número entero positivo: "))
  if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
  else:
    suma = 0.0
    i = 1
    while i <= n:
        suma += 1 / i
        i += 1
    print(f"La suma de los primeros {n} términos de la serie armónica es: {suma:.2f}")

def palindrome_number():
  number = int(input("ingresa un número entero positivo: "))

  if number <= 0:
    print("El número ingresado no es positivo.")
  else:
    number_str = str(number)
    length = len(number_str)
    is_palindrome = True
    index = 0
    while index < length // 2:
      if number_str[index] != number_str[length - index - 1]:
        is_palindrome = False
        break
      index += 1

    if is_palindrome:
      print("El número", number, "es un palíndromo.")
    else:
      print("El número", number, "no es un palíndromo.")


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
  print('11 -> Numeros de 10 al 1')
  print('12 -> Serie fibonacci')
  print('13 -> Serie fibonacci primeros n términos')
  print('14 -> Numeros divisores')
  print('15 -> Numeros primos del 1 al 100')
  print('16 -> Numero primo')
  print('17 -> Tabla de multiplicar')
  print('18 -> Numero perfecto')
  print('19 -> Serie armonica')
  print('20 -> Numero palindromo')
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
  elif option == 11:
    decent_order()
  elif option == 12:
    fibonacci()
  elif option == 13:
    fibonacci_user()
  elif option == 14:
    divisors_numbers()
  elif option == 15:
    primos_numbers()
  elif option == 16:
    is_primo()
  elif option == 17:
    multiply_numbers()
  elif option == 18:
    perfect_numbers()
  elif option == 19:
    armonic_serie()
  elif option == 20:
    palindrome_number()
  elif option == 0:
    print('saliendo...')
    break
  else:
    print('opcion no valida')