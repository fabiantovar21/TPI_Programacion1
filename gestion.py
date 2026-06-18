#Funcion para agregar pais
def agregar_pais(lista_paises,nombre,poblacion,superficie,continente):
    # Validación: Evitar que se duplique un país con el mismo nombre
    for pais in lista_paises:
        if pais['nombre'].lower() == nombre.lower():
            return False # País ya en la lista
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    lista_paises.append(nuevo_pais)
    return True # Éxito en agregar

#Funcion para actualizar la poblacion y superficie
def actualizar_datos(lista_paises, nombre_buscado, nueva_pob, nueva_sup):
    for pais in lista_paises:
        if pais['nombre'].lower() == nombre_buscado.lower():
            pais['poblacion'] = nueva_pob
            pais['superficie'] = nueva_sup
            return True # Éxito en la actualización
    return False # País no encontrado

#Funcion para buscar un pais por el nombre
def buscar_por_nombre(lista_paises, nombre_buscar):
    nombre_buscar_min = nombre_buscar.lower()
    for pais in lista_paises:
        if nombre_buscar_min in pais['nombre'].lower():
            print(
                f"Nombre: {pais['nombre']} | "
                f"Población: {pais['poblacion']} | "
                f"Superficie: {pais['superficie']} | "
                f"Continente: {pais['continente']}"
            )
            return 
    print(f'{nombre_buscar} no se encontró')