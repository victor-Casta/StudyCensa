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
})();