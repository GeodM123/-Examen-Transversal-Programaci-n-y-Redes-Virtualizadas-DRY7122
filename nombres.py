integrantes = [
    {"nombre": "Francisca", "apellido": "Meza", "profesion": "Ing Redes"},
    {"nombre": "Roberto", "apellido": "Mena"}
]

letras = ["a", "b"]

def imprimir_nombres_apellidos(integrantes):
    for alumno in integrantes:
        print(f"Nombre: {alumno['nombre']}, Apellido: {alumno['apellido']}")

if __name__ == "__main__":
    imprimir_nombres_apellidos(integrantes)