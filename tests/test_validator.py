from core.target import create_target
from core.validator import validate_target
from models.target import Target, TargetType


def test_valid_target():
    target = create_target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",)
    )
    assert validate_target(target) is True


def test_empty_identifier():
    target = Target(
        identifier="",
        target_type=TargetType.DOMAIN,
        scope=("example.com",)
    )
    assert validate_target(target) is False


def test_unsupported_target_type():
    target = Target(
        identifier="example.com",
        target_type="banana",
        scope=("example.com",)
    )

    assert validate_target(target) is False


def test_empty_scope():
    target = Target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=()
    )

    assert validate_target(target) is False


def test_out_of_scope_target():
    target = Target(
        identifier="api.example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",)
    )

    assert validate_target(target) is False