
import logging

from models.target import Target, TargetType

logger = logging.getLogger(__name__)


def validate_target(target: Target) -> bool:
    """Validate a target object and its declared scope."""

    if not isinstance(target, Target):
        logger.warning("Target rejected: invalid target object")
        return False

    if not target.identifier:
        logger.warning("Target rejected: empty identifier")
        return False

    if not isinstance(target.target_type, TargetType):
        logger.warning("Target rejected: unsupported target type")
        return False

    if not target.scope:
        logger.warning("Target rejected: empty scope")
        return False

    if target.identifier not in target.scope:
        logger.warning("Target rejected: target is outside declared scope")
        return False

    logger.info("Target validation successful")
    return True
