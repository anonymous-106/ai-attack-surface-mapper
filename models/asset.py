from dataclasses import dataclass, field


@dataclass
class Asset:
    identifier: str
    asset_type: str
    source: str
    attributes: dict = field(default_factory=dict)