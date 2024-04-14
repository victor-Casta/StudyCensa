function addition(numberOne, numberTwo) {
  return numberOne + numberTwo;
}

function substract(numberOne, numberTwo) {
 return numberOne - numberTwo;
}

function multiply(numberOne, numberTwo) {
 return numberOne * numberTwo;
}

function divide(numberOne, numberTwo) {
 return numberOne / numberTwo;
}

function triangleArea(base, height) {
 return (base * height) / 2
}

console.log(addition(8, 2))
console.log(substract(9, 1))
console.log(multiply(9, 9))
console.log(divide(4, 2))
console.log(triangleArea(8, 9))

// de celsius a fahrenheit
//°F = (°C x 9/5) + 32

function converter( celsius ) {
  let fahrenheit = ( celsius * 9/5) + 32
  return fahrenheit
}

console.log(`${converter(32)} °F`)

//print result

function printResult() {
  console.log(((8 * 2) / 6) + 4)
}

printResult()

//notes average
function gradeAverage(notes) {
  let addition = 0
  for (let i = 0; i < notes.length; i++) {
    addition += notes[i]
  }
  return addition / notes.length
}

let notesList = [4.0, 2.7, 3.2]
console.log(`El promedio de notas es: ${gradeAverage(notesList)}`)