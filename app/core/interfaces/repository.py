from abc import ABC, abstractmethod
from typing import List
from app.core.entities.vulnerability import Vulnerability

class VulnerabilityRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Vulnerability]:
        pass

    @abstractmethod
    def save_all(self, vulnerabilities: List[Vulnerability]):
        pass
