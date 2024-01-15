from typing import List
from app.core.entities.vulnerability import Vulnerability
from app.core.interfaces.repository import VulnerabilityRepository
from app.infrastructure.persistence.database import db
from app.infrastructure.persistence.models import VulnerabilityModel

class FlaskVulnerabilityRepository(VulnerabilityRepository):
    def get_all(self) -> List[Vulnerability]:
        vulnerabilities = VulnerabilityModel.query.all()
        return [Vulnerability(title=v.title, description=v.description) for v in vulnerabilities]

    def save_all(self, vulnerabilities: List[Vulnerability]):
        for vulnerability in vulnerabilities:
            vulnerability_model = VulnerabilityModel(
                title=vulnerability.title,
                description=vulnerability.description
            )
            db.session.add(vulnerability_model)

        db.session.commit()


