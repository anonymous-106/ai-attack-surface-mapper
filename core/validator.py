from models.target import Target, TargetType

def validate_target(target: Target) -> bool:
    if not target.identifier:
        return False
    
    if not isinstance(target.target_type, TargetType):
        return False

    if not target.scope:
        return False

    if target.identifier not in target.scope:
        return False
    
    return True
