def opcion1():
  counter = 1
  while counter <= 10:
    print(counter)
    counter += 1

def opcion2():
  suma = 0
  contador = 1
  while contador <= 100:
    suma += contador
    contador += 1
  print(f'La suma de los primeros 100 números naturales es: {suma}')

def opcion3():
  number = input('Ingresa un numero entero positivo: ')
  counter = 2
  while counter <= int(number):
    print(counter)
    counter += 2

def opcion4():
  factorialNumber = input('Ingresa un numero entero: ')
  counter = 1
  factorial = 1
  while counter <= int(factorialNumber):
    factorial *= counter
    counter += 1
  print(f'El numero factorial de {factorialNumber}: {factorial}')

def opcion5():
  primoNumber = input('Ingresa un numero entero positivo: ')
  i = 2
  while i <= int(primoNumber):
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

def opcion6():
  i = 0
  a = 0
  b = 1

  print(a)
  print(b)

  while i < 20:
    temp = b
    b = a + b
    a = temp
    print(b)
    i += 1

def opcion7():
  secundsForUser = input('Ingresa una cantidad de segundos: ')

  hours = int(secundsForUser) // 3600
  minutes = (int(secundsForUser) % 3600) // 60
  seconds = (int(secundsForUser) % 3600) % 60

  print(f'{hours} horas, {minutes} minutos y {seconds} segundos')

def opcion8():
  numberUser = [int(input('Ingresa un numero entero, ideal de dos o más cifras: '))]

  def suma_list_numbers(list_numbers):
    container = []

    for number in numberUser:
      format_number = str(number)
      for item in format_number:
        container.append(int(item))

    suma = 0
    for item_number in container:
      suma += int(item_number)
    return(suma)

def opcion9():
    user_number = int(input('Ingresa un numero: '))
    divisors = []
    suma_numbers = 0
    counter = 1
    while counter <= user_number - 1:
      if user_number % counter == 0:
        divisors.append(counter)
      counter += 1
    for number in divisors:
      suma_numbers += number
    if suma_numbers == user_number:
      print(f'el numero {user_number} es perfecto')
    else:
      print(f'el numero {user_number} no es perfecto')

def opcion10():
  number = int(input('Ingresa un numero: '))
  for i in range(11):
    print(i * number)

def opcion_por_defecto():
  print("Opción no válida.")


opciones = {
  1: opcion1,
  2: opcion2,
  3: opcion3,
  4: opcion4,
  5: opcion5,
  6: opcion6,
  7: opcion7,
  8: opcion8,
  9: opcion9,
  10: opcion10,
}

opcion = int(input(
    "Selecciona 1: Numeros del 1 al 10 \n"
    "Selecciona 2: Suma de los 100 primeros numeros naturales \n"
    "Selecciona 3: numeros pares \n"
    "Selecciona 4: Numero Factorial \n"
    "Selecciona 5: Numeros primos menores \n"
    "Selecciona 6: Serie Fibinacci 20 primeros números \n"
    "Selecciona 7: Segundos Horas y minutos \n"
    "Selecciona 8: Suma de dígitos \n"
    "Selecciona 9: Numero Perfecto \n"
    "Selecciona 10: Taabla de multiplicar "
  ))

funcion = opciones.get(opcion, opcion_por_defecto)
funcion()
