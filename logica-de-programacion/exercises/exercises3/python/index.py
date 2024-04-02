def imc_calculator(weight, height):
  imc = weight / (height * height)
  if imc < 18.5:
    print("Se encuentra en bajo peso")
  elif imc >= 18.5 and imc <= 24.9:
    print("Su peso es normal")
  elif imc >= 25.0 and imc <= 29.9:
    print("Se encuentra en sobrepeso")
  elif imc >= 30.0 and imc <= 34.9:
    print("se encuentra en obesidad grado 1")
  elif imc >= 35.0 and imc <= 39.9:
    print("se encuentra en obesidad grado 2")
  elif imc >= 40:
    print("se encuentra en obesidad grado 3")
  else:
    print("Ingrese un valor correcto")

def coin_converter():
  coins = {
    1: ["COP", 0.00026, "USD", "De COP a USD"],
    2: ["USD", 3871.22, "COP", "De USD a COP"],
    4: ["USD", 0.90, "EUR", "De USD a EUR"],
    5: ["GBP", 1.30, "USD", "De GBP a USD"],
    6: ["USD", 0.77, "GBP", "De USD a GBP"],
    7: ["CAD", 0.75, "USD", "De CAD a USD"],
    8: ["USD", 1.34, "CAD", "De USD a CAD"],
    9: ["AUD", 0.68, "USD", "De AUD a USD"],
    10: ["USD", 1.48, "AUD", "De USD a AUD"],
    11: ["JPY", 0.0092, "USD", "De JPY a USD"],
    12: ["USD", 108.62, "JPY", "De USD a JPY"],
    13: ["CHF", 1.03, "USD", "De CHF a USD"],
    14: ["USD", 0.97, "CHF", "De USD a CHF"],
    15: ["CNY", 0.14, "USD", "De CNY a USD"],
    16: ["USD", 7.01, "CNY", "De USD a CNY"],
  }
  print("Selecciona: ")
  for option in coins:
    print(f"{option} -> {coins[option][3]}")

    option_selected = int(input("Ingresa una opcion: "))

    for i in coins:
      if option_selected == i:
        amount = float(input(f"Ingresa la cantidad de {
                      coins[i][0]} a convertir: "))
        print(
          f"La cantidad de {amount} {coins[i][0]} equivale a {
            coins[i][1] * amount} {coins[i][2]}"
        )

while True:
  print("1 -> Calculadora de IMC")
  print("2 -> Conversor de monedas")
  print("0 -> salir")

  option = int(input("Ingresa una opcion: "))

  if option == 1:
    weight = int(input("Ingresa tu peso en Kilogramos: "))
    height = float(input("Ingresa tu altura en metros: "))
    imc_calculator(weight, height)
  elif option == 2:
    coin_converter()
  elif option == 0:
    print("saliendo...")
    break
  else:
    print("opcion no valida")