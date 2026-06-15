from validaciones import validar_entero, validar_nombre
from gestion import agregar_pais, actualizar_datos, buscar_por_nombre
from archivos import cargar_paises_csv, guardar_paises_csv
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
        if n==1:
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
        if n==2:
            nombre_buscado=validar_nombre('Ingrese el nombre del país que desea actualizar: ')
            nueva_pob=validar_entero('Ingrese la población: ')
            nueva_sup=validar_entero('Ingrese la superficie: ')
            exito=actualizar_datos(lista_paises, nombre_buscado, nueva_pob, nueva_sup)
            if exito:
                guardar_paises_csv(nombre_archivo, lista_paises)
            else:
                print(f'{nombre_buscado} no encontrado')
        if n==3:
            nombre_buscar=validar_nombre('Ingrese el país que desea buscar: ')
            coincidencia=buscar_por_nombre(lista_paises, nombre_buscar)
        if n==4:
            pass
        if n==5:
            pass
        if n==6:
            pass
    except ValueError as e:
        print(f'Error: {e}')