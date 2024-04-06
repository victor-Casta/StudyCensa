import random
import string


def imc_calculator(weight, height):
    imc = weight / (height * height)
    if imc < 18.5:
        print('Se encuentra en bajo peso')
    elif imc >= 18.5 and imc <= 24.9:
        print('Su peso es normal')
    elif imc >= 25.0 and imc <= 29.9:
        print('Se encuentra en sobrepeso')
    elif imc >= 30.0 and imc <= 34.9:
        print('se encuentra en obesidad grado 1')
    elif imc >= 35.0 and imc <= 39.9:
        print('se encuentra en obesidad grado 2')
    elif imc >= 40:
        print('se encuentra en obesidad grado 3')
    else:
        print('Ingrese un valor correcto')


def coin_converter():
    coins = {
        1: ['COP', 0.00026, 'USD', 'De COP a USD'],
        2: ['USD', 3871.22, 'COP', 'De USD a COP'],
        3: ['EUR', 1.11, 'USD', 'De EUR a USD'],
        4: ['USD', 0.90, 'EUR', 'De USD a EUR'],
        5: ['GBP', 1.30, 'USD', 'De GBP a USD'],
        6: ['USD', 0.77, 'GBP', 'De USD a GBP'],
        7: ['CAD', 0.75, 'USD', 'De CAD a USD'],
        8: ['USD', 1.34, 'CAD', 'De USD a CAD'],
        9: ['AUD', 0.68, 'USD', 'De AUD a USD'],
        10: ['USD', 1.48, 'AUD', 'De USD a AUD'],
        11: ['JPY', 0.0092, 'USD', 'De JPY a USD'],
        12: ['USD', 108.62, 'JPY', 'De USD a JPY'],
        13: ['CHF', 1.03, 'USD', 'De CHF a USD'],
        14: ['USD', 0.97, 'CHF', 'De USD a CHF'],
        15: ['CNY', 0.14, 'USD', 'De CNY a USD'],
        16: ['USD', 7.01, 'CNY', 'De USD a CNY'],
    }
    print('Selecciona: ')
    for option in coins:
        print(f'{option} -> {coins[option][3]}')

    option_selected = int(input('Ingresa una opcion: '))

    for i in coins:
        if option_selected == i:
            amount = float(input(f'Ingresa la cantidad de {
                           coins[i][0]} a convertir: '))
            print(
                f'La cantidad de {amount} {coins[i][0]} equivale a {
                    coins[i][1] * amount} {coins[i][2]}'
            )


def discount_calculator(product_price, discount):
    total_discount = product_price * (discount / 100)
    price_with_discount = product_price - total_discount
    return price_with_discount


def game(user_option):
    options_game = ['piedra', 'papel', 'tijera']
    random_option = random.choice(options_game)
    print(f'Maquina ha selccionado: {random_option}')
    if user_option == random_option:
        print('empate!')
    elif user_option == options_game[0] and random_option == options_game[1]:
        print('Gana maquina!')
    elif user_option == options_game[0] and random_option == options_game[2]:
        print('Gana Jugador 1!')
    elif user_option == options_game[1] and random_option == options_game[2]:
        print('Gana Maquina!')
    elif user_option == options_game[1] and random_option == options_game[0]:
        print('Gana Jugador 1!')
    elif user_option == options_game[2] and random_option == options_game[0]:
        print('Gana Maquina!')
    elif user_option == options_game[2] and random_option == options_game[1]:
        print('Gana Jugador 1!')
    else:
        print('opcion no valida')


def leap_year(year):
    if 1998 <= year <= 2024:
        if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            return True
        else:
            return False
    else:
        return None


def password_generator(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña


def unit_converter():
    def meters_to_inches(meters):
        return meters * 39.3701

    def liters_to_gallons(liters):
        return liters * 0.264172

    def show_menu():
        print("Opciones de conversión:")
        print("1. Metros a Pulgadas")
        print("2. Litros a Galones")

    def convert(option):
        if option == 1:
            meters = float(input("Ingrese la longitud en metros: "))
            inches = meters_to_inches(meters)
            print(f"{meters} metros equivale a {inches} pulgadas.")
        elif option == 2:
            liters = float(input("Ingrese el volumen en litros: "))
            gallons = liters_to_gallons(liters)
            print(f"{liters} litros equivale a {gallons} galones.")
        else:
            print("Opción no válida.")

    show_menu()

    chosen_option = int(input("Selecciona una opcion: "))

    convert(chosen_option)


def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]


def main_process():
    user_input = input("Escribe una palabra: ")
    if is_palindrome(user_input):
        print("La palabra es palindroma.")
    else:
        print("La palabra no es palindroma")


def check_balance(balance):
    return balance


def deposit(balance, amount):
    balance += amount
    return balance


def withdraw(balance, amount):
    if amount > balance:
        return "Fondos insuficientes"
    else:
        balance -= amount
        return amount, balance


def atm_simulator():
    balance = 0
    while True:
        print("\nMenú del Cajero Automático:")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        choice = input("Ingrese su opción: ")

        if choice == "1":
            print("Su saldo es:", check_balance(balance))
        elif choice == "2":
            amount = float(input("Ingrese la cantidad a depositar: "))
            balance = deposit(balance, amount)
            print("Depósito exitoso. Su nuevo saldo es:", balance)
        elif choice == "3":
            amount = float(input("Ingrese la cantidad a retirar: "))
            result = withdraw(balance, amount)
            if isinstance(result, tuple):
                withdrawn_amount, balance = result
                print("Retiro exitoso. Saldo restante:", balance)
            else:
                print(result)
        elif choice == "4":
            print("Saliendo del Cajero Automático. ¡Gracias!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")


def guess_number(answer):
    while True:
        guess = input(
            "Adivina el número (o ingresa 'salir' para salir del juego): ")
        if guess.lower() == "salir":
            print("¡Hasta luego!")
            return
        try:
            guess = int(guess)
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if guess == answer:
            print("¡Felicidades! ¡Has adivinado el número correctamente!")
            return
        elif guess < answer:
            print("El número que debes adivinar es mayor que", guess)
        else:
            print("El número que debes adivinar es menor que", guess)


def game_guess():
    answer = random.randint(1, 100)
    print("Bienvenido al juego de adivinanzas. Estoy pensando en un número entre 1 y 100.")
    guess_number(answer)


while True:
    print('1 -> Calculadora de IMC')
    print('2 -> Conversor de monedas')
    print('3 -> Calculadora de descuentos')
    print('4 -> Piedra, papel o tijera')
    print('5 -> Verificador de año bisiesto')
    print('6 -> generador de contraseñas')
    print('7 ->  Convertidor de Unidades')
    print('8 -> Verificador de palindromos')
    print('9 -> Simulador de Cajero automatico')
    print('10 -> Juego de adivinanzas')
    print('0 -> salir')

    option = int(input('Ingresa una opcion: '))

    if option == 1:
        weight = int(input('Ingresa tu peso en Kilogramos: '))
        height = float(input('Ingresa tu altura en metros: '))
        imc_calculator(weight, height)
    elif option == 2:
        coin_converter()
    elif option == 3:
        product = int(input('Ingresa el valor del producto: '))
        discount_number = int(input('Ingresa el valor de descuento: '))
        print(discount_calculator(product, discount_number))
    elif option == 4:
        user_option = str(input('Ingresa una opcion: '))
        game(user_option)
    elif option == 5:
        option = int(input('Ingrese un año: '))
        resultado = leap_year(option)
        if resultado is None:
            print('El año debe estar en el rango de 1998 a 2024')
        elif resultado:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    elif option == 6:
        longitud_deseada = int(
            input("Ingrese la longitud deseada para la contraseña: "))
        if longitud_deseada > 0:
            contraseña_generada = password_generator(longitud_deseada)
            print("La contraseña generada es:", contraseña_generada)
        else:
            print("La longitud de la contraseña debe ser mayor que 0.")
    elif option == 7:
        unit_converter()
    elif option == 8:
        main_process()
    elif option == 9:
        atm_simulator()
    elif option == 10:
      game_guess()
    elif option == 0:
        print('saliendo...')
        break
    else:
        print('opcion no valida')