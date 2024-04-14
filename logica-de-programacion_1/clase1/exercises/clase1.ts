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

 // de celsius a fahrenheit
 //°F = (°C x 9/5) + 32
 function converter( celsius:number ): number {
  let fahrenheit = ( celsius * 9/5) + 32
  return fahrenheit
 }

 //print result
function printResult(): void {
 console.log(((8 * 2) / 6) + 4)
}

//notes average
function gradeAverage(notes: Array<number>): number {
 let addition = 0
 for (let i = 0; i < notes.length; i++) {
   addition += notes[i]
 }
 return addition / notes.length
}

let notesList = [4.0, 2.7, 3.2]

 console.log(addition(8,9))
 console.log(substract(6,3))
 console.log(multiply(8,9))
 console.log(division(4,2))
 console.log(triangleArea(8, 9))
 console.log(`${converter(32)} °F`)
 printResult()
 console.log(gradeAverage(notesList))
})()