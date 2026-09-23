from core.target import create_target
from core.validator import validate_target
from models.target import Target, TargetType


def main():
    # Valid target
    valid_target = create_target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",)
    )

    # Target that is outside the declared scope
    out_of_scope_target = Target(
        identifier="api.example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",)
    )

    # Target with no scope
    no_scope_target = Target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=()
    )

    print("Valid target:", validate_target(valid_target))
    print("Out of scope:", validate_target(out_of_scope_target))
    print("No scope:", validate_target(no_scope_target))


if __name__ == "__main__":
    main()