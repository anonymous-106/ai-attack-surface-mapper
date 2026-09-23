from dataclasses import dataclass
from enum import Enum


class TargetType(Enum):
    DOMAIN = "domain"
    IP = "ip"
    URL = "url"


@dataclass(frozen=True)
class Target:
    identifier: str
    target_type: str  # e.g., "DOMAIN", "IP_ADDRESS", "URL"
    scope: tuple[str, ...]  # List of allowed scopes for the target