from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

ENTERPRISE_DIR = DATA_DIR / "enterprise"

GENERATED_DIR = DATA_DIR / "generated"

POISONED_DIR = GENERATED_DIR / "poisoned"

REPOISONED_DIR = GENERATED_DIR / "repoisoned"

PROMPT_DIR = GENERATED_DIR / "prompt_injection"

SENSITIVE_DIR = GENERATED_DIR / "sensitive_data"

FORGOTTEN_REPOSITORY = DATA_DIR / "forgotten_repository"

METADATA_DIR = DATA_DIR / "metadata"

EVALUATION_DIR = DATA_DIR / "evaluation"