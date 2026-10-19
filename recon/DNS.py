import logging
import dns.exception
import dns.resolver
from models.target import Target, TargetType
from recon.base import ReconModule
from recon.result import ReconResult

logger = logging.getLogger(__name__)


class DNSReconModule(ReconModule):
    """Collect DNS records for a validated domain target."""

    RECORD_TYPES = ("A", "AAAA", "CNAME", "MX", "NS", "TXT")

    def __init__(self, resolver=None):
        self.resolver = resolver or dns.resolver.Resolver()
        self.resolver.timeout = 2.0
        self.resolver.lifetime = 5.0

    @property
    def name(self) -> str:
        return "dns"

    def run(self, target: Target) -> ReconResult:
        if not isinstance(target, Target):
            return ReconResult(
                module=self.name,
                target="unknown",
                success=False,
                error="Invalid target object",
            )

        if target.target_type != TargetType.DOMAIN:
            return ReconResult(
                module=self.name,
                target=target.identifier,
                success=False,
                error="DNS reconnaissance requires a domain target",
            )

        if not target.identifier or target.identifier not in target.scope:
            return ReconResult(
                module=self.name,
                target=target.identifier or "unknown",
                success=False,
                error="Target is outside the declared scope",
            )

        records = {}
        failures = {}

        for record_type in self.RECORD_TYPES:
            try:
                answers = self.resolver.resolve(
                    target.identifier,
                    record_type,
                    raise_on_no_answer=False,
                )

                records[record_type] = (
                    [answer.to_text() for answer in answers]
                    if answers.rrset is not None
                    else []
                )

            except dns.resolver.NXDOMAIN:
                logger.info("DNS name does not exist")
                failures[record_type] = "Name does not exist"
                break

            except dns.resolver.NoNameservers:
                logger.warning("DNS query failed: no nameservers available")
                failures[record_type] = "No nameservers available"

            except (dns.resolver.NoAnswer, dns.exception.Timeout):
                logger.info("DNS query returned no answer or timed out")
                failures[record_type] = "No answer or timeout"

            except dns.exception.DNSException as error:
                logger.warning(
                    "DNS query failed for record type %s: %s",
                    record_type,
                    type(error).__name__,
                )
                failures[record_type] = "DNS query failed"

        return ReconResult(
            module=self.name,
            target=target.identifier,
            success=bool(records) and any(records.values()),
            data={
                "records": records,
                "failures": failures,
            },
        )