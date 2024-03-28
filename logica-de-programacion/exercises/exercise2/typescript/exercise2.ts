import { createInterface } from "readline";

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

function numbersOnetoTen(): void {
  let counter = 1;
  while (counter <= 10) {
    console.log(counter);
    counter++;
  }
}

function naturalNumbers(): void {
  let counter = 0;
  let suma = 0;
  while (counter <= 100) {
    suma += counter;
    counter++;
  }
  console.log("la suma de los 100 primeros números naturales es: ", suma);
}

function printNumbers(number: string): void {
  let i = 1;
  while (i <= parseInt(number)) {
    console.log(i);
    i++;
  }
}

function pairNumbersOfTen(): void {
  let counter = 2;
  while (counter <= 10) {
    console.log(counter);
    counter += 2;
  }
}

function pairNumbersOfUserNumber(number: string): void {
  let counter = 2;
  while (counter <= parseInt(number)) {
    console.log(counter);
    counter += 2;
  }
}

function factorial(number: string): number {
  let factorial = 1;
  let counter = 1;
  while (counter <= parseInt(number)) {
    factorial *= counter;
    counter++;
  }
  return factorial;
}

function digits_addition(number: string): number {
  let counter = 0;
  let suma = 0;
  while (counter < number.length) {
    let numberUnited = parseInt(number[counter]);
    suma += numberUnited;
    counter++;
  }
  return suma;
}

function threeMultiply(): void {
  let counter = 1;
  while (counter <= 100) {
    console.log(counter * 3);
    counter++;
  }
}

function oddNumbers(number: string): void {
  let counter = 1;
  while (counter <= parseInt(number)) {
    if (counter % 2 !== 0) {
      console.log(counter);
    }
    counter++;
  }
}

function additionPairNumbers(): number {
  let counter = 1;
  let suma = 0;
  while (counter <= 100) {
    if (counter % 2 == 0) {
      suma += counter;
    }
    counter++;
  }
  return suma;
}

function numbersTenToOne(): void {
  let counter: number = 10;
  while (counter > 0) {
    console.log(counter);
    counter -= 1;
  }
}

function fibonacci(number: string): void {
  let a: number = 0;
  let b: number = 1;
  let counter: number = 0;
  console.log(a);
  while (counter <= parseInt(number)) {
    let temp: number = b;
    b = a + b;
    a = temp;
    console.log(a);
    counter++;
  }
}

function fibonacciNTerms(n: string): void {
  let a: number = 0;
  let b: number = 1;
  let counter = 1;

  console.log(a);

  while (counter < parseInt(n)) {
    let temp: number = b;
    b = a + b;
    a = temp;
    console.log(a);
    counter++;
  }
}

function divisor(number: string): void {
  let counter: number = 1;
  let parsedNumber: number = parseInt(number);
  while (counter <= parsedNumber) {
    if (parsedNumber % counter === 0) {
      console.log("el numero ", counter, "es divisible por ", number);
    }
    counter++;
  }
}

function PrimeNumbers(): void {
  let i = 2;

  while (i <= 100) {
    let isPrimo = true;
    let j = 2;
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

function isPrimeNumber(number: number): boolean {
  if (number < 2) {
    return false;
  }

  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      return false;
    }
  }

  return true;
}

function multiply(number: string): void {
  let counter: number = 1;
  let parsedNumber: number = parseInt(number);
  while (counter <= 10) {
    console.log(`${parsedNumber} * ${counter} = ${parsedNumber * counter}`);
    counter++;
  }
}

function perfectNumber(number: string): boolean {
  let counter = 1;
  let suma = 0;
  let parsedNumber: number = parseInt(number);
  while (counter < parsedNumber) {
    if (parsedNumber % counter === 0) {
      suma += counter;
    }
    counter++;
  }
  if (suma === parsedNumber) {
    return true;
  } else {
    return false;
  }
}

function armonicSerie(number: string) {
  const n = parseInt(number);

  if (Number.isNaN(n) || n <= 0) {
    console.log("Debe ingresar un número entero positivo.");
    rl.close();
    return;
  }

  let i = 1;
  let suma = 0;

  while (i <= n) {
    suma += 1 / i;
    i++;
  }

  console.log(
    `La suma de los primeros ${n} términos de la serie armónica es: ${suma}`
  );
}

function palindrome(number: string): void {
  const numberFormat = String(number);
  let reversedNumber = '';
  let i = numberFormat.length - 1;

  while (i >= 0) {
    reversedNumber += numberFormat[i];
    i--;
  }

  if (numberFormat === reversedNumber) {
    console.log(`${number} es un palíndromo.`);
  } else {
    console.log(`${number} no es un palíndromo.`);
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

  rl.question("Selecciona una opción o 0 para salir: ", (option: string) => {
    switch (option) {
      case "1":
        numbersOnetoTen();
        break;
      case "2":
        naturalNumbers();
        break;
      case "3":
        rl.question("Ingresa un número: ", (numero: string) => {
          printNumbers(numero);
          preguntarOpcion();
        });
        return;
      case "4":
        pairNumbersOfTen();
        break;
      case "5":
        rl.question("Ingresa un número: ", (numero: string) => {
          pairNumbersOfUserNumber(numero);
          preguntarOpcion();
        });
        return;
      case "6":
        rl.question("Ingresa un número: ", (numero: string) => {
          console.log(`el factorial de ${numero} es ${factorial(numero)}`);
          preguntarOpcion();
        });
        return;
      case "7":
        rl.question("Ingresa un número: ", (numero: string) => {
          console.log(
            `la suma de los digitos de ${numero} es ${digits_addition(numero)}`
          );
          preguntarOpcion();
        });
        return;
      case "8":
        threeMultiply();
        break;
      case "9":
        rl.question("Ingresa un número: ", (numero: string) => {
          oddNumbers(numero);
          preguntarOpcion();
        });
        return;
      case "10":
        console.log(
          `la suma de los numeros pares del 1 al 100 es: ${additionPairNumbers()}`
        );
        break;
      case "11":
        numbersTenToOne();
        break;
      case "12":
        rl.question("Ingresa un número: ", (numero: string) => {
          fibonacci(numero);
          preguntarOpcion();
        });
        return;
      case "13":
        rl.question("Ingresa un número: ", (numero: string) => {
          fibonacciNTerms(numero);
          preguntarOpcion();
        });
        return;
      case "14":
        rl.question("Ingresa un número: ", (numero: string) => {
          divisor(numero);
          preguntarOpcion();
        });
        return;
      case "15":
        PrimeNumbers();
        break;
      case "16":
        rl.question("Ingresa un número: ", (numero: string) => {
          console.log(
            isPrimeNumber(parseInt(numero)) === true
              ? "El numero es primo"
              : "El numero no es primo"
          );
          preguntarOpcion();
        });
        return;
      case "17":
        rl.question("Ingresa un número: ", (numero: string) => {
          multiply(numero);
          preguntarOpcion();
        });
        return;
      case "18":
        rl.question("Ingresa un número: ", (numero: string) => {
          console.log(
            perfectNumber(numero) === true
              ? "El numero es perfecto"
              : "El numero no es perfecto"
          );
          preguntarOpcion();
        });
        return;
      case "19":
        rl.question("Ingresa un número: ", (numero: string) => {
          armonicSerie(numero);
          preguntarOpcion();
        });
        return;
      case "20":
        rl.question("Ingresa un número: ", (numero: string) => {
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