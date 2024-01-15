from typing import List
from app.core.entities.vulnerability import Vulnerability
from app.infrastructure.persistence.database import db


class VulnerabilityModel(db.Model):
    __tablename__ = 'vulnerabilities'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    @staticmethod
    def get_all() -> List[Vulnerability]:
        return VulnerabilityModel.query.all()

    @staticmethod
    def save_all(vulnerabilities: List[Vulnerability]):
        for vulnerability in vulnerabilities:
            vulnerability_model = VulnerabilityModel(
                title=vulnerability.title,
                description=vulnerability.description
            )
            db.session.add(vulnerability_model)

        db.session.commit()
