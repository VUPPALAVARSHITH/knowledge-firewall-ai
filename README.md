# 🛡️ Knowledge Firewall AI

> **An Enterprise Knowledge Security Framework for Protecting Organizational Knowledge Before, During, and After Retrieval-Augmented Generation (RAG).**

Knowledge Firewall AI is a security-first framework designed to protect enterprise knowledge throughout its lifecycle. It introduces a dedicated **Knowledge Firewall** between enterprise knowledge repositories and downstream Large Language Model (LLM) applications.

Unlike conventional RAG systems that primarily focus on retrieving relevant information, Knowledge Firewall AI applies security controls at both **knowledge admission time** and **runtime retrieval time**.

The framework verifies uploaded knowledge, generates multiple fingerprints, detects knowledge manipulation and sensitive information, computes trust scores, maintains a trusted knowledge repository, and verifies retrieved knowledge before allowing it to reach the LLM.

> **Knowledge Firewall AI is not a chatbot.**
>
> The Secure RAG Assistant included in this repository is one consumer of the trusted knowledge produced by the framework.

---

# 🎯 Project Overview

Modern enterprises increasingly use Retrieval-Augmented Generation (RAG) systems to provide AI assistants with access to internal organizational knowledge.

However, enterprise RAG systems introduce security risks when untrusted or manipulated knowledge enters the retrieval corpus.

Potential threats include:

- Corpus poisoning
- Knowledge manipulation
- Re-poisoning attacks
- Prompt injection
- Sensitive information leakage
- Semantic modification
- Unauthorized knowledge tampering
- Irrelevant knowledge entering the generation pipeline

Knowledge Firewall AI addresses these risks by introducing a security layer between enterprise knowledge and downstream AI applications.

The framework operates across two major security stages:

```text
                    Enterprise Knowledge
                            │
                            ▼
               Knowledge Admission Firewall
                            │
                 ┌──────────┼──────────┐
                 ▼          ▼          ▼
            Fingerprint   Attack    Sensitive
            Generation   Analysis      Data
                 │          │          │
                 └──────────┼──────────┘
                            ▼
                       Trust Engine
                            │
                     ACCEPT / REVIEW /
                        REJECT
                            │
                            ▼
                  Trusted Knowledge Base
                            │
                            ▼
                       Runtime RAG
                            │
                     Relevance Gate
                            │
                  Fingerprint Verification
                            │
                       Trust Engine
                            │
                            ▼
                    Knowledge Firewall
                            │
                            ▼
                           LLM
                            │
                            ▼
                     Secure Response
```

---

# 🏗️ System Architecture

```text
                    Enterprise Documents
                            │
                            ▼
                  Document Parsing Engine
                            │
                            ▼
                  Semantic Chunk Builder
                            │
                            ▼
              Fingerprint Generation Engine
        (SHA-256 • SimHash • Embedding Fingerprints)
                            │
                            ▼
              Knowledge Admission Firewall
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
 Repository Check     Attack Analysis    Sensitive Data
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
                    Admission Trust Engine
                            │
                     ACCEPT / REVIEW /
                        REJECT
                            │
                            ▼
              Trusted Enterprise Repository
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
        Repository      Integrity      Analytics /
        Management       Scanner        History
                            │
                            ▼
                    Secure Retrieval
                            │
                            ▼
                     Relevance Gate
                            │
                            ▼
              Runtime Fingerprint Engine
                            │
                            ▼
                    Similarity Engine
                            │
                            ▼
                      Trust Engine
                            │
                            ▼
                   Knowledge Firewall
                            │
                            ▼
                    Enterprise LLM
                            │
                            ▼
                Trusted Enterprise Response
```

---

# ✨ Key Features

## 🔐 Enterprise Knowledge Security

- Enterprise knowledge admission
- Repository verification
- Knowledge fingerprinting
- Trust-score generation
- Explainable security decisions
- Repository health monitoring
- Admission-time security analysis

## 🛡️ Knowledge Protection

- Corpus poisoning detection
- Knowledge manipulation detection
- Prompt-injection detection
- Sensitive-data detection
- Semantic integrity verification
- Runtime tamper detection
- Re-poisoning / duplicate analysis

## 🔎 Secure Retrieval

- Semantic retrieval
- Relevance gating
- Runtime chunk verification
- SHA-256 verification
- SimHash comparison
- Embedding similarity comparison
- Trust-aware context construction
- Secure prompt construction
- Trusted-context-only generation

## 🏢 Enterprise Management

- Enterprise dashboard
- Knowledge repository
- Knowledge Admission Firewall
- Repository Integrity Scanner
- Policy comparison
- Version history
- Trust analytics
- Enterprise Assistant

---

# 🔥 Knowledge Admission Firewall

The Knowledge Admission Firewall evaluates enterprise documents before they enter the trusted knowledge repository.

```text
Knowledge Upload
       │
       ▼
Policy Parsing
       │
       ▼
Semantic Chunking
       │
       ▼
Fingerprint Generation
       │
       ▼
Repository Similarity Analysis
       │
       ▼
Knowledge Manipulation Detection
       │
       ▼
Sensitive Data Detection
       │
       ▼
Admission Trust Engine
       │
       ▼
Admission Decision
       │
       ├──────────────► ACCEPT
       │
       ├──────────────► REVIEW
       │
       └──────────────► REJECT
```

## Admission Security Checks

The admission layer evaluates:

- SHA-256 fingerprints
- SimHash fingerprints
- Embedding similarity
- Repository similarity
- Duplicate policy identifiers
- Knowledge manipulation
- Prompt-injection patterns
- Sensitive information
- Admission trust

This prevents untrusted knowledge from being directly inserted into the trusted enterprise repository.

---

# 🧬 Knowledge Fingerprinting

Each semantic knowledge chunk is represented using multiple complementary fingerprints.

## SHA-256

Provides exact textual integrity verification.

```text
Original Text
      │
      ▼
   SHA-256
      │
      ▼
Exact Fingerprint
```

A modified chunk produces a different SHA-256 fingerprint.

## SimHash

Provides compact structural similarity information based on textual token patterns.

## Embedding Fingerprint

Provides semantic similarity information using sentence embeddings.

The framework combines these signals during runtime verification.

```text
              Knowledge Chunk
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     SHA-256      SimHash      Embedding
        │            │            │
        └────────────┼────────────┘
                     ▼
             Similarity Engine
                     │
                     ▼
                Trust Engine
```

---

# 🧠 Runtime Knowledge Firewall

The runtime firewall protects the retrieval-to-generation path.

```text
User Query
    │
    ▼
Semantic Retrieval
    │
    ▼
Top-K Candidates
    │
    ▼
Relevance Gate
    │
    ├── Irrelevant ─────► Reject
    │
    ▼
Runtime Fingerprinting
    │
    ▼
Fingerprint Comparison
    │
    ├── SHA-256
    ├── SimHash
    └── Embedding
    │
    ▼
Trust Engine
    │
    ├── TRUSTED
    ├── SUSPICIOUS
    └── BLOCKED
    │
    ▼
Trusted Context
    │
    ▼
Enterprise LLM
    │
    ▼
Secure Response
```

Only knowledge that passes the relevance and integrity checks is admitted into the final LLM context.

---

# ⚖️ Trust Engine

The Trust Engine combines multiple verification signals into a unified trust score.

## Current Weighting

| Signal | Weight |
|---|---:|
| SHA-256 | 40% |
| SimHash | 25% |
| Embedding Similarity | 30% |
| Section Priority | 5% |

The resulting score is used to determine the runtime decision:

```text
Trust Score
     │
     ├── TRUSTED
     │
     ├── SUSPICIOUS
     │
     └── BLOCKED
```

Security gating rules are also applied so that a significant fingerprint deviation cannot simply be hidden by a high semantic similarity score.

---

# 🚨 Attack Detection

Knowledge Firewall AI includes a semantic attack library containing:

- **760 attack patterns**
- **31 attack categories**
- **200 Critical**
- **350 High**
- **210 Medium**

Attack categories include areas such as:

- Access Control
- AI Governance
- Identity Authentication
- Password Management
- Incident Response
- Data Classification
- Data Retention
- Remote Access
- Software Installation
- Threat Intelligence
- Vendor Management
- Research Data Protection

The Attack Analyzer identifies known malicious knowledge modifications and produces an explainable security result.

### Example

```text
Attack ID      : PI-006
Category       : Instruction Override
Severity       : Critical
Confidence     : 1.00
Recommendation : Reject Upload
```

---

# 🔒 Sensitive Data Detection

The admission pipeline also scans uploaded knowledge for potentially sensitive information.

Detection includes:

- Email addresses
- URLs
- IPv4 addresses
- API keys
- Bearer tokens
- Private keys
- Social Security numbers
- Credit-card information
- Passwords

Detected sensitive information contributes to the admission risk score and can result in document rejection.

---

# 📊 Enterprise Repository

The current trusted repository contains:

| Metric | Value |
|---|---:|
| Enterprise Policies | 925 |
| Knowledge Chunks | 12,025 |
| Trusted Chunks | 12,025 |
| Poisoned Chunks | 0 |
| Fingerprints | 12,025 |
| Fingerprint Version | 2.0 |
| Average Trust | 100% |

The repository represents the clean trusted baseline.

Malicious and sensitive documents are evaluated as admission-test inputs and are not intentionally inserted into the trusted baseline.

---

# 🧪 Experimental Validation

The framework was evaluated using clean, near-duplicate, sensitive-data, malicious, retrieval, and tampering scenarios.

## 1. Clean Knowledge Admission

```text
Policy          : DEMO-SEC-001
Chunks          : 10
Admission Trust : 100%
Decision        : ACCEPT
```

## 2. Near-Policy Admission

```text
Policy          : DEMO-SEC-002
Chunks          : 10
Admission Trust : 100%
Decision        : ACCEPT
```

## 3. Sensitive Information Detection

```text
Policy          : DEMO-SENS-001
Findings        : 4
Admission Trust : 80%
Decision        : REJECT
```

## 4. Prompt-Injection / Knowledge Manipulation

```text
Policy          : DEMO-POISON-001
Attack ID       : PI-006
Severity        : Critical
Admission Trust : 60%
Decision        : REJECT
```

## 5. Clean Runtime Verification

A trusted VPN knowledge chunk produced:

```text
SHA Similarity       : 1.0
SimHash Similarity   : 1.0
Embedding Similarity : 1.0
Trust Score          : 0.995
Decision             : TRUSTED
```

## 6. Runtime Tampering Detection

After modifying a trusted chunk:

```text
SHA Similarity       : 0.0
SimHash Similarity   : 0.84375
Embedding Similarity : 0.94967
Trust Score          : 0.5458
Decision             : BLOCKED
```

This demonstrates that textual modification is detected through multiple independent integrity signals.

## 7. Known Query

For:

> Does VPN require authentication?

The runtime firewall produced:

```text
Retrieved  : 5
Relevant   : 5
Trusted    : 5
Suspicious : 0
Blocked    : 0

Verification Rate: 100%
```

The system generated an answer using only verified trusted context.

## 8. Unknown Query

For:

> What is the company international office relocation policy?

The relevance gate produced:

```text
Retrieved  : 5
Relevant   : 0
Trusted    : 0
Suspicious : 0
Blocked    : 0

Verification Rate: 0%
```

No irrelevant retrieved knowledge was passed to the LLM.

---

# 📈 Security Validation Summary

| Security Scenario | Result |
|---|---|
| Clean admission | ✅ ACCEPT |
| Near-policy analysis | ✅ ACCEPT |
| Sensitive information | ❌ REJECT |
| Prompt injection | ❌ REJECT |
| Knowledge manipulation | ❌ REJECT |
| Clean runtime verification | ✅ TRUSTED |
| Runtime tampering | ❌ BLOCKED |
| Relevant enterprise query | ✅ TRUSTED CONTEXT |
| Unknown enterprise query | ❌ NO CONTEXT ADMITTED |

---

# 🏢 Enterprise Framework

The Streamlit Enterprise Framework provides a centralized interface for managing enterprise knowledge.

## Available Modules

- 🏠 Enterprise Dashboard
- 📂 Enterprise Knowledge Repository
- ⬆️ Knowledge Admission Firewall
- 🛡️ Repository Integrity Scanner
- 🔍 Policy Comparison
- 🕒 Version History
- 📈 Trust Analytics
- 🤖 Enterprise Assistant
- ⚙️ Settings

The Enterprise Assistant is a consumer of the security framework rather than the primary purpose of the system.

---

# 📂 Project Structure

```text
knowledge-firewall-ai/
│
├── data/
│   ├── enterprise/
│   ├── metadata/
│   ├── benchmark/
│   ├── evaluation/
│   └── vector_store/
│
├── docs/
├── models/
├── notebooks/
├── outputs/
├── reports/
├── scripts/
├── tests/
│
├── src/
│   │
│   ├── config/
│   │
│   ├── core/
│   │   ├── fingerprint/
│   │   ├── firewall/
│   │   ├── ingestion/
│   │   ├── llm/
│   │   ├── metadata/
│   │   ├── preprocessing/
│   │   ├── rag/
│   │   ├── repository/
│   │   └── retriever/
│   │
│   ├── enterprise/
│   │   ├── managers/
│   │   ├── pages/
│   │   └── upload/
│   │
│   ├── research/
│   │   ├── attacks/
│   │   ├── benchmark/
│   │   ├── dataset_generator/
│   │   └── evaluation/
│   │
│   ├── services/
│   └── utils/
│
├── enterprise_app.py
├── streamlit_app.py
├── app.py
├── requirements.txt
└── README.md
```

---

# 🧩 Core Modules

| Module | Responsibility |
|---|---|
| Policy Parser | Parses enterprise policy documents |
| Semantic Chunk Builder | Creates structured semantic chunks |
| Embedding Engine | Generates semantic embeddings |
| Fingerprint Engine | Generates SHA-256, SimHash and embedding fingerprints |
| Repository Checker | Detects duplicates and similar repository knowledge |
| Attack Analyzer | Detects known knowledge manipulation patterns |
| Sensitive Data Detector | Detects potentially sensitive information |
| Admission Trust Engine | Computes document admission trust |
| Knowledge Firewall | Verifies retrieved knowledge at runtime |
| Similarity Engine | Compares runtime and trusted fingerprints |
| Trust Engine | Computes runtime trust and security decisions |
| Secure Retriever | Performs semantic enterprise retrieval |
| Secure RAG | Connects verified context to the LLM |
| Enterprise Framework | Provides management and visualization interfaces |

---

# 📚 Research Data

The repository contains research and evaluation resources including:

- Enterprise Knowledge Base
- Semantic Attack Library
- Semantic Chunk Database
- Trusted Fingerprint Database
- Benchmark Dataset
- Evaluation Dataset

The trusted repository currently contains **12,025 clean indexed chunks across 925 enterprise policies**.

---

# 💻 Technology Stack

## Programming

- Python 3.12

## AI / NLP

- Sentence Transformers
- all-MiniLM-L6-v2
- Ollama
- Qwen 2.5

## Vector Search

- FAISS

## Data Processing

- Pandas
- NumPy

## Visualization / Interface

- Streamlit
- Matplotlib

## Machine Learning

- Scikit-learn

## Development

- VS Code
- Jupyter Notebook

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<username>/knowledge-firewall-ai.git
cd knowledge-firewall-ai
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Configure Ollama

The Enterprise Assistant uses Ollama for local LLM generation.

Install Ollama and make sure the service is running.

Pull the configured model:

```bash
ollama pull qwen2.5:3b
```

Verify:

```bash
ollama list
```

The current project configuration uses:

```text
qwen2.5:3b
```

---

# ▶️ Running the Framework

## Enterprise Framework

```bash
streamlit run enterprise_app.py
```

This launches the complete enterprise interface containing:

- Dashboard
- Repository
- Knowledge Admission
- Integrity Scanner
- Policy Comparison
- Version History
- Trust Analytics
- Enterprise Assistant
- Settings

## Standalone Secure RAG Interface

```bash
streamlit run streamlit_app.py
```

## Command-Line Secure RAG

```bash
python app.py
```

---

# 🧪 Running Security Tests

Runtime verification:

```bash
python -m src.core.firewall.verifier
```

Knowledge Firewall:

```bash
python -m src.core.firewall.knowledge_firewall
```

Attack Analyzer:

```bash
python -m src.core.security.attack_analyzer
```

---

# 🔬 Research Objectives

The project aims to:

- Protect enterprise knowledge before retrieval.
- Detect corpus poisoning.
- Detect knowledge manipulation.
- Detect prompt injection embedded in enterprise knowledge.
- Detect sensitive information during admission.
- Verify knowledge integrity at runtime.
- Prevent irrelevant knowledge from reaching the LLM.
- Generate explainable trust scores.
- Secure enterprise RAG pipelines.
- Provide a reusable security framework for downstream enterprise AI applications.

---

# 🏆 Current Project Status

## Core Security

| Component | Status |
|---|---|
| Enterprise Knowledge Base | ✅ Complete |
| Semantic Chunking | ✅ Complete |
| Fingerprinting Engine | ✅ Complete |
| Repository Checker | ✅ Complete |
| Attack Analyzer | ✅ Complete |
| Sensitive Data Detector | ✅ Complete |
| Admission Trust Engine | ✅ Complete |
| Secure Retrieval | ✅ Complete |
| Relevance Gate | ✅ Complete |
| Knowledge Firewall | ✅ Complete |
| Runtime Verification | ✅ Complete |
| Secure RAG | ✅ Complete |

## Enterprise Framework

| Component | Status |
|---|---|
| Enterprise Dashboard | ✅ Complete |
| Knowledge Repository | ✅ Complete |
| Knowledge Admission Firewall | ✅ Complete |
| Repository Integrity Scanner | ✅ Complete |
| Policy Comparison | ✅ Complete |
| Version History | ✅ Complete |
| Trust Analytics | ✅ Complete |
| Enterprise Assistant | ✅ Complete |
| Settings | ✅ Complete |

## Research Validation

| Area | Status |
|---|---|
| Clean admission validation | ✅ Complete |
| Sensitive-data rejection validation | ✅ Complete |
| Prompt-injection validation | ✅ Complete |
| Runtime tampering validation | ✅ Complete |
| Known-query validation | ✅ Complete |
| Unknown-query validation | ✅ Complete |
| Trusted repository validation | ✅ Complete |

---

# 🗺️ Project Lifecycle

```text
Phase 1
Research & Dataset Construction
        │
        ▼
Phase 2
Knowledge Security Architecture
        │
        ▼
Phase 3
Fingerprinting & Trust Engine
        │
        ▼
Phase 4
Knowledge Admission Firewall
        │
        ▼
Phase 5
Runtime Knowledge Firewall
        │
        ▼
Phase 6
Secure RAG Integration
        │
        ▼
Phase 7
Enterprise Framework
        │
        ▼
Phase 8
Security Evaluation
        │
        ▼
     COMPLETE
```

---

# 💡 Why Knowledge Firewall AI?

## Traditional RAG

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retrieval
    ↓
LLM
```

The fundamental assumption is that the knowledge repository is trustworthy.

Knowledge Firewall AI changes that assumption:

```text
Documents
    ↓
Security Analysis
    ↓
Fingerprinting
    ↓
Trust Evaluation
    ↓
Admission Decision
    ↓
Trusted Repository
    ↓
Retrieval
    ↓
Relevance Verification
    ↓
Runtime Integrity Verification
    ↓
Trust Evaluation
    ↓
LLM
```

The framework therefore treats enterprise knowledge as a security-sensitive asset rather than merely a source of context.

---

# 🎓 Research Contribution

The central contribution of Knowledge Firewall AI is the introduction of a reusable security framework that protects enterprise knowledge across its lifecycle.

The framework combines:

- Knowledge admission security
- Multi-modal knowledge fingerprinting
- Repository similarity analysis
- Semantic attack detection
- Sensitive-data detection
- Runtime integrity verification
- Relevance gating
- Trust-based context filtering
- Explainable security decisions

This allows downstream RAG applications to consume knowledge that has passed explicit security controls rather than directly trusting the underlying repository.

---

# 📄 Academic Context

This project is developed as an academic research project investigating security mechanisms for enterprise Retrieval-Augmented Generation systems.

The experimental implementation demonstrates the feasibility of applying admission-time and runtime security controls to enterprise knowledge before it is supplied to an LLM.

---

# 👨‍💻 Team

**VUPPALA VARSHITH**
**VONTELA GOPIKA**

---

# 📄 License

This project is developed as an academic research project for demonstrating secure enterprise Retrieval-Augmented Generation systems.