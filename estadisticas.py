
#Pais con mayor y menor poblacion
def extremos(lista_paises):
    mayor=0
    menor=float('inf')
    for poblacion in lista_paises:
        if poblacion['poblacion'] > mayor:
            mayor=poblacion['poblacion']
            pais_mayor=poblacion['nombre']
        if poblacion['poblacion'] < menor:
            menor=poblacion['poblacion']
            pais_menor=poblacion['nombre']
    print(f'El país con mayor población es {pais_mayor} con {mayor} habitantes\nEl país con menor población es {pais_menor} con {menor} habitantes\n')

#Promedio de poblacion
def prom_pob(lista_paises):
    suma=0
    for poblacion in lista_paises:
        suma+=poblacion['poblacion']
    prom=suma/len(lista_paises)
    print(f'El promedio de las poblaciones es: {prom}\n')

#Promedio de superficie
def prom_sup(lista_paises):
    suma=0
    for superficie in lista_paises:
        suma+=superficie['superficie']
    prom=suma/len(lista_paises)
    print(f'El promedio de las superficies es: {prom}\n')

#Cantidad de paises por continente
def cant_paises(lista_paises):
    am=0
    eu=0
    asi=0
    af=0
    oc=0
    for pais in lista_paises:
        if pais['continente']=='America':
            am+=1
        elif pais['continente']=='Europa':
            eu+=1
        elif pais['continente']=='Asia':
            asi+=1
        elif pais['continente']=='Africa':
            af+=1
        elif pais['continente']=='Oceania':
            oc+=1
    print(
        'Cantidad de países en America: ',am,'\n'
        'Cantidad de países en Europa: ',eu,'\n'
        'Cantidad de países en Asia: ',asi,'\n'
        'Cantidad de países en Africa: ',af,'\n'
        'Cantidad de países en Oceania: ',oc,'\n'
        )