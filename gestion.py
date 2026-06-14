def agregar_pais(lista_paises,nombre,poblacion,superficie,continente):
    # Validación: Evitar que se duplique un país con el mismo nombre
    for pais in lista_paises:
        if pais['nombre'].lower() == nombre.lower():
            return False # País ya en la lista
    pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    lista_paises.append(pais)
    return True# Éxito en la actualización

def actualizar_datos_pais(lista_paises, nombre_buscado, nueva_pob, nueva_sup):
    for pais in lista_paises:
        if pais['nombre'].lower() == nombre_buscado.lower().strip():
            pais['poblacion'] = nueva_pob
            pais['superficie'] = nueva_sup
            return True # Éxito en la actualización
    return False # País no encontrado

def buscar_por_nombre(lista_paises, nombre_buscado):
    coincidencias = []
    nombre_buscado_min = nombre_buscado.lower()
    
    for pais in lista_paises:
        if nombre_buscado_min in pais['nombre'].lower():
            coincidencias.append(pais)        
    return coincidencias   