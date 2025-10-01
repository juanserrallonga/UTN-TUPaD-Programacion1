
import random

opcion = int(input(("ingrese el numero de ejercicio")))

i = 0

if opcion == 1:

    notas = [2,1,10,9,7,8,5,5,3]

    cont = len(notas) - 1

    alta = 0

    baja = 10

    promedio = 0

    print(notas)

    while cont > 0:

        promedio += notas[cont]

        if alta < notas[cont]:

            alta = notas[cont]
        
        if baja > notas[cont]:

            baja = notas[cont]

        cont -= 1

    promedio = promedio / len(notas) 

    print(f"el promedio es {promedio}")

    print(f"la nota mas alta es {alta}")

    print(f"la nota mas baja es {baja}")


if opcion == 2:

    i = int(input("ingrese el tamanio de la lista"))

    lista = [""] * i

    i = i - 1

    while i >= 0:

        lista[i] = input("ingrese un producto") 

        i += -1

    lista = sorted(lista)

    print(lista)

    i = 0
 
    opcion = input("ingrese el producto  que desea eliminar")

    if opcion in lista:

        while i < len(lista):
           
            if lista[i] == opcion:

                print(f"se elimino el producto {lista[i]}")

                lista[i] = ""

            i += 1

    else:

         print("el producto no se encuentra en la lista")

    print(sorted(lista))

    opcion = 0

    i = 0

if opcion == 3:

    i = int(input("ingrese el tamanio de la lista"))

    a = 0

    b = 0

    rnd = [0] * i 

    pa = 0

    im = 0
    
    while i > 0:   

        rnd[i - 1] = random.randint(1, 100)
        
        if rnd[i - 1] != 0:
           
            if rnd[i - 1] % 2 == 0:

                pa += 1

            else:

                im += 1

        i -= 1

    i = 0

    print(rnd)

    par = [0] * pa

    impar = [0] * im

    while i < len(rnd):

        if rnd[i] % 2 == 0:

            par[a] = rnd[i]

            a += 1

        else: 

            impar[b] = rnd[i]

            b += 1

        i += 1

    print(f"pares: {par}")

    print(f"impares: {impar}")

if opcion == 4:

    datos = [1,3,5,3,7,1,9,5,3]

    sinrepetir = [0] * len(datos) 

    i = 0

    b = 0

    while i < len(datos):

        if datos[i] in sinrepetir:

            a = 0

        else:

            sinrepetir[b] = datos[i]

            b += 1

        if sinrepetir[i] == 0:

            sinrepetir[i] = ""

        i += 1

    print(sinrepetir)

if opcion == 5:

    estudiantes = ["Juan", "Luis", "María", "Carlos", "Sofia", "Pedro", "Laura", "Diego"]

    print("Lista actual:", estudiantes)
    
    while True:
      
        print("1. agregar estudiante")
        
        print("2. eliminar estudiante")
        
        opcion = input("Elige una opción (1 o 2): ")
        
        if opcion == "1":

            nuevo = input("Ingresa el nombre del nuevo estudiante: ")
            
            estudiantes.append(nuevo)
           
            print(f"{nuevo} agregado a la lista")
            
        elif opcion == "2":
            
            eliminar = input("Ingresa el nombre del estudiante a eliminar: ")
            
            if eliminar in estudiantes:
                
                estudiantes.remove(eliminar)
                
                print(f"{eliminar} eliminado de la lista")
            
            else:
                
                print("Estudiante no encontrado")
        
        print("Lista actualizada:", estudiantes)

if opcion == 6:

    i = 0

    numeros = [1, 2, 3, 4, 5, 6, 7]

    print("Lista original:", numeros)

    ultimo = numeros[-1]  

    i = len(numeros) - 1

    while i > 0:
       
        numeros[i] = numeros[i-1]
        
        i -= 1

    numeros[0] = ultimo

    print("Lista rotada:", numeros)

if opcion == 7:

    temperaturas = [[15, 25],[16, 28],[14, 26],[17, 30],[18, 32],[16, 29],[15, 27]]

    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    suma_minimas = 0

    suma_maximas = 0

    for temp in temperaturas:
    
        suma_minimas += temp[0]
        
        suma_maximas += temp[1]

    promedio_min = suma_minimas / len(temperaturas)

    promedio_max = suma_maximas / len(temperaturas)

    print(f" Promedio de minimas: {promedio_min}°C")

    print(f" Promedio de maximas: {promedio_max}°C")

    mayor_amplitud = 0

    dia_mayor = 0

    i = 0

    while i < len(temperaturas):
        
        amplitud = temperaturas[i][1] - temperaturas[i][0]
    
        if amplitud > mayor_amplitud:
        
            mayor_amplitud = amplitud
        
            dia_mayor = i
    
        i += 1

    print(f"Mayor amplitud termica: {mayor_amplitud}°C el {dias[dia_mayor]}")

if opcion == 8:

    notas = [[7, 8, 6],[9, 7, 8],[6, 5, 7],[8, 9, 9],[7, 6, 8]]

    materias = ["Matematica", "Lengua", "Historia"]

    print("promedio por estudiante:")
   
    i = 0

    while i < len(notas):
       
        suma = 0
       
        for nota in notas[i]:
            
            suma += nota
        
        promedio = suma / len(notas[i])
        
        print(f"Estudiante {i + 1}: {promedio}")
       
        i += 1

    print("promedio por materia:")

    j = 0
    
    while j < len(materias):
       
        suma_materia = 0
       
        for estudiante in notas:
          
            suma_materia += estudiante[j]
      
        promedio_materia = suma_materia / len(notas)
        
        print(f"{materias[j]}: {promedio_materia}")
 
        j += 1

if opcion == 9:

    j = 0

    end = 0

    tablero = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

    jugador_actual = "X"

    jugadas = 0

    print("TA-TE-TI")

    print("Los jugadores son X y O")

    print("posiciones van de 0 a 2 para fila y columna")

    while jugadas < 9:
        
        print("\n  0 1 2")
    
        i = 0
    
        while i < 3:
        
            print(f"{i} ", end="")
        
            j = 0
        
            while j < 3:
                
                print(tablero[i][j], end=" ")
            
                j += 1
            
            print()
            
            i += 1
        
        print(f"\nTurno del jugador {jugador_actual}")
        
        posicion_valida = False
        
        while not posicion_valida:
            
            fila_input = input("Fila (0-2): ")
            
            columna_input = input("Columna (0-2): ")
            
            if fila_input in "012" and columna_input in "012":
            
                fila = int(fila_input)
                
                columna = int(columna_input)
                
            
                if tablero[fila][columna] == "-":
                
                    posicion_valida = True
            
                else:
                
                    print("Esa casilla ya está ocupada")
        
            else:
                
                print("Ingresa números del 0 al 2")
        
        tablero[fila][columna] = jugador_actual
    
        jugadas += 1
    
        if jugador_actual == "X":
        
            jugador_actual = "O"
        
        else:
        
            jugador_actual = "X"

    print("\n JUEGO TERMINADO")

    print("  0 1 2")

    i = 0

    while i < 3:
    
        print(f"{i} ", end="")
    
        j = 0  # ¡Y TAMBIÉN AQUÍ!
    
        while j < 3:
        
            print(tablero[i][j], end=" ")
        
            j += 1
    
        print()
    
        i += 1

if opcion == 10:

    ventas = [[15, 20, 18, 22, 25, 30, 28],[10, 12, 15, 18, 20, 22, 25],[8, 10, 12, 15, 18, 20, 22],[5, 8, 10, 12, 15, 18, 20]]

    productos = ["jabon", "shampoo", "crema facial", "desodorante"]
   
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    print("ventas totales por producto:")

    i = 0
    
    while i < len(ventas):
       
        total_producto = 0
       
        for venta_dia in ventas[i]:
        
            total_producto += venta_dia
       
        print(f"{productos[i]}: {total_producto} unidades")
       
        i += 1

    print("\n DIA CON MAYORES VENTAS TOTALES:")
   
    mayor_venta_dia = 0
    
    dia_mayor_venta = 0

    j = 0
    
    while j < len(dias):
       
        total_dia = 0
       
        for producto in ventas:
        
            total_dia += producto[j]
        
        if total_dia > mayor_venta_dia:
           
            mayor_venta_dia = total_dia
            
            dia_mayor_venta = j
        
        print(f"{dias[j]}: {total_dia} unidades")
        
        j += 1

    print(f" Día con mayores ventas: {dias[dia_mayor_venta]} con {mayor_venta_dia} unidades")

    producto_mas_vendido = 0
    
    cantidad_mayor = 0

    k = 0
    
    while k < len(ventas):
      
        total = 0
       
        for venta in ventas[k]:
           
            total += venta
        
        if total > cantidad_mayor:
            
            cantidad_mayor = total
           
            producto_mas_vendido = k
      
        k += 1

    print(f"Producto más vendido: {productos[producto_mas_vendido]} con {cantidad_mayor} unidades")