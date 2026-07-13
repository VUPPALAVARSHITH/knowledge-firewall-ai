from src.core.security.sensitive_detector import SensitiveDetector

detector = SensitiveDetector()

result = detector.analyze("""

API KEY

AKIAIOSFODNN7EXAMPLE

Admin Email

security@company.com

VPN

https://vpn.company.com

""")

print(result)