#Validacione de nombre
def validar_nombre(msg):
    while True:
        try:
            nombre = input(msg).strip().title()
            if nombre and nombre.isalpha():
                return nombre
            raise ValueError(f"Este campo no puede contener números ni quedar vacío")
        except ValueError as e:
            print(f'Error: {e}')

#Validacione de cantidad
def validar_entero(msg):
    while True:
        try:
            cantidad=int(input(msg))
            if cantidad <0:
                raise ValueError("la cantidad a cargar debe ser mayor a cero")
            return cantidad
        except ValueError as e:
            print(f"Error: {e}")