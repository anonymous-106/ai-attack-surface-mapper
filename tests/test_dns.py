import dns.resolver
from unittest.mock import Mock, MagicMock
from models.target import Target, TargetType
from recon.dns import DNSReconModule


def test_dns_module_has_correct_name():
    module = DNSReconModule(resolver=Mock())

    assert module.name == "dns"

def test_dns_module_collects_a_record():
    resolver = MagicMock()
    answer = Mock()
    answer.to_text.return_value = "192.0.2.10"

    response = MagicMock()
    response.rrset = object()
    response.__iter__.return_value = iter([answer])

    empty_response = MagicMock()
    empty_response.rrset = None


    def fake_resolve(name, record_type, raise_on_no_answer = False):
        if record_type == "A":
            return response
        return empty_response      

    resolver.resolve.side_effect = fake_resolve

    module = DNSReconModule(resolver=resolver)

    taregt = Target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",)
    )

    result = module.run(taregt)

    assert result.success is True
    assert result.data["records"]["A"] == ["192.0.2.10"]
    assert result.module  == "dns"
    assert result.target == "example.com"

def test_dns_module_handles_timeout():
    import dns.exception

    resolver = MagicMock()
    resolver.resolve.side_effect = dns.exception.Timeout

    module = DNSReconModule(resolver=resolver)

    target = Target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",),
    )

    result = module.run(target)

    assert result.success is False
    assert result.data["failures"]["A"] == "No answer or timeout"

def test_dns_module_handles_nonexistent_domain():
    import dns.resolver

    resolver = MagicMock()
    resolver.resolve.side_effect = dns.resolver.NXDOMAIN

    module = DNSReconModule(resolver = resolver)

    target = Target(
        identifier="example.com",
        target_type = TargetType.DOMAIN,
        scope = ("example.com",),
    )

    result = module.run(target)

    assert result.success is False
    assert result.data["failures"]["A"] == "Name does not exist"


def test_dns_module_handles_no_nameservers():
    import dns.resolver

    resolver = MagicMock()
    resolver.resolve.side_effect = dns.resolver.NoNameservers

    module = DNSReconModule(resolver=resolver)

    target = Target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",),
    )

    result = module.run(target)

    assert result.success is False
    assert result.data["failures"]["A"] == "No nameservers available"