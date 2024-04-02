def imc_calculator(weight, height):
  imc = weight / (height * height)
  if(imc < 18.5):
    print('Se encuentra en bajo peso')
  elif(imc >= 18.5 and imc <= 24.9):
    print('Su peso es normal')
  elif(imc >= 25.0 and imc <= 29.9):
    print('Se encuentra en sobrepeso')
  elif(imc >= 30.0 and imc <= 34.9):
    print('se encuentra en obesidad grado 1')
  elif(imc >= 35.0 and imc <= 39.9):
    print('se encuentra en obesidad grado 2')
  elif(imc >= 40):
    print('se encuentra en obesidad grado 3')
  else:
    print('Ingrese un valor correcto')


while True:
  print('1 -> Calculadora de IMC')
  print('2 -> Conversor de monedas')
  print('0 -> salir')

  option = int(input('Ingresa una opcion: '))

  if option == 1:
    weight = int(input('Ingresa tu peso en Kilogramos: '))
    height = float(input('Ingresa tu altura en metros: '))
    imc_calculator(weight, height)
  elif option == 2:
    print('opcion 2')
  elif option == 0:
    print('saliendo...')
    break
  else:
    print('opcion no valida')