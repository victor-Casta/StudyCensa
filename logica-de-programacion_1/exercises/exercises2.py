import time
# 1.	Hacer un algoritmo que calcule e imprima la edad aproximada de una persona si se tiene el  año de nacimiento y el año actual.

def age_calculator():
  year_of_birth =  int(input('Ingresa el año de nacimiento: '))
  actual_year = int(input('Ingresa el año actual: '))
  counter = 0

  for year in range(year_of_birth, actual_year):
    counter += 1

  return counter

print(f'la edad actual es de: {age_calculator()}')


# 2.	Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los tiempos obtenidos. Realice un algoritmo que determine e imprima el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera.

def registrar_tiempo_carrera():
  tiempo_actual = time.time()
  tiempo_carrera = float(input("Ingrese el tiempo de carrera en segundos: "))
  return tiempo_carrera, tiempo_actual

def calcular_promedio_semanal(tiempos_registrados):
  suma_tiempos = 0
  cantidad_carreras = 0

  for tiempo, _ in tiempos_registrados:
    suma_tiempos += tiempo
    cantidad_carreras += 1

  if cantidad_carreras > 0:
    promedio_semanal = suma_tiempos / cantidad_carreras
  else:
    promedio_semanal = 0

  return promedio_semanal

tiempos_registrados = []

for _ in range(3):
  tiempo_carrera, tiempo_actual = registrar_tiempo_carrera()
  tiempos_registrados.append((tiempo_carrera, tiempo_actual))

promedio_semanal = calcular_promedio_semanal(tiempos_registrados)


print(f"El tiempo promedio semanal para la ruta de running es de {promedio_semanal:.2f} segundos.")

# 3.	Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Realice un algoritmo que obtenga e imprima el porcentaje que cada quien invierte con respecto a la cantidad total invertida.

def invested_percentage():
  peson_1 = int(input('Ingrese la cantidad invertida: '))
  peson_2 = int(input('Ingrese la cantidad invertida: '))
  peson_3 = int(input('Ingrese la cantidad invertida: '))

  total_invested = peson_1 + peson_2 + peson_3

  def get_percentage(amount):
    percentage = (amount / total_invested) * 100
    return percentage

  print(f'El porcentaje invertido de la persona 1 es de: {get_percentage(peson_1)}')
  print(f'El porcentaje invertido de la persona 2 es de: {get_percentage(peson_2)}')
  print(f'El porcentaje invertido de la persona 3 es de: {get_percentage(peson_3)}')

invested_percentage()

# 4.	Se tiene el nombre de un vendedor, el valor de la venta y el código del producto. La comisión de este vendedor se le liquida de acuerdo al código del producto que vende: si el código del producto es 1 la comisión es del 5% sobre el valor de su venta; si el código del producto es 2 la comisión es del 7.5% sobre el valor de sus ventas; si el código del producto es 3 la comisión es del 6% sobre el valor de sus ventas. Realice un algoritmo que Imprima el nombre del vendedor y su comisión

def commission():
  seller_name = input('Ingrese el nombre del vendedor: ')
  sale_value = int(input('Ingrese el valor de la venta: '))
  product_code = int(input('Ingrese el codigo del producto: '))

  commission = 0

  if(product_code == 1):
    commission = (5/100) * sale_value
    total_commission = commission + sale_value
    print(f'Nombre: {seller_name}, Comision: {total_commission}')
  elif(product_code == 2):
    commission = (7.5/100) * sale_value
    total_commission = commission + sale_value
    print(f'Nombre: {seller_name}, Comision: {total_commission}')
  elif(product_code == 3):
    commission = (6/100) * sale_value
    total_commission = commission + sale_value
    print(f'Nombre: {seller_name}, Comision: {total_commission}')

commission()

# 5.	Se   desea   seleccionar  un  atleta   para   una   maratón internacional,  para seleccionarlo este debe haber  terminado  el maratón anterior, en un tiempo determinado.  Los tiempos son  150 minutos para hombres menores de 40 años; 175 minutos para hombres con una edad mayor o igual a 40 años y 180 minutos para mujeres. Realice un algoritmo que lea el sexo, Edad y tiempo  efectuado en su maratón anterior e imprima si la persona queda seleccionada para la maratón

def select_athlete():
  gender = input('Ingrese el genero del atleta (M/F): ')
  age = int(input('Ingrese la edad del atleta: '))
  time = int(input('Ingrese el tiempo efectuado en su maratón anterior: '))

  if(time == 150 and age < 40):
    print('El atleta puede maratón internacional')
  elif(time == 175 and gender.upper() == 'M' and age >= 40):
    print('El atleta puede maratón internacional')
  elif(time == 180 and gender.upper() == 'F'):
    print('El atleta puede maratón internacional')
  else:
    print('El atleta no puede participar en la maratón internacional')

select_athlete()

# 6.	Realizar un algoritmo que lea tres números e imprimirlos en orden descendente.

def descendant_order():
  numberList = []

  while(True):
    print('1. agregar numeros a la lista')
    print('2. Dejar de agregar numeros a la lista')

    option = int(input('Digite una opcion: '))

    if(option == 1):
      number = int(input('Ingrese un numero a la lista: '))
      numberList.append(number)
    if(option == 2):
      break

  if(len(numberList) > 0):
    counter = 0
    for number in numberList:
      if(number < counter):
        print(number)
      counter += 1
  else:
    print('La lista está vacia')

descendant_order()

# 6.	Realizar un algoritmo que lea tres números e imprimirlos en orden descendente.

def descendant_order():
  numbers_list = []

  while(True):
    print('1. agregar numeros a la lista')
    print('2. Dejar de agregar numeros a la lista')

    option = int(input('Digite una opcion: '))

    if(option == 1):
      number = int(input('Ingrese un numero a la lista: '))
      numbers_list.append(number)
    if(option == 2):
      break

  if(len(numbers_list) > 0):
    numbers_list.sort(reverse=True)
    for number in numbers_list:
      print(number)
  else:
    print('La lista está vacia')

descendant_order()

# 7.	Realizar un algoritmo  que imprima el  número  medio  de  tres números.    El número medio es aquel que no es ni el menor ni  el mayor.

def middle_number(a, b, c):
  sorted_numbers = sorted([a, b, c])
  middle = sorted_numbers[1]
  return middle

number1 = float(input("Ingrese el primer número: "))
number2 = float(input("Ingrese el segundo número: "))
number3 = float(input("Ingrese el tercer número: "))

print("El número medio es:", middle_number(number1, number2, number3))
