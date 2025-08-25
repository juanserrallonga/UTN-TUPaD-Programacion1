
import random

from statistics import mode, median, mean

opcion = int(input(("ingrese el numero de ejercicio")))

if opcion == 1:
 
    edad = int(input("Ingrese su edad:"))
 
    if edad >= 18:
 
        print("Usted es mayor de edad")
 
    else:
 
        print("Usted es menor de edad")

elif opcion == 2:
    
    nota = int(input("Ingrese su nota:"))

    if nota >= 6:
        
        print("Aprobado")
    
    else:
        
        print("Desaprobado")

elif opcion == 3:

    numero = int(input("Ingrese numeros que sean pares"))

    while numero % 2 != 0:

        print("El numero no es par, ingrese otro numero")

        numero = int(input("Ingrese numeros que sean pares"))
    
    else:

        print("El numero es par")

elif opcion == 4:

    edad = int(input("Ingrese su edad:"))

    if edad < 12:
    
        print("Usted es un niño")

    if edad >= 12 and edad < 18:
    
        print("Usted es un adolescente")

    if edad >= 18 and edad < 30:
    
        print("Usted es un adulto joven")

    if edad >= 30:
    
        print("Usted es un adulto")

elif opcion == 5:

    contracenia = input("Ingrese su contraseña entre 8 y 14 caracteres:")

    while len(contracenia) < 8 or len(contracenia) > 14:

        print("Contraseña incorrecta, ingrese nuevamente")

        contracenia = input("Ingrese su contraseña entre 8 y 14 caracteres:")

    print("ha ingresado una Contraseña correcta")

elif opcion == 6:

    numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

    moda_valor = mode(numeros_aleatorios)

    mediana_valor = median(numeros_aleatorios)
    
    media_valor = mean(numeros_aleatorios)

    if media_valor > mediana_valor and mediana_valor > moda_valor:
    
        sesgo = "Sesgo positivo o a la derecha"
    
    elif media_valor < mediana_valor and mediana_valor < moda_valor:
    
        sesgo = "Sesgo negativo o a la izquierda"
    
    else:
    
        sesgo = "Sin sesgo"

    print("Lista de números aleatorios:")
    
    print(numeros_aleatorios)
    
    print(f"\nMedia: {media_valor:.2f}")
    
    print(f"Mediana: {mediana_valor:.2f}")
    
    print(f"Moda: {moda_valor}")
    
    print(f"\nResultado: {sesgo}")

elif opcion == 7:

    palabra = input("Ingrese una palabra:")

    if  palabra[len(palabra)- 1] == "a" or palabra[len(palabra)- 1] == "e" or palabra[len(palabra)- 1] == "i" or palabra[len(palabra)- 1] == "o" or palabra[len(palabra)- 1] == "u":

        palabra = palabra[:] + "!"

    print(palabra)

elif opcion == 8:

    nombre = input("Ingrese su nombre:")

    opcion = int(input("Ingrese 1 para todo mayusculas o 2 para todo minusculas y 3 para solo la primer letra mayuscula:"))

    if opcion == 1:

        nombre = nombre.upper()

    
    if opcion == 2:

        nombre = nombre.lower()

        
    if opcion == 3:

        nombre = nombre.capitalize()

    print(nombre)

elif opcion == 9:

    magnitud = float(input("Ingrese la magnitud del terremoto:"))

    if magnitud < 3.0:

        print("muy leve")
    
    if magnitud >= 3.0 and magnitud < 4.0:

        print("leve")
    
    if magnitud >= 4.0 and magnitud < 5.0:

        print("moderado")
        
    if magnitud >= 5.0 and magnitud < 6.0:

        print("fuerte")

    if magnitud >= 6.0 and magnitud < 7.0:

        print("muy fuerte")

    if magnitud >= 7.0:

        print("extremo")

elif opcion == 10:

    emisferio = input("Ingrese el hemisferio en el que vive (N/S):").lower()

    mes = int(input("Ingrese el mes en el que se encuentra:"))

    dia = int(input("Ingrese el dia en el que se encuentra:"))

    if emisferio == "n":

        if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia < 21:

            print("Invierno")

    if emisferio == "s":

        if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia < 21:

            print("verano")

    if emisferio == "n":

        if mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia < 21:

            print("primavera")

    if emisferio == "s":

        if mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia < 21:

            print("otonio")

    if emisferio == "n":

        if mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 21:

            print("verano")

    if emisferio == "n":

        if mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 21:

            print("invierno")

    if emisferio == "n":

        if mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia < 21:

            print("otonio")
            
    if emisferio == "s":

        if mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia < 21:

            print("primavera")