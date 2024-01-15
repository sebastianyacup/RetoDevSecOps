from flask import Flask, jsonify, Blueprint
from app.adapters.flask_repository import FlaskVulnerabilityRepository
from app.core.use_cases.obtener_vulnerabilidades import ObtenerVulnerabilidades
from scripts.obtener_reportes_pipeline import obtener_reportes_desde_pipelines

bp = Blueprint('vulnerabilities', __name__)


@bp.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    repository = FlaskVulnerabilityRepository()

    # Obtén los reportes desde donde sea necesario (en este ejemplo, desde la función obtener_reportes_desde_pipelines)
    reportes = obtener_reportes_desde_pipelines()

    # Crea una instancia de ObtenerVulnerabilidades con el repository y ejecuta el método execute con los reportes
    obtener_vulnerabilidades = ObtenerVulnerabilidades(repository)
    vulnerabilities = obtener_vulnerabilidades.execute(reportes)

    return jsonify([vars(v) for v in vulnerabilities])


def configure_routes(app: Flask, obtener_reportes_desde_pipelines):
    app.register_blueprint(bp)
