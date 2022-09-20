from utils import promedio_est, get_aprobados, escribir_reporte, leer_reporte

notas = [
    {"mat": 90,"fis": 70,"qmc": 60,"cal": 75},
    {"mat": 80,"fis": 20,"qmc": 20,"cal": 20},
    {"mat": 90,"fis": 90,"qmc": 50,"cal": 55},
    {"mat": 70,"fis": 80,"qmc": 90,"cal": 100},
]

nombres = ["juan perez", "sara rivera", "ana montero", "raul soza"]

print(promedio_est(notas[0]))

aprobados = get_aprobados(nombres, notas)

print(aprobados)

escribir_reporte(aprobados, "aprobados.csv")

leer_reporte("aprobados.csv")