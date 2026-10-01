from models.target import Target
from recon.base import ReconModule
from recon.result import ReconResult

class ReconFramework:
    """
    Coordinates the execution of reconnaissance modules.
    """

    def __init__(self):
        self.modules: list[ReconModule] = []

    def register(self, module: ReconModule):
        """Register a reconnaissance module."""
        self.modules.append(module)

    def run(self, target: Target) -> list[ReconResult]:
        """Execute all registered reconnaissance modules."""
        results = []

        for module in self.modules:
            try:
                result = module.run(target)
                results.append(result)

            except Exception as error:
                results.append(
                    ReconResult(
                        module=module.name,
                        target=target.identifier,
                        success=False,
                        error=str(error),
                    )
                )

        return results
