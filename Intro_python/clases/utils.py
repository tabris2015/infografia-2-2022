def promedio_est(estudiante: dict) -> float:
    acum = 0
    for materia, nota in estudiante.items():
        acum += nota
    
    return acum / len(estudiante)

def promedio_general(estudiantes: list) -> float:
    return sum([promedio_est(est) for est in estudiantes]) / len(estudiantes)


def get_aprobados(nombres, notas):
    aprobados = {}
    for nombre, notas_est in zip(nombres, notas):
        promedio = promedio_est(notas_est)
        if promedio > 60:
            aprobados[nombre] = promedio
    
    return aprobados

def escribir_reporte(lista_estudiantes, nombre_archivo):
    with open(nombre_archivo, "r+") as f:
        for nombre, prom in lista_estudiantes.items():
            f.write(f"{nombre}, {prom}\n")

    print(f"Reporte guardado en el archivo: {nombre_archivo}")

def leer_reporte(nombre_archivo):
    datos = {}
    with open(nombre_archivo, "r") as f:
        for linea in f:
            nombre, nota_str = linea.split(",")[:2]
            datos[nombre] = float(nota_str)