//Numeros del 1 al 10
for (let i = 0; i <= 10; i++) {
  console.log(i);
}

//numeros naturales del 1 al 100
let counter = 0;
for (let i = 0; i <= 100; i++) {
  counter += i;
}
console.log("numeros naturales", counter);

//Desarrolla un programa que solicite al usuario un número entero positivo y luego imprima todos los números pares desde 2 hasta ese número.

function imprimirPares(numero) {
  for (let i = 2; i <= numero; i += 2) {
    console.log(i);
  }
}

imprimirPares(20);

//Escribe un programa que solicite al usuario un número entero positivo y luego imprima la tabla de multiplicar de ese número hasta el 10.

function imprimirMultiplos(numero) {
  for (let i = 1; i <= 10; i++) {
    console.log(i * numero);
  }
}

imprimirMultiplos(5);

//Crea un programa que calcule el factorial de un número ingresado por el usuario
function imprimirFactorial(numero) {
  let factorial = 1;

  for (let i = 1; i <= numero; i++) {
    factorial *= i;
  }
  console.log("factorial:", factorial);
}

imprimirFactorial(3);

//Desarrolla un programa que pida al usuario un número entero positivo y luego imprima todos los números primos menores o iguales a ese número.

function imprimirNumeroPrimo(number) {
  for (let i = 2; i <= number; i++) {
    let esPrimo = true;
    for (let j = 2; j < i; j++) {
      if (i % j === 0) {
        esPrimo = false;
        break;
      }
    }
    if (esPrimo) {
      console.log(i);
    }
  }
}

imprimirNumeroPrimo(10);


//Escribe un programa que genere e imprima los primeros 20 términos de la secuencia de Fibonacci

function Fibonacci(number) {
  let a = 0, b = 1;
  console.log(a);
  console.log(b);
  for (let i = 2; i <= number; i++) {
    let temp = b;
    b = a + b;
    a = temp;
    console.log(b);
  }
}

Fibonacci(6);


//Crea un programa que solicite al usuario una cantidad de segundos y luego convierta ese tiempo a horas, minutos y segundos.

function time(timeInSeconds) {
  const minutes = timeInSeconds * 60
  console.log(minutes);
}

time(1)

