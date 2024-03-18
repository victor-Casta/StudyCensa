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
    for( let i: number = 2; i <= finalNumber; i += 2) {
      console.log(i);
    }
  }

  pairNumber(10)

  //Escribe un programa que solicite al usuario un número entero positivo y luego imprima la tabla de multiplicar de ese número hasta el 10.
  function multiplicationTable(number: number) {
    let counter: number = 1
    while(counter <= 10) {
      console.log(number * counter)
      counter++;
    }
  }

  multiplicationTable(5)

})()