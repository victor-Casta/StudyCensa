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


console.log("1 -> Numeros del 1 al 10");
console.log("2 -> Suma de los 100 primeros numeros naturales");
console.log("3 -> Imprimir números");
console.log("4 -> Numeros pares del 1 al 10");
console.log("5 -> Numeros pares hasta n numero");
console.log("6 -> Factorial de un numero");
console.log("7 -> Suma de los digitos de un numero");

function preguntarOpcion() {
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
          console.log(`la suma de los digitos de ${numero} es ${digits_addition(numero)}`);
          preguntarOpcion();
        });
        return;
      case "8":
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
