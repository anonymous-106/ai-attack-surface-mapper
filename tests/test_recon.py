from models.target import Target, TargetType
from recon.base import ReconModule 
from recon.result import ReconResult
from recon.framework import ReconFramework


class DummyReconModule(ReconModule):
    @property
    def name(self) -> str:
        return "dummy"
    def run(self, target: Target) -> ReconResult:
        return ReconResult(
            module=self.name,
            target=target.identifier,
            success=True,
            data={"info": "Dummy Reconnaissance executed successfully."},
        )

class FailingReconModule(ReconModule):
    @property
    def name(self) -> str:
        return "failing"
    def run(self, target: Target) -> ReconResult:
        raise RuntimeError("Simulated Reconnaissance Failure.")

def test_module_registration():
    framework = ReconFramework()
    module = DummyReconModule()

    framework.register(module)
    assert module in framework.modules

def test_module_execution():
    framework = ReconFramework()
    framework.register(DummyReconModule())

    target = Target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",),
    )

    results = framework.run(target)

    assert len(results) == 1
    assert results[0].success is True
    assert results[0].module == "dummy"
    assert results[0].target == "example.com"

def test_module_failure_isolated():
    framework = ReconFramework()
    framework.register(FailingReconModule())
    framework.register(DummyReconModule())

    target = Target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",),
    )

    results = framework.run(target)

    assert len(results) == 2

    assert results[0].success is False
    assert results[0].module == "failing"

    assert results[1].success is True
    assert results[1].module == "dummy"
def test_invalid_target_is_rejected():
    framework = ReconFramework()
    framework.register(DummyReconModule())

    target = Target(
        identifier="outside.example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",),
    )

    results = framework.run(target)

    assert len(results) == 1
    assert results[0].success is False
    assert results[0].module == "framework"
    assert results[0].error == "Target validation failed"