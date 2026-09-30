from abc import ABC, abstractmethod
from models.target import Target

class ReconModule(ABC):
    """
    Base interface for all reconnaissance modules.
    """
    @property
    @abstractmethod
    def name(self) -> str:
        """
        Returns the name of the reconnaissance module.
        """
        pass

    @abstractmethod
    def run(self, target: Target):
        """Execute reconnaissance against the validated target."""
        pass