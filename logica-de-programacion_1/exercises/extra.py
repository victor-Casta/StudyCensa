# Hacer un algoritmo que lea el nombre, edad, sexo, estado civil de una cantidad de personas, hallar la suma total de todas las edades, la suma de edad de las mujeres, de los hombres, cantidad de hombres, cantidad de mujeres, edad promedio de los hombres edad promedio de las mujeres

total_edad = 0
suma_edad_mujeres = 0
suma_edad_hombres = 0
cantidad_hombres = 0
cantidad_mujeres = 0
edad_promedio_hombres = 0
edad_promedio_mujeres = 0


cantidad_personas = int(input("Ingrese la cantidad de personas a analizar: "))

for i in range(cantidad_personas):
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    sexo = input("Ingrese el sexo de la persona (M/F): ")
    estado_civil = input("Ingrese el estado civil de la persona: ")

    total_edad += edad

    if sexo.upper() == 'F':
        suma_edad_mujeres += edad
        cantidad_mujeres += 1
    elif sexo.upper() == 'M':
        suma_edad_hombres += edad
        cantidad_hombres += 1

if cantidad_hombres > 0:
    edad_promedio_hombres = suma_edad_hombres / cantidad_hombres

if cantidad_mujeres > 0:
    edad_promedio_mujeres = suma_edad_mujeres / cantidad_mujeres

print("Suma total de todas las edades:", total_edad)
print("Suma de edades de las mujeres:", suma_edad_mujeres)
print("Suma de edades de los hombres:", suma_edad_hombres)
print("Cantidad de hombres:", cantidad_hombres)
print("Cantidad de mujeres:", cantidad_mujeres)
print("Edad promedio de los hombres:", edad_promedio_hombres)
print("Edad promedio de las mujeres:", edad_promedio_mujeres)