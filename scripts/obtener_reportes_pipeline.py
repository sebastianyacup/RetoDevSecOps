import json
import os

def obtener_reportes_desde_pipelines():
    ruta_resultados = os.path.join(os.getcwd(), 'resultados_analisis.json')

    try:
        with open(ruta_resultados, 'r') as file:
            reportes = json.load(file)
        return reportes
    except FileNotFoundError:
        print(f'Archivo de resultados no encontrado en: {ruta_resultados}')
        return []
    except json.JSONDecodeError:
        print(f'Error al cargar JSON desde: {ruta_resultados}')
        return []
