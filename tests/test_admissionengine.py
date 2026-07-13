from src.core.security.admission_trust_engine import AdmissionTrustEngine

engine = AdmissionTrustEngine()

result = engine.compute(

    repository_similarity=0.10,

    attack_confidence=0.00,

    sensitive_risk=0.00

)

print(result)