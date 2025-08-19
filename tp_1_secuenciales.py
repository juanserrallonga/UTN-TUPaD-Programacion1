opcion = int(input("ingrese el numero de ejercicio")) 

if opcion == 1:
   
    #1
    print("Hola mundo!")

elif opcion == 2:
   
    #2
    nombre = input("ingrese su nombre ")
    print(f"hola {nombre}!")

elif opcion == 3:
   
    #3
    nombre = input("ingrese su nombre")
    apellido = input("ingrese su apellido")
    edad = input("ingrese su edad")
    pais = input("ingrese su pais de residencia")
    print(f"soy {nombre} {apellido} tengo {edad} anios y vivo en {pais} ")

elif opcion == 4:

    #4
    radio = int(input("ingresa el radio de un circulo"))
    perimetro = 2 * 3.14159 * radio
    area = 3.14159 * radio * radio
    print(f"el perimetro es {perimetro}")
    print(f"el area es {area}")

elif opcion == 5:

    #5
    segundos = int(input("ingresa los segundos que quiera convertir a horas"))
    horas = (segundos // 60) // 60
    print(f"son {horas} horas")

elif opcion == 6:

    #6
    num = int(input("ingresa un numero para ver su tabla de multiplicar"))
    i = 0
    while i <= num:
        res = num * i
        print(f"{i} X {num} = {res}")
        i += 1

elif opcion == 7:

    #7
    num1 = int(input("ingresa un numero distinto de 0"))
    num2 = int(input("ingresa un numero distinto de 0"))
    res = 0
    if num1 and num2 != 0:
        res = num1 + num2
        print(f"suma: {res}")
        res = num1 - num2
        print(f"resta: {res}")
        res = num1 / num2
        print(f"division: {res}")
        res = num1 * num2
        print(f"multiplicacion: {res}")

elif opcion == 8:

    #8
    altura = int(input("ingresa la altura en centimetros"))
    peso = int(input("ingresa su peso en kilos"))
    altura = altura / 100
    masa = peso / (altura*altura)
    print(f"su indice de masa corporal es {masa}")

elif opcion == 9:

    #9
    celsius = int(input("ingresa los grados celsius"))
    celsius = (9/5) * celsius + 32 
    print(f"es {celsius} grados fahrenheit")

elif opcion == 10:

    #10
    num1 = int(input(" ingresa un numero"))
    num2 = int(input(" ingresa un numero"))
    num3 = int(input(" ingresa un numero"))
    res = (num1 + num2 + num3) / 3
    print(f"el promedio es {res}")
else:
    print("Opción inválida")


