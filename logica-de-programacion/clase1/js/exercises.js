"use strict";
(() => {
    //Escribe un programa que imprima los números del 1 al 10 en una línea separada.
    let counter = 1;
    while (counter <= 10) {
        console.log(counter);
        counter++;
    }
    //Crea un programa que calcule la suma de los primeros 100 números naturales.
    let addition = 0;
    for (let i = 0; i <= 100; i++) {
        addition += i;
    }
    console.log(addition);
    //Desarrolla un programa que solicite al usuario un número entero positivo y luego imprima todos los números pares desde 2 hasta ese número.
    function pairNumber(finalNumber) {
        for (let i = 2; i <= finalNumber; i += 2) {
            console.log(i);
        }
    }
    pairNumber(10);
    //Escribe un programa que solicite al usuario un número entero positivo y luego imprima la tabla de multiplicar de ese número hasta el 10.
    function multiplicationTable(number) {
        let counter = 1;
        while (counter <= 10) {
            console.log(number * counter);
            counter++;
        }
    }
    multiplicationTable(5);
    //Crea un programa que calcule el factorial de un número ingresado por el usuario.
    function Factorial(number) {
        let counter = 1;
        let factorial = 1;
        while (counter <= number) {
            factorial *= counter;
            counter++;
        }
        return factorial;
    }
    console.log(`El Factorial es: ${Factorial(3)}`);
    //Desarrolla un programa que pida al usuario un número entero positivo y luego imprima todos los números primos menores o iguales a ese número.
    function NumbersPrimosMenores(number) {
        let counter = 2;
        while (counter <= number) {
            let IsPrimo = true;
            let j = 2;
            while (j < counter) {
                if (counter % j === 0) {
                    IsPrimo = false;
                    break;
                }
                j++;
            }
            if (IsPrimo) {
                console.log(counter);
            }
            counter++;
        }
    }
    NumbersPrimosMenores(10);
})();
