from validaciones import validar_entero, validar_nombre
from gestion import agregar_pais, actualizar_datos, buscar_por_nombre
from archivos import cargar_paises_csv, guardar_paises_csv
from estadisticas import extremos, prom_pob, prom_sup, cant_paises
from procesamiento import (
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie,
    ordenar_por_nombre,
    ordenar_por_poblacion,
    ordenar_superficie_asc,
    ordenar_superficie_desc,
    mostrar_paises
)

#Menú
n=0
nombre_archivo='paises.csv'
lista_paises=cargar_paises_csv(nombre_archivo)
while n!=7:
    try:
        n=int(input('-----Menú-----\n' \
        '1) Agregar país (nombre,población,superficie,continente)\n' \
        '2) Actualizar datos de Población y Superficie de un país\n' \
        '3) Buscar un país\n' \
        '4) Filtrar países\n' \
        '5) Ordenar países\n' \
        '6) Mostrar estadísticas\n' \
        '7) Salir\n'))
        if n < 1 or n > 7:
            print('Por favor ingrese una opción válida 1-7')
        #Opcion 1
        elif n==1:
            nombre=validar_nombre('Ingrese el nombre del país: ')
            poblacion=validar_entero(f'Ingrese la poblacion de {nombre}: ')
            superficie=validar_entero(f'Ingrese la superficie de {nombre} en km2: ')
            continente=validar_nombre(f'Ingrese el continente de {nombre}: ')
            exito=agregar_pais(lista_paises,nombre,poblacion,superficie,continente)
            if exito:
                print(f"\n¡Éxito! El país '{nombre}' se registró correctamente en la memoria.")
                guardar_paises_csv(nombre_archivo, lista_paises)
            else:
                print(f"\n[Error]: No se pudo agregar. El país '{nombre}' ya se encuentra registrado en el sistema.")

        #Opcion 2
        elif n==2:
            nombre_buscado=validar_nombre('Ingrese el nombre del país que desea actualizar: ')
            nueva_pob=validar_entero('Ingrese la población: ')
            nueva_sup=validar_entero('Ingrese la superficie: ')
            exito=actualizar_datos(lista_paises, nombre_buscado, nueva_pob, nueva_sup)
            if exito:
                guardar_paises_csv(nombre_archivo, lista_paises)
            else:
                print(f'{nombre_buscado} no encontrado')

        #Opcion 3
        elif n==3:
            nombre_buscar=validar_nombre('Ingrese el país que desea buscar: ')
            coincidencia=buscar_por_nombre(lista_paises, nombre_buscar)

        #Opcion 4
        elif n==4:
            opcion_filtro = int(input(
                "\n1) Filtrar por continente\n"
                "2) Filtrar por población\n"
                "3) Filtrar por superficie\n"
            ))

            if opcion_filtro == 1:
                continente = input("Ingrese continente: ")
                resultados = filtrar_por_continente(
                    lista_paises,
                    continente
                )

            elif opcion_filtro == 2:
                minimo = validar_entero("Población mínima: ")
                maximo = validar_entero("Población máxima: ")
                resultados = filtrar_por_poblacion(
                    lista_paises,
                    minimo,
                    maximo
                )

            elif opcion_filtro == 3:
                minimo = validar_entero("Superficie mínima: ")
                maximo = validar_entero("Superficie máxima: ")
                resultados = filtrar_por_superficie(
                    lista_paises,
                    minimo,
                    maximo
                )

            else:
                resultados = []
                print("Opción inválida")

            mostrar_paises(resultados)

        #Opcion 5
        elif n==5:
            opcion_orden = int(input(
            "\n1) Ordenar por nombre\n"
            "2) Ordenar por población\n"
            "3) Superficie ascendente\n"
            "4) Superficie descendente\n"
            ))

            if opcion_orden == 1:
                resultado = ordenar_por_nombre(lista_paises)

            elif opcion_orden == 2:
                resultado = ordenar_por_poblacion(lista_paises)

            elif opcion_orden == 3:
                resultado = ordenar_superficie_asc(lista_paises)

            elif opcion_orden == 4:
                resultado = ordenar_superficie_desc(lista_paises)

            else:
                resultados = []
                print("Opción inválida")
                
            mostrar_paises(resultados)                  

        #Opcion 6
        elif n==6:
            opcion=0
            while opcion!=5:
                try:
                    opcion=int(input('Seleccione la estadistica que desea ver:\n' \
                    '1) País con mayor y menor población\n' \
                    '2) Promedio de población \n' \
                    '3) Promedio de superficie\n' \
                    '4) Cantidad de países por continente\n'
                    '5) Volver\n'))
                    if opcion < 1 or opcion > 5:
                        print('Por favor ingrese una opción válida 1-5')
                    #opcion 1
                    elif opcion==1:
                        extremos(lista_paises)
                    #opcion 2
                    elif opcion==2:
                        prom_pob(lista_paises)
                    #opcion 3
                    elif opcion==3:
                        prom_sup(lista_paises)
                    #opcion 4
                    elif opcion==4:
                        cant_paises(lista_paises)
                except ValueError as e:
                    print(f'Error: {e}')
    except ValueError as e:
        print(f'Error: {e}')