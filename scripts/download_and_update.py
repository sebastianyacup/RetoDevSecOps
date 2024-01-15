import os
import zipfile
import requests
import tempfile
import requests


def get_latest_run_id(repo, workflow_name, access_token):
    url = f'https://api.github.com/repos/{repo}/actions/workflows/{workflow_name}/runs'
    print(url + "Soy url");
    headers = {'Authorization': f'token {access_token}'}

    try:
        # Desactivar la verificación SSL
        response = requests.get(url, headers=headers, verify=False)

        if response.status_code == 200:
            data = response.json()
            if data['workflow_runs']:
                return str(data['workflow_runs'][0]['id'])
    except requests.RequestException as e:
        print(f'Error al obtener el último run_id: {e}')

    # Si no se pudo obtener el run_id, devuelve un valor conocido
    return '7525592605'


def download_and_update(repo, workflow_name):
    run_id = get_latest_run_id(repo, workflow_name, access_token="")

    if run_id:
        headers = {'Accept': 'application/vnd.github.v3+json'}
        api_url = f'https://github.com/{repo}/Docs'

        try:
            # Hacer una solicitud a la API de GitHub para descargar el archivo ZIP
            response = requests.get(api_url, headers=headers, stream=True)

            # Asegurarse de que la solicitud fue exitosa
            response.raise_for_status()

            # Crear un archivo temporal para guardar el contenido descargado
            with open("1169124285.zip", 'wb') as temp_file:
                for chunk in response.iter_content(chunk_size=128):
                    temp_file.write(chunk)

            print(f'Archivo ZIP descargado en: 1169124285.zip')
            return "1169124285.zip"
        except requests.exceptions.RequestException as e:
            print(f'Error al descargar el archivo ZIP: {e}')

    print('No se pudo obtener el run_id.')
    return None