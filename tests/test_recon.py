from models.target import Target, TargetType
from recon.base import ReconModule 
from recon.result import ReconResult
from recon.framework import ReconFramework


class DummyRecoveryModule(ReconModule):
    @property
    def name(self) -> str:
        return "Dummy"
    def run(self, target: Target) -> ReconResult:
        return ReconResult(
            module=self.name,
            target=target.identifier,
            success=True,
            data={"info": "Dummy Reconnaissance executed successfully."},
        )

def test_module_registration():
    framework = ReconFramework()
    module = DummyRecoveryModule()

    framework.register(module)
    assert module in framework.modules

def test_module_execution():
    framework = ReconFramework()
    framework.register(DummyRecoveryModule())

    target = Target(
        identifier="example.com",
        target_type=TargetType.DOMAIN,
        scope=("example.com",),
    )

    results = framework.run(target)

    assert len(results) == 1
    assert results[0].success is True
    assert results[0].module == "Dummy"
    assert results[0].target == "example.com"
