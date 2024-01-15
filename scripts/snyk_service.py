import requests
import json
import os

def analizar_dependencias(api_key, ruta_proyecto):
    url = "https://snyk.io/api/v1/test"
    headers = {
        "Authorization": f"token {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "project": ruta_proyecto
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        resultado_analisis = response.json()

        ruta_resultados = os.path.join(os.getcwd(), 'resultados_analisis.json')
        with open(ruta_resultados, 'w') as file:
            json.dump(resultado_analisis, file)

        print(f'Resultados guardados en: {ruta_resultados}')
        return resultado_analisis
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


integration_id_snyk = os.environ.get("SNYK_INTEGRATION_ID")
clave_api_snyk = os.environ.get("SNYK_API_KEY")
ruta_proyecto = r"C:\Users\sebastian.aguirre\Desktop\Proyecto-Reto-DevSecOps"

resultado_analisis = analizar_dependencias(clave_api_snyk, ruta_proyecto)
print(resultado_analisis)