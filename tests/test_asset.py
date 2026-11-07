from models.asset import Asset

def test_asset_creation():
    asset = Asset(
        identifier="example.com",
        asset_type="domain",
        source="dns",
    )
    assert asset.identifier == "example.com"
    assert asset.asset_type == "domain"
    assert asset.source == "dns"
    assert asset.attributes == {}

def test_assets_have_independent_attributes():
    asset_one = Asset(
        identifier="example.com",
        asset_type="domain",
        source="dns",
    )

    asset_two = Asset(
        identifier="192.0.2.10",
        asset_type="ip",
        source="dns",
    )

    asset_one.attributes["record"] = "A"

    assert asset_one.attributes == {"record": "A"}
    assert asset_two.attributes == {}