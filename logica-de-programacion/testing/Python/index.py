# data = input('inserta un año: ')

# if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
# print('el año es bisiesto')
# else:
# print('no es biciesto')


# conversor de temperatura

print("1 -> celsius a farenheit")
print("2 -> farenheit a celsius")
print("0 -> salir")

option = input("Ingresa una opcion: ")

if option == "1":
    celsius = float(input("Ingrese la temperatura en celcius"))
    fahrenheit = (celsius * 9 / 5) + 32
    print("La temperatura en Farenheit es: ", fahrenheit)
if option == "2":
    fahrenheit = (fahrenheit - 32) * 5 / 9
    print("La temperatura en Farenheit es: ", fahrenheit)
else:
    print("opcion no valida")
