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