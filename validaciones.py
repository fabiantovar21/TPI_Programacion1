#Validaciones de nombre
def validar_nombre(msg):
    while True:
        nombre = input(msg).strip().title()
        # Reemplazamos espacios para validar que sean solo letras
        if nombre and nombre.replace(" ", "").isalpha():
            return nombre
        print("Error: Este campo no puede contener números, símbolos ni quedar vacío.")

#Validaciones de cantidad
def validar_entero(msg):
    while True:
        try:
            cantidad=int(input(msg))
            if cantidad <0:
                raise ValueError("la cantidad a cargar debe ser mayor a cero")
            return cantidad
        except ValueError as e:
            print(f"Error: {e}")
