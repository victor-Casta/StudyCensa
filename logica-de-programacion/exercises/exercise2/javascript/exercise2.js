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
