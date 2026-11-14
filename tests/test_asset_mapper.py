from recon.asset_mapper import dns_result_to_assets
from recon.result import ReconResult

def test_dns_result_to_assets_with_valid_dns_result():
    result = ReconResult(
        module="dns",
        target="example.com",
        success=True,
        data={
            "records": {
                "A": ["192.0.2.10"],
                "AAAA": ["2001:db8::10"],
            },
            "failures": {},
        },
    )
    assets = dns_result_to_assets(result)

    assert len(assets) == 2

    assert assets[0].identifier == "192.0.2.10"
    assert assets[0].asset_type == "ip"
    assert assets[0].source == "dns"
    assert assets[0].attributes == {"record_type": "A"}

    assert assets[1].identifier == "2001:db8::10"
    assert assets[1].asset_type == "ip"
    assert assets[1].source == "dns"
    assert assets[1].attributes == {"record_type": "AAAA"}

def test_dns_result_returns_empty_list_when_recon_failed():
    result = ReconResult(
        module="dns",
        target="example.com",
        success=False,
        data={
            "records": {"A": ["192.0.2.10"]},
            "failures": {},
        },
    )

    assert dns_result_to_assets(result) == []

def test_non_dns_result_returns_empty_list():
    result = ReconResult(
        module = "http",
        target = "example.com",
        success = True,
        data = {
            "records": {"A": ["192.0.2.10"]},
            "failures": {},
        },
    )

    assert dns_result_to_assets(result) == []
    
    