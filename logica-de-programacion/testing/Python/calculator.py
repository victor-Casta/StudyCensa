while True:
  print('1 -> suma')
  print('2 -> resta')
  print('3 -> multiplicacion')
  print('4 -> division')
  print('5 -> salir')

  option = input('Ingresa una opcion: ')

  if option == '1':
    number1 = int(input(('Ingresa numero a: ')))
    number2 = int(input(('Ingresa numero b: ')))
    print(number2 + number1)
  elif option == '2':
    number1 = int(input(('Ingresa numero a: ')))
    number2 = int(input(('Ingresa numero b: ')))
    print(number2 - number1)
  elif option == '3':
    number1 = int(input(('Ingresa numero a: ')))
    number2 = int(input(('Ingresa numero b: ')))
    print(number2 * number1)
  elif option == '4':
    number1 = int(input(('Ingresa numero a: ')))
    number2 = int(input(('Ingresa numero b: ')))
    print(number2 / number1)
  elif option == '5':
    print('saliendo...')
    break
  else:
    print('opcion incorrecta')
    break