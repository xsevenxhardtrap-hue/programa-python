# Fase 5 - Evaluación Final POA - Problema 1: Nivel de compromiso de sesiones

# Matriz: [ID del cliente, Duración (segundos), Número de clics]
sesiones = [
    [101, 250, 12],   # duración > 180 y clics > 8
    [102, 45, 10],    # duración < 60
    [103, 120, 5],    # ni alto ni bajo
    [104, 300, 2],    # clics < 3
    [105, 181, 9],    # justo por encima de los límites
    [106, 60, 3],     # justo en el límite inferior
]


def clasificar_compromiso(duracion, clics):
    """Devuelve 'Alto', 'Bajo' o 'Medio' según duración y clics."""
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


def mostrar_informe(matriz):
    print("=" * 38)
    print("   INFORME DE COMPROMISO POR SESIÓN")
    print("=" * 38)
    print(f"{'ID Cliente':<15}{'Compromiso':<15}")
    print("-" * 38)
    for fila in matriz:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]
        nivel = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<15}{nivel:<15}")
    print("=" * 38)


mostrar_informe(sesiones)