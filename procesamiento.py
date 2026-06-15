#Filtrar países por continente

def filtrar_por_continente(lista_paises, continente):

    continente = continente.strip().lower()
    continente = continente.replace("á", "a")
    continente = continente.replace("é", "e")
    continente = continente.replace("í", "i")
    continente = continente.replace("ó", "o")
    continente = continente.replace("ú", "u")

    resultados = []

    for pais in lista_paises:

        continente_pais = pais["continente"].strip().lower()

        continente_pais = continente_pais.replace("á", "a")
        continente_pais = continente_pais.replace("é", "e")
        continente_pais = continente_pais.replace("í", "i")
        continente_pais = continente_pais.replace("ó", "o")
        continente_pais = continente_pais.replace("ú", "u")

        if continente_pais == continente:
            resultados.append(pais)

    return resultados

#Filtrar por rango de población

def filtrar_por_poblacion(lista_paises, minimo, maximo):
    resultados = []

    for pais in lista_paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    return resultados

#Filtrar por rango de superficie

def filtrar_por_superficie(lista_paises, minimo, maximo):
    resultados = []

    for pais in lista_paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    return resultados

#Ordenar por nombre

def ordenar_por_nombre(lista_paises):
    return sorted(
        lista_paises,
        key=lambda pais: pais["nombre"]
    )

#Ordenar por población

def ordenar_por_poblacion(lista_paises):
    return sorted(
        lista_paises,
        key=lambda pais: pais["poblacion"]
    )

#Ordenar por superficie

#Ascendete
def ordenar_superficie_asc(lista_paises):
    return sorted(
        lista_paises,
        key=lambda pais: pais["superficie"]
    )
#Descendente
def ordenar_superficie_desc(lista_paises):
    return sorted(
        lista_paises,
        key=lambda pais: pais["superficie"],
        reverse=True
    )

#Mostrar países
def mostrar_paises(lista_paises):
    for pais in lista_paises:
        print(
            f"{pais['nombre']} | "
            f"Población: {pais['poblacion']} | "
            f"Superficie: {pais['superficie']} km² | "
            f"Continente: {pais['continente'].strip()}"
        )
