from pathlib import Path
import json
import random
import shutil
import re
from src.config.path_config import ENTERPRISE_DIR
from src.research.attacks.attack_templates import ATTACK_TEMPLATES

BENCHMARK_DIR = Path("src/evaluation/benchmark")


CLEAN_DIR = BENCHMARK_DIR / "clean"
DUP_DIR = BENCHMARK_DIR / "duplicates"
NEAR_DIR = BENCHMARK_DIR / "near_duplicates"
POISON_DIR = BENCHMARK_DIR / "poisoned"
SENSITIVE_DIR = BENCHMARK_DIR / "sensitive"
COMBINED_DIR = BENCHMARK_DIR / "combined"
NEAR_DIR.mkdir(parents=True, exist_ok=True)
POISON_DIR.mkdir(parents=True,exist_ok=True)
SENSITIVE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


class BenchmarkBuilder:

    CLEAN_COUNT = 40

    DUPLICATE_COUNT = 40

    NEAR_DUPLICATE_COUNT = 40

    POISONED_COUNT = 40

    SENSITIVE_COUNT = 40

    COMBINED_COUNT = 40

    def __init__(self):

        self.metadata = []
        self.expected = {}

        self.enterprise_files = sorted(
            ENTERPRISE_DIR.rglob("*.txt")
        )

        random.seed(42)

    # ---------------------------------------------------------

    def build(self):

        print("=" * 70)
        print("BUILDING LAYER-2 BENCHMARK")
        print("=" * 70)

        self.prepare()

        self.clean_files = random.sample(
            self.enterprise_files,
            self.CLEAN_COUNT
        )

        self.generate_clean()
        self.generate_duplicates()
        self.generate_near_duplicates()
        self.generate_poisoned()
        self.generate_sensitive()
        self.generate_combined()

        self.save_metadata()

        print("=" * 70)
        print("Layer-2 Benchmark Generated")
        print("=" * 70)

    # ---------------------------------------------------------

    def prepare(self):

        for folder in [
            CLEAN_DIR,
            DUP_DIR,
            NEAR_DIR,
            POISON_DIR,
            SENSITIVE_DIR,
            COMBINED_DIR,
        ]:

            folder.mkdir(
                parents=True,
                exist_ok=True
            )

            for file in folder.glob("*.txt"):
                file.unlink()

    # ---------------------------------------------------------

    def register(

        self,
        case_id,
        filename,
        source_policy,
        category,
        decision,
        duplicate,
        attack,
        sensitive,
    ):

        self.metadata.append({

            "case_id": case_id,
            "filename": filename,
            "source_policy": source_policy,
            "category": category

        })

        self.expected[filename] = {

            "decision": decision,
            "duplicate": duplicate,
            "attack": attack,
            "sensitive": sensitive

        }

    # ---------------------------------------------------------

    def generate_clean(self):

        print("Generating clean policies...")

        for i, src in enumerate(self.clean_files, 1):

            text = src.read_text(
                encoding="utf-8"
            )

            text = self.replace_policy_id(
                text,
                f"BENCH-CLEAN-{i:03}"
            )

            filename = f"L2-CLEAN-{i:03}.txt"

            (CLEAN_DIR / filename).write_text(
                text,
                encoding="utf-8"
            )

            self.register(

                case_id=f"L2-CLEAN-{i:03}",

                filename=filename,

                source_policy=src.stem,

                category="clean",

                decision="ACCEPT",

                duplicate=False,

                attack=False,

                sensitive=False

            )

    # ---------------------------------------------------------

    def generate_duplicates(self):

        print("Generating duplicate policies...")

        samples = random.sample(
            self.enterprise_files,
            self.DUPLICATE_COUNT
        )

        for i, src in enumerate(samples, 1):

            filename = f"L2-DUP-{i:03}.txt"

            shutil.copy2(
                src,
                DUP_DIR / filename
            )

            self.register(

                case_id=f"L2-DUP-{i:03}",

                filename=filename,

                source_policy=src.stem,

                category="duplicate",

                decision="REJECT",

                duplicate=True,

                attack=False,

                sensitive=False

            )

     # ---------------------------------------------------------

    def generate_near_duplicates(self):

        print("Generating near-duplicate policies...")

        samples = random.sample(
            self.enterprise_files,
            self.NEAR_DUPLICATE_COUNT
        )

        for i, src in enumerate(samples, 1):

            text = src.read_text(
                encoding="utf-8"
            )

            text = self.replace_policy_id(
                text,
                f"BENCH-NEAR-{i:03}"
            )

            modified = self.modify_policy(text)

            filename = f"L2-NEAR-{i:03}.txt"

            (NEAR_DIR / filename).write_text(
                modified,
                encoding="utf-8"
            )

            self.register(

                case_id=f"L2-NEAR-{i:03}",

                filename=filename,

                source_policy=src.stem,

                category="near_duplicate",

                decision="REVIEW",

                duplicate=False,

                attack=False,

                sensitive=False

            )   

    def generate_poisoned(self):

        print("Generating poisoned policies...")

        count = 0

        random.shuffle(self.enterprise_files)

        for src in self.enterprise_files:

            if count >= self.POISONED_COUNT:
                break

            text = src.read_text(
                encoding="utf-8"
            )

            text = self.replace_policy_id(
                text,
                f"BENCH-POISON-{count+1:03}"
            )

            poisoned, trigger, replacement = self.poison_policy(text)
            
            if poisoned is None:
                continue

            count += 1

            filename = f"L2-POISON-{count:03}.txt"

            (POISON_DIR / filename).write_text(

                poisoned,

                encoding="utf-8"

            )

            self.register(

                case_id=f"L2-POISON-{count:03}",

                filename=filename,

                source_policy=src.stem,

                category="poisoned",

                decision="REJECT",

                duplicate=False,

                attack=True,

                sensitive=False

            )

    LOW_RISK_PAYLOADS = [

        "Administrator Email: admin@example.com",

        "Server IP: 192.168.10.25",

        "Documentation URL: https://intranet.company.com"

    ]

    HIGH_RISK_PAYLOADS = [

        "AWS Key: AKIAIOSFODNN7EXAMPLE",

        "Bearer Token: Bearer abc123XYZ987TOKEN",

        "Password = Admin@123",

        "SSN: 123-45-6789",

        "Credit Card: 4111 1111 1111 1111"

    ]

    def inject_sensitive(self, text, high_risk=True):

        if high_risk:

            payload = random.choice(
                self.HIGH_RISK_PAYLOADS
            )

        else:

            payload = random.choice(
                self.LOW_RISK_PAYLOADS
            )

        return text + "\n\n" + payload

    def generate_sensitive(self):

        print("Generating sensitive-data policies...")

        samples = random.sample(
            self.enterprise_files,
            self.SENSITIVE_COUNT
        )

        half = self.SENSITIVE_COUNT // 2

        for i, src in enumerate(samples, 1):

            text = src.read_text(encoding="utf-8")

            text = self.replace_policy_id(
                text,
                f"BENCH-SENSITIVE-{i:03}"
            )

            if i <= half:

                payload = random.choice(
                    self.LOW_RISK_PAYLOADS
                )

                decision = "REVIEW"

            else:

                payload = random.choice(
                    self.HIGH_RISK_PAYLOADS
                )

                decision = "REJECT"

            modified = text + "\n\n" + payload

            filename = f"L2-SENSITIVE-{i:03}.txt"

            (SENSITIVE_DIR / filename).write_text(
                modified,
                encoding="utf-8"
            )

            self.register(

                case_id=f"L2-SENSITIVE-{i:03}",

                filename=filename,

                source_policy=src.stem,

                category="sensitive",

                decision=decision,

                duplicate=False,

                attack=False,

                sensitive=True

            )

    def generate_combined(self):

        print("Generating combined attack policies...")

        count = 0

        samples = random.sample(
            self.enterprise_files,
            self.COMBINED_COUNT
        )

        for src in samples:

            text = src.read_text(
                encoding="utf-8"
            )

            text = self.replace_policy_id(

                text,

                f"BENCH-COMBINED-{count+1:03}"

            )

            poisoned, _, _ = self.poison_policy(
                text
            )

            if poisoned is None:
                continue

            modified = self.modify_policy(
                poisoned
            )

            modified = self.inject_sensitive(
                modified,
                high_risk=True,
            )

            count += 1

            filename = f"L2-COMBINED-{count:03}.txt"

            (
                COMBINED_DIR / filename

            ).write_text(

                modified,

                encoding="utf-8"

            )

            self.register(

                case_id=f"L2-COMBINED-{count:03}",

                filename=filename,

                source_policy=src.stem,

                category="combined",

                decision="REJECT",

                duplicate=False,

                attack=True,

                sensitive=True,

            )

    # ---------------------------------------------------------

    def save_metadata(self):

        with open(

            BENCHMARK_DIR / "metadata.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                self.metadata,

                f,

                indent=4

            )

        with open(

            BENCHMARK_DIR / "expected_results.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                self.expected,

                f,

                indent=4

            )

    def modify_policy(self, text):

        replacements = {

            r"\bmust\b": "should",
            r"\bshall\b": "should",
            r"\brequired\b": "recommended",
            r"\borganization\b": "company",
            r"\bEnterprise\b": "Corporate",

            r"\bprohibited\b": "discouraged",
            r"\bmandatory\b": "recommended",
            r"\bimmediately\b": "as soon as practical",
            r"\bwithin 24 hours\b": "within 48 hours",
            r"\bonly\b": "primarily",
            r"\ball employees\b": "authorized employees",

        }

        modified = text

        changes = 0

        for pattern, replacement in replacements.items():

            modified, count = re.subn(
                pattern,
                replacement,
                modified,
                flags=re.IGNORECASE
            )

            changes += count

            if changes >= 5:
                break

        return modified

    def poison_policy(self, text):

        from pathlib import Path
        import json
        import random
        import re

        attacks = json.loads(
            Path(
                "src/research/attacks/attack_library.json"
            ).read_text(encoding="utf-8")
        )

        random.shuffle(attacks)

        lower = text.lower()

        for attack in attacks:

            original = attack.get(
                "original",
                ""
            ).strip()

            poisoned = attack.get(
                "poisoned",
                ""
            ).strip()

            if not original or not poisoned:
                continue

            if original.lower() not in lower:
                continue

            modified = re.sub(
                re.escape(original),
                poisoned,
                text,
                flags=re.IGNORECASE,
                count=1,
            )

            return modified, original, poisoned

        return None, None, None

    def replace_policy_id(self, text, new_policy_id):

        pattern = r"(Policy\s*ID\s*:\s*)([^\r\n]+)"

        return re.sub(
            pattern,
            rf"\1{new_policy_id}",
            text,
            count=1,
            flags=re.IGNORECASE,
        )


   


if __name__ == "__main__":

    BenchmarkBuilder().build()