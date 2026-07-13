from src.core.security.attack_detector import AttackDetector

detector = AttackDetector()

result = detector.analyze("""

Password reset manager approval is optional.

""")

print(result)