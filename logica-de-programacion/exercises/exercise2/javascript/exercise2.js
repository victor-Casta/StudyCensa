"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readline_1 = require("readline");
var rl = (0, readline_1.createInterface)({
    input: process.stdin,
    output: process.stdout,
});
function numbersOnetoTen() {
    var counter = 1;
    while (counter <= 10) {
        console.log(counter);
        counter++;
    }
}
function naturalNumbers() {
    var counter = 0;
    var suma = 0;
    while (counter <= 100) {
        suma += counter;
        counter++;
    }
    console.log("la suma de los 100 primeros números naturales es: ", suma);
}
function printNumbers(number) {
    var i = 1;
    while (i <= parseInt(number)) {
        console.log(i);
        i++;
    }
}
function pairNumbersOfTen() {
    var counter = 2;
    while (counter <= 10) {
        console.log(counter);
        counter += 2;
    }
}
function pairNumbersOfUserNumber(number) {
    var counter = 2;
    while (counter <= parseInt(number)) {
        console.log(counter);
        counter += 2;
    }
}
function factorial(number) {
    var factorial = 1;
    var counter = 1;
    while (counter <= parseInt(number)) {
        factorial *= counter;
        counter++;
    }
    return factorial;
}
function digits_addition(number) {
    var counter = 0;
    var suma = 0;
    while (counter < number.length) {
        var numberUnited = parseInt(number[counter]);
        suma += numberUnited;
        counter++;
    }
    return suma;
}
function threeMultiply() {
    var counter = 1;
    while (counter <= 100) {
        console.log(counter * 3);
        counter++;
    }
}
function oddNumbers(number) {
    var counter = 1;
    while (counter <= parseInt(number)) {
        if (counter % 2 !== 0) {
            console.log(counter);
        }
        counter++;
    }
}
function additionPairNumbers() {
    var counter = 1;
    var suma = 0;
    while (counter <= 100) {
        if (counter % 2 == 0) {
            suma += counter;
        }
        counter++;
    }
    return suma;
}
function numbersTenToOne() {
    var counter = 10;
    while (counter > 0) {
        console.log(counter);
        counter -= 1;
    }
}
function fibonacci(number) {
    var a = 0;
    var b = 1;
    var counter = 0;
    console.log(a);
    while (counter <= parseInt(number)) {
        var temp = b;
        b = a + b;
        a = temp;
        console.log(a);
        counter++;
    }
}
function fibonacciNTerms(n) {
    var a = 0;
    var b = 1;
    var counter = 1;
    console.log(a);
    while (counter < parseInt(n)) {
        var temp = b;
        b = a + b;
        a = temp;
        console.log(a);
        counter++;
    }
}
function divisor(number) {
    var counter = 1;
    var parsedNumber = parseInt(number);
    while (counter <= parsedNumber) {
        if (parsedNumber % counter === 0) {
            console.log("el numero ", counter, "es divisible por ", number);
        }
        counter++;
    }
}
function PrimeNumbers() {
    var i = 2;
    while (i <= 100) {
        var isPrimo = true;
        var j = 2;
        while (j < i) {
            if (i % j === 0) {
                isPrimo = false;
                break;
            }
            j++;
        }
        if (isPrimo) {
            console.log(i);
        }
        i++;
    }
}
function isPrimeNumber(number) {
    if (number < 2) {
        return false;
    }
    for (var i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            return false;
        }
    }
    return true;
}
function multiply(number) {
    var counter = 1;
    var parsedNumber = parseInt(number);
    while (counter <= 10) {
        console.log("".concat(parsedNumber, " * ").concat(counter, " = ").concat(parsedNumber * counter));
        counter++;
    }
}
function perfectNumber(number) {
    var counter = 1;
    var suma = 0;
    var parsedNumber = parseInt(number);
    while (counter < parsedNumber) {
        if (parsedNumber % counter === 0) {
            suma += counter;
        }
        counter++;
    }
    if (suma === parsedNumber) {
        return true;
    }
    else {
        return false;
    }
}
function armonicSerie(number) {
    var n = parseInt(number);
    if (Number.isNaN(n) || n <= 0) {
        console.log("Debe ingresar un número entero positivo.");
        rl.close();
        return;
    }
    var i = 1;
    var suma = 0;
    while (i <= n) {
        suma += 1 / i;
        i++;
    }
    console.log("La suma de los primeros ".concat(n, " t\u00E9rminos de la serie arm\u00F3nica es: ").concat(suma));
}
function palindrome(number) {
    var numberFormat = String(number);
    var reversedNumber = '';
    var i = numberFormat.length - 1;
    while (i >= 0) {
        reversedNumber += numberFormat[i];
        i--;
    }
    if (numberFormat === reversedNumber) {
        console.log("".concat(number, " es un pal\u00EDndromo."));
    }
    else {
        console.log("".concat(number, " no es un pal\u00EDndromo."));
    }
}
function preguntarOpcion() {
    console.log("1 -> Numeros del 1 al 10");
    console.log("2 -> Suma de los 100 primeros numeros naturales");
    console.log("3 -> Imprimir números");
    console.log("4 -> Numeros pares del 1 al 10");
    console.log("5 -> Numeros pares hasta n numero");
    console.log("6 -> Factorial de un numero");
    console.log("7 -> Suma de los digitos de un numero");
    console.log("8 -> Multiplos de 3 hasta 100");
    console.log("9 -> Numeros impares hasta n numero");
    console.log("10 -> Suma de numeros pares del 1 al 100");
    console.log("11 -> Numeros del 10 al 1");
    console.log("12 -> Serie fibonacci");
    console.log("13 -> Serie fibonacci hasta n términos");
    console.log("14 -> Divisores de un numero");
    console.log("15 -> Numeros primos del 1 al 100");
    console.log("16 -> Comprobar si un número es primo");
    console.log("17 -> Tabla de multiplicar");
    console.log("18 -> Numero perfecto");
    console.log("19 -> Suma de serie armonica");
    console.log("20 -> Numeros palindromos");
    rl.question("Selecciona una opción o 0 para salir: ", function (option) {
        switch (option) {
            case "1":
                numbersOnetoTen();
                break;
            case "2":
                naturalNumbers();
                break;
            case "3":
                rl.question("Ingresa un número: ", function (numero) {
                    printNumbers(numero);
                    preguntarOpcion();
                });
                return;
            case "4":
                pairNumbersOfTen();
                break;
            case "5":
                rl.question("Ingresa un número: ", function (numero) {
                    pairNumbersOfUserNumber(numero);
                    preguntarOpcion();
                });
                return;
            case "6":
                rl.question("Ingresa un número: ", function (numero) {
                    console.log("el factorial de ".concat(numero, " es ").concat(factorial(numero)));
                    preguntarOpcion();
                });
                return;
            case "7":
                rl.question("Ingresa un número: ", function (numero) {
                    console.log("la suma de los digitos de ".concat(numero, " es ").concat(digits_addition(numero)));
                    preguntarOpcion();
                });
                return;
            case "8":
                threeMultiply();
                break;
            case "9":
                rl.question("Ingresa un número: ", function (numero) {
                    oddNumbers(numero);
                    preguntarOpcion();
                });
                return;
            case "10":
                console.log("la suma de los numeros pares del 1 al 100 es: ".concat(additionPairNumbers()));
                break;
            case "11":
                numbersTenToOne();
                break;
            case "12":
                rl.question("Ingresa un número: ", function (numero) {
                    fibonacci(numero);
                    preguntarOpcion();
                });
                return;
            case "13":
                rl.question("Ingresa un número: ", function (numero) {
                    fibonacciNTerms(numero);
                    preguntarOpcion();
                });
                return;
            case "14":
                rl.question("Ingresa un número: ", function (numero) {
                    divisor(numero);
                    preguntarOpcion();
                });
                return;
            case "15":
                PrimeNumbers();
                break;
            case "16":
                rl.question("Ingresa un número: ", function (numero) {
                    console.log(isPrimeNumber(parseInt(numero)) === true
                        ? "El numero es primo"
                        : "El numero no es primo");
                    preguntarOpcion();
                });
                return;
            case "17":
                rl.question("Ingresa un número: ", function (numero) {
                    multiply(numero);
                    preguntarOpcion();
                });
                return;
            case "18":
                rl.question("Ingresa un número: ", function (numero) {
                    console.log(perfectNumber(numero) === true
                        ? "El numero es perfecto"
                        : "El numero no es perfecto");
                    preguntarOpcion();
                });
                return;
            case "19":
                rl.question("Ingresa un número: ", function (numero) {
                    armonicSerie(numero);
                    preguntarOpcion();
                });
                return;
            case "20":
                rl.question("Ingresa un número: ", function (numero) {
                    palindrome(numero);
                    preguntarOpcion();
                });
                return;
            case "0":
                console.log("Saliendo...");
                rl.close();
                return;
            default:
                console.log("Opción no válida");
                break;
        }
        preguntarOpcion();
    });
}
preguntarOpcion();
