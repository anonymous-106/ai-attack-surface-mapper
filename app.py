import argparse
from config import Config
from core.target import create_target
from core.validator import validate_target
from models.target import TargetType


def main():
    parser = argparse.ArgumentParser( prog="AI Attack Surface Mapper", description="AI Attack Surface Mapper - Attack surface discovery and mapping tool.")
    parser.add_argument("--target", required=True, help = "Target to assess")
    args = parser.parse_args()

    target = create_target(
        identifier=args.target,
        target_type=TargetType.DOMAIN,
        scope=(args.target,)
    )

    if validate_target(target):
        print("Target accepted:", target.identifier)
    else:
        print("Target rejected.")


if __name__ == "__main__":
    main()