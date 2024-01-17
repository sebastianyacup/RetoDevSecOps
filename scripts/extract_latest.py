import requests

def get_latest_json_url(repo):
    url = f'https://api.github.com/repos/{repo}/releases/latest'
    headers = {'Accept': 'application/vnd.github.v3+json'}

    try:
        response = requests.get(url, headers=headers, verify=False)

        response.raise_for_status()

        download_url = response.json()['assets'][0]['browser_download_url']

        return download_url
    except requests.exceptions.RequestException as e:
        print(f'Error al obtener la URL del archivo JSON: {e}')

    return None