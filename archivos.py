import csv
#Carga del archivo
def cargar_paises_csv(nombre_archivo):
    lista_paises = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Verificamos que ninguno de los campos requeridos esté vacío
                if not fila['nombre'] or not fila['poblacion'] or \
                not fila['superficie'] or not fila['continente']:
                    print(f"Advertencia: Se saltó un registro con campos vacíos.")
                    continue 
                # Creamos diccionarios dentro de la lista_paises
                pais = {
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente']
                }
                lista_paises.append(pais)
        print(f"Éxito: Se cargaron {len(lista_paises)} países correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
    except ValueError:
        print("Error: El archivo contiene datos numéricos con formato inválido.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return lista_paises

#Funcion para guardar cambio en el archivo
def guardar_paises_csv(nombre_archivo, lista_paises):
    try:
        campos = ['nombre', 'poblacion', 'superficie', 'continente']
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(lista_paises)
            
        print("Datos guardados exitosamente en el archivo CSV.")
        return True
    except Exception as e:
        print(f"Error al intentar guardar los datos: {e}")
        return False