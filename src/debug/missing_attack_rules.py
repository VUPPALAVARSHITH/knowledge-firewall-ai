from pathlib import Path

from src.attacks.attack_engine import AttackEngine
from src.config.path_config import ENTERPRISE_DIR

engine = AttackEngine()

missing = []

for file in ENTERPRISE_DIR.rglob("*.txt"):

    text = file.read_text(encoding="utf-8")

    result = engine.apply_attack(text)

    if not result["success"]:

        print(file.stem)
        print("-"*50)

        start = text.find("4. POLICY STATEMENTS")
        end = text.find("5. RESPONSIBILITIES")

        print(text[start:end])
        print()

        missing.append(file.stem)

print("="*60)
print("Missing:", len(missing))