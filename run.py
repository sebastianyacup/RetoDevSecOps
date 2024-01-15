from app import app
from app.adapters.flask_repository import FlaskVulnerabilityRepository
from app.core.use_cases.obtener_vulnerabilidades import ObtenerVulnerabilidades
from scripts.download_and_update import download_and_update
from scripts.extract_latest_json import extract_latest_json
from app.adapters.flask_routes import bp

def run_analysis():
    REPO_NAME = 'sebastianyacup/RetoDevSecOps'
    WORKFLOW_NAME = 'analisis-dependencias.yml'
    GITHUB_ACCESS_TOKEN = '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'

    extract_path = download_and_update(REPO_NAME, WORKFLOW_NAME)

    if extract_path:
        reportes = extract_latest_json(extract_path)

        repository = FlaskVulnerabilityRepository()
        obtener_vulnerabilidades_instance = ObtenerVulnerabilidades(repository=repository)

        obtener_vulnerabilidades_instance.execute(reportes)

        app.register_blueprint(bp)

        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run_analysis()
