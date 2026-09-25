import logging
from models.target import Target, TargetType

logger = logging.getLogger(__name__)

def normalize_target(identifier: str) -> str:
    logger.debug("Normalizing target identifier")
    return identifier.strip()                       


def create_target(
    identifier: str,
    target_type: TargetType,
    scope: tuple[str, ...]
) -> Target:
    logger.debug("Creating target object")
    try:
        normalized_identifier = normalize_target(identifier)

        return Target(
            identifier=normalized_identifier,
            target_type=target_type,
            scope=scope
        )

    except Exception:
        logger.error("Failed to create target object", exc_info=True)
        raise