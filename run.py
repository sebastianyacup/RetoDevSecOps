from app.adapters.flask_routes import configure_routes
from app import app
from app.core.use_cases.obtener_vulnerabilidades import ObtenerVulnerabilidades
from app.adapters.flask_repository import FlaskVulnerabilityRepository
from scripts.obtener_reportes_pipeline import obtener_reportes_desde_pipelines

reportes = obtener_reportes_desde_pipelines()

obtener_vulnerabilidades_instance = ObtenerVulnerabilidades(repository=FlaskVulnerabilityRepository())
obtener_vulnerabilidades_instance.execute(reportes)
configure_routes(app, obtener_vulnerabilidades_instance)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
