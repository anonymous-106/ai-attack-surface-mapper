from models.asset import Asset
from recon.result import ReconResult


def dns_result_to_assets(result: ReconResult) -> list[Asset]:
    """Convert DNS reconnaissance results into asset objects."""

    if result.module != "dns" or not result.success:
        return []

    records = result.data.get("records", {})
    assets = []

    for ip in records.get("A", []):
        assets.append(
            Asset(
                identifier=ip,
                asset_type="ip",
                source="dns",
                attributes={"record_type": "A"},
            )
        )

    for ip in records.get("AAAA", []):
        assets.append(
            Asset(
                identifier=ip,
                asset_type="ip",
                source="dns",
                attributes={"record_type": "AAAA"},
            )
        )

    return assets