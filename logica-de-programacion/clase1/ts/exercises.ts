(() => {
  //Escribe un programa que imprima los números del 1 al 10 en una línea separada.
  let counter: number = 1;
  while (counter <= 10) {
    console.log(counter);
    counter++;
  }

  //Crea un programa que calcule la suma de los primeros 100 números naturales.
  let addition: number = 0;
  for (let i: number = 0; i <= 100; i++) {
    addition += i;
  }
  console.log(addition);

  //Desarrolla un programa que solicite al usuario un número entero positivo y luego imprima todos los números pares desde 2 hasta ese número.
  function pairNumber(finalNumber: number) {
    for (let i: number = 2; i <= finalNumber; i += 2) {
      console.log(i);
    }
  }

  pairNumber(10);

  //Escribe un programa que solicite al usuario un número entero positivo y luego imprima la tabla de multiplicar de ese número hasta el 10.
  function multiplicationTable(number: number) {
    let counter: number = 1;
    while (counter <= 10) {
      console.log(number * counter);
      counter++;
    }
  }

  multiplicationTable(5);

  //Crea un programa que calcule el factorial de un número ingresado por el usuario.
  function Factorial(number: number): number {
    let counter: number = 1;
    let factorial: number = 1;
    while (counter <= number) {
      factorial *= counter;
      counter++;
    }
    return factorial;
  }

  console.log(`El Factorial es: ${Factorial(3)}`);

  //Desarrolla un programa que pida al usuario un número entero positivo y luego imprima todos los números primos menores o iguales a ese número.
  function NumbersPrimosMenores(number: number): void {
    let counter: number = 2;
    while (counter <= number) {
      let IsPrimo: boolean = true;
      let j: number = 2
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

  //Escribe un programa que genere e imprima los primeros 20 términos de la secuencia de Fibonacci.
  function Fibonnacci(number: number): void {
    let a: number = 0
    let b: number = 1
    let counter: number = 0

    console.log(a)

    while (counter <= number) {
      let temp: number = b;
      b = a + b;
      a = temp;
      console.log(a)
      counter++;
    }
  }

  Fibonnacci(10);
})();