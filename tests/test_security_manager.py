from src.enterprise.security_manager import SecurityManager

manager = SecurityManager()

result = manager.verify_query(
    "Does VPN require authentication?"
)

print(result.statistics)

print("\nVerification Reports\n")

for report in result.verification_reports:
    print(report)