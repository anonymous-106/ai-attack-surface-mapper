from models.target import Target, TargetType

def normalize_target(identifier: str) -> str:
    return identifier.strip()                       


def create_target(
    identifier: str,
    target_type: TargetType,
    scope: tuple[str, ...]
) -> Target:
    normalized_identifier = normalize_target(identifier)

    return Target(
        identifier=normalized_identifier,
        target_type=target_type,
        scope=scope
    )