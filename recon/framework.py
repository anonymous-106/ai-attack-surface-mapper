from models.target import Target
from recon.base import ReconModule
from recon.result import ReconResult
from core.validator import validate_target


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

        if not validate_target(target):
            return [
                ReconResult(
                    module="framework",
                    target=target.identifier,
                    success=False,
                    error="Target validation failed",
                )
            ]

        results = []

        for module in self.modules:
            try:
                result = module.run(target)
                if not isinstance(result, ReconResult):
                    raise TypeError(
                        f"Recon module '{module.name}' returned an invalid result"
                    )
                result.target = target.identifier
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
