from flask import Flask, request, Blueprint, jsonify
from app.adapters.flask_repository import FlaskVulnerabilityRepository
from app.core.use_cases.obtener_vulnerabilidades import ObtenerVulnerabilidades
from scripts.download_and_update import download_and_update
from scripts.extract_latest_json import extract_latest_json

bp = Blueprint('vulnerabilities', __name__)

REPO_NAME = 'sebastianyacup/RetoDevSecOps'
WORKFLOW_NAME = 'analisis-dependencias.yml'
GITHUB_ACCESS_TOKEN = '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'


@bp.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    repository = FlaskVulnerabilityRepository()
    vulnerabilities = []

    extract_path = download_and_update(REPO_NAME, WORKFLOW_NAME, GITHUB_ACCESS_TOKEN)

    if extract_path:
        reportes = extract_latest_json(extract_path)

        if reportes:
            obtener_vulnerabilidades = ObtenerVulnerabilidades(repository)
            vulnerabilities.extend(obtener_vulnerabilidades.execute(reportes))

    return jsonify([vars(v) for v in vulnerabilities])


@bp.route('/webhook-endpoint', methods=['POST'])
def webhook_handler():
    payload = request.json
    ref = payload.get('ref')
    head_commit = payload.get('head_commit')

    if ref == 'refs/heads/main' and head_commit:
        files_changed = head_commit.get('added') + head_commit.get('modified') + head_commit.get('removed')

        # Verifica si hay cambios en el análisis de dependencias
        if WORKFLOW_NAME in files_changed:
            # Realiza la lógica para actualizar el informe y obtener el último JSON automáticamente
            extract_path = download_and_update(REPO_NAME, WORKFLOW_NAME, GITHUB_ACCESS_TOKEN)
            reportes = extract_latest_json(extract_path)

            if reportes:
                repository = FlaskVulnerabilityRepository()
                obtener_vulnerabilidades = ObtenerVulnerabilidades(repository)
                vulnerabilities = obtener_vulnerabilidades.execute(reportes)
                return jsonify([vars(v) for v in vulnerabilities])

    return jsonify({'status': 'success'})
