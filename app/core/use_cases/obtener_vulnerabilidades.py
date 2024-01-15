from typing import List
from app.core.entities.vulnerability import Vulnerability

class ObtenerVulnerabilidades:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, reportes: List[dict]) -> List[Vulnerability]:
        # Lógica para procesar los reportes y extraer vulnerabilidades
        return self.procesar_reportes(reportes)

    def procesar_reportes(self, reportes: List[dict]) -> List[Vulnerability]:
        vulnerabilidades = []
        for reporte in reportes:
            # Lógica específica para extraer vulnerabilidades del reporte
            # (Adapta según el formato de tus reportes)
            vulnerabilidades.append(Vulnerability(title=reporte["title"], description=reporte["description"]))

        return vulnerabilidades
