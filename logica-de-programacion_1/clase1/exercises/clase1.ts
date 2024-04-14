(() => {
 function addition(numberOne: number, numberTwo: number): number {
  return numberOne + numberTwo;
 }
 function substract(numberOne: number, numberTwo: number): number {
  return numberOne - numberTwo;
 }
 function multiply(numberOne: number, numberTwo: number): number {
  return numberOne * numberTwo;
 }
 function division(numberOne: number, numberTwo: number): number {
  return numberOne / numberTwo;
 }
 function triangleArea(base: number, height: number): number {
  return (base * height) / 2
 }

 console.log(addition(8,9))
 console.log(substract(6,3))
 console.log(multiply(8,9))
 console.log(division(4,2))
 console.log(triangleArea(8, 9))
})()