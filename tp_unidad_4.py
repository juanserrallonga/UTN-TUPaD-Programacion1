import random

opcion = int(input(("ingrese el numero de ejercicio")))

digitos = 0

if opcion == 1:

    numero = 0

    while numero <= 100:

        print(f"{numero}")

        numero += 1

elif opcion == 2:

    numero = int(input("ingrese un numero"))

    while numero // 10 > 0:

        digitos = digitos + 1

        numero = numero // 10
    
    digitos = digitos + 1

    print(f"{digitos} digitos")

elif opcion == 3:

    num1 = int(input("ingrese un numero"))
    
    num2 = int(input("ingrese otro numero"))

    suma = 0

    aux1 = num1

    aux2 = num2 

    while aux1 > aux2 :

        if aux1 -1 >= aux2 +1:
           
            suma += aux1 + aux2
        
        aux1 -= 1
        
        aux2 += 1
   
    while aux1 < aux2 :

        if aux1 +1 <= aux2 -1:
           
            suma += aux1 + aux2

        aux1 += 1

        aux2 -= 1

    print(f"{suma}")

elif opcion == 4:
    
    num = 1

    suma = 0

    while num != 0:

        num = int(input("ingrese numeros para sumarlos, para salir ingresa 0"))
    
        suma += num

    print(f"la suma es {suma}")

elif opcion == 5:

    intentos = 0

    num = 10

    random = random.randint(0, 9)
    
    while num != random:
        
        num = int(input("ingrese un numero del 0 al 9"))

        intentos += 1

    print(f"felicitaciones, adivinaste el numero en {intentos} intentos")    

elif opcion == 6:

    numero = 102

    while numero > 0:

        numero = numero - 2

        print(f"{numero}")

elif opcion == 7:

    i = 0

    suma = 0

    numero = int(input("ingrese un numero"))

    for i in range(0, numero + 1):

        suma += i 
    
    print(f"la suma es {suma}")

elif opcion == 8:

    par = 0

    impar = 0

    positivo = 0    

    negativo = 0

    num = 1

    while num != 0:

        num = int(input("ingrese numeros, para terminar ingresa 0"))

        if num % 2 == 0:

            par += 1
        
        else:

            impar += 1

        if num > 0:

            positivo += 1

        else:

            negativo += 1
        
    print(f"pares: {par}, impares: {impar}, positivos: {positivo}, negativos: {negativo}")

elif opcion == 9:

    media = 0

    num = 1

    contador = 0

    while num != 0: 

        contador += 1

        num = int(input("ingrese numeros, para terminar ingresa 0"))

        media += num

    media = media // contador

    print(f"la media es {media}")

elif opcion == 10:

    num = int(input("ingrese un numero"))

    numero = num

    aux = 0

    digitos = 0
    
    dig = 0

    invertido = 0

    while numero // 10 > 0:

        dig = dig + 1

        numero = numero // 10
    
    dig = dig + 1

    aux = dig

    dig = 1

    while aux > 1:

        dig = dig * 10
        
        aux -= 1

    while num // 10 > 0:
        
        digitos = num % 10

        invertido += digitos * dig

        dig = dig // 10

        num = num // 10
    
    invertido += num

    print(f"el numero invertido es {invertido}")

