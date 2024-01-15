import requests
from flask import Flask, jsonify, Blueprint
from app.adapters.flask_repository import FlaskVulnerabilityRepository
from app.core.use_cases.obtener_vulnerabilidades import ObtenerVulnerabilidades
from scripts.obtener_reportes_pipeline import obtener_reportes_desde_pipelines

bp = Blueprint('vulnerabilities', __name__)


@bp.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    repository = FlaskVulnerabilityRepository()
    vulnerabilities = []

    repo = 'sebastianyacup/RetoDevSecOps'
    artifact_url = f'https://api.github.com/repos/{repo}/actions/artifacts'
    headers = {'Authorization': 'Bearer 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'}

    response = requests.get(artifact_url, headers=headers)
    artifacts = response.json()['artifacts']

    if artifacts:
        artifact_id = artifacts[0]['id']
        download_url = f'https://api.github.com/repos/{repo}/actions/artifacts/{artifact_id}/zip'
        response = requests.get(download_url, headers=headers)

        report_path = f'/path/to/report/resultados-analisis-synk.json'
        with open(report_path, 'wb') as file:
            file.write(response.content)

        reportes = obtener_reportes_desde_pipelines(report_path)
        obtener_vulnerabilidades = ObtenerVulnerabilidades(repository)
        vulnerabilities.extend(obtener_vulnerabilidades.execute(reportes))

    return jsonify([vars(v) for v in vulnerabilities])


def configure_routes(app: Flask, obtener_reportes_desde_pipelines):
    app.register_blueprint(bp)
