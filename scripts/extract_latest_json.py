import glob
import os
import json


def extract_latest_json(extract_path):
    result_files = glob.glob(os.path.join(extract_path, 'resultados_analisis_snyk_*.json'))

    result_files.sort(key=os.path.getmtime, reverse=True)

    if result_files:
        latest_result_file = result_files[0]

        try:
            with open(latest_result_file, 'r') as file:
                reportes = json.load(file)
                return reportes
        except FileNotFoundError:
            print(f'Archivo de resultados no encontrado: {latest_result_file}')
        except json.JSONDecodeError:
            print(f'Error al cargar JSON desde: {latest_result_file}')

    return None
