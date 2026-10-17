
import logging

from core.validator import validate_target
from models.target import Target
from recon.base import ReconModule
from recon.result import ReconResult

logger = logging.getLogger(__name__)


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
            target_identifier = (
                target.identifier if isinstance(target, Target) else "unknown"
            )
            return [
                ReconResult(
                    module="framework",
                    target=target_identifier,
                    success=False,
                    error="Target validation failed",
                )
        ]
        
    
        results = []

        for module in self.modules:
            logger.info(
                "Starting reconnaissance module: %s",
                module.name,
            )

            try:
                result = module.run(target)

                if not isinstance(result, ReconResult):
                    raise TypeError(
                        f"Recon module '{module.name}' returned an invalid result"
                    )
                result.target = target.identifier
                results.append(result)

                logger.info(
                    "Reconnaissance module completed: %s",
                    module.name,
                )

            except Exception as error:
                logger.error(
                    "Reconnaissance module failed: %s (%s)",
                    module.name,
                    type(error).__name__,
                )

                results.append(
                    ReconResult(
                        module=module.name,
                        target=target.identifier,
                        success=False,
                        error=str(error),
                    )
                )

        return results
