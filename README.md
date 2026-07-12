# 🛡️ Knowledge Firewall AI

> **An Enterprise Knowledge Security Framework for Trusted Retrieval-Augmented Generation (RAG) Systems**

Knowledge Firewall AI is a security-first framework designed to protect enterprise knowledge before it reaches Large Language Models (LLMs). Unlike conventional Secure RAG systems that focus only on retrieval, Knowledge Firewall AI introduces a dedicated **Knowledge Firewall** that continuously verifies, fingerprints, monitors, and protects organizational knowledge throughout its lifecycle.

---

## 🎯 Project Overview

Modern enterprises increasingly rely on Retrieval-Augmented Generation (RAG) systems to power AI assistants using internal knowledge bases. However, these systems are vulnerable to several security threats:

- Corpus Poisoning
- Re-Poisoning Attacks
- Prompt Injection
- Knowledge Tampering
- Sensitive Data Leakage
- Semantic Manipulation

Knowledge Firewall AI addresses these challenges by introducing a security layer between enterprise knowledge repositories and downstream AI applications.

---

## 🏗️ System Architecture

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
                 Knowledge Firewall AI
      ├── Corpus Poisoning Detection
      ├── Re-Poisoning Detection
      ├── Prompt Injection Detection
      ├── Sensitive Data Detection
      ├── Semantic Integrity Verification
      ├── Runtime Trust Verification
      └── Knowledge Fingerprinting
                            │
                            ▼
                Knowledge Admission Engine
                 Allow • Reject • Review
                            │
                            ▼
          Trusted Enterprise Knowledge Repository
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
      Integrity Scanner  Analytics   Version History
                            │
                            ▼
                  Secure Retrieval Layer
                            │
                            ▼
                  Runtime Knowledge Firewall
                            │
                            ▼
                     Large Language Model
                            │
                            ▼
                  Trusted Enterprise Response
```

---

# ✨ Key Features

## Enterprise Knowledge Security

- Enterprise Knowledge Admission
- Repository Integrity Verification
- Knowledge Fingerprinting
- Trust Score Generation
- Explainable Security Decisions
- Continuous Repository Monitoring

---

## Knowledge Protection

- Corpus Poisoning Detection
- Re-Poisoning Detection
- Prompt Injection Resistance
- Sensitive Data Leakage Detection
- Semantic Integrity Verification
- Knowledge Tampering Detection

---

## Secure Retrieval

- Trusted Retrieval Pipeline
- Runtime Chunk Verification
- Secure Prompt Construction
- Context Filtering
- Trust-Aware Response Generation

---

## Enterprise Management

- Security Dashboard
- Knowledge Repository
- Integrity Scanner
- Policy Comparison
- Version History
- Trust Analytics
- Enterprise Assistant

---

# 🔬 Research Contribution

Knowledge Firewall AI extends traditional Secure RAG architectures by introducing a reusable enterprise security framework capable of:

- Knowledge Fingerprinting
- Runtime Trust Verification
- Repository Monitoring
- Enterprise Knowledge Admission
- Semantic Integrity Verification
- Explainable Trust Decisions

Unlike existing Secure RAG systems that protect only the retrieval process, Knowledge Firewall AI protects enterprise knowledge **before**, **during**, and **after** retrieval.

---

# 📂 Project Structure

```text
knowledge-firewall-ai/

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
│
│   ├── config/
│   ├── core/
│   │
│   │   ├── embeddings/
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

# 🧠 Core Modules

| Module | Description |
|---------|-------------|
| Policy Parser | Parses enterprise policy documents |
| Semantic Chunk Builder | Creates structured semantic chunks |
| Embedding Engine | Generates MiniLM embeddings |
| Fingerprint Engine | SHA256, SimHash and Embedding Fingerprints |
| Knowledge Firewall | Runtime security verification |
| Trust Engine | Computes trust scores |
| Secure Retriever | Retrieves trusted knowledge |
| Secure RAG | Generates trusted responses |

---

# 📊 Enterprise Modules

- Dashboard
- Knowledge Repository
- Knowledge Admission
- Integrity Scanner
- Policy Comparison
- Version History
- Trust Analytics
- Enterprise Assistant

---

# 📚 Datasets

The project includes multiple research datasets:

- Enterprise Knowledge Base
- Semantic Attack Library
- Poisoned Knowledge Repository
- Semantic Chunk Database
- Trusted Fingerprint Database
- Benchmark Dataset
- Evaluation Dataset

---

# 🧪 Security Pipeline

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
Knowledge Firewall
        │
        ▼
Trust Verification
        │
        ▼
Admission Decision
        │
        ▼
Trusted Repository
```

---

# 🔐 Runtime Pipeline

```text
User Query
      │
      ▼
Secure Retriever
      │
      ▼
Knowledge Firewall
      │
      ▼
Trusted Context
      │
      ▼
Prompt Builder
      │
      ▼
Large Language Model
      │
      ▼
Trusted Response
```

---

# 💻 Technology Stack

### Programming

- Python 3.12

### AI / NLP

- Sentence Transformers
- all-MiniLM-L6-v2
- Ollama
- Qwen 2.5

### Vector Search

- FAISS

### Data Processing

- Pandas
- NumPy

### Visualization

- Streamlit
- Matplotlib

### Machine Learning

- Scikit-learn

### Development

- VS Code
- Jupyter Notebook

---

# 🚀 Running the Project

## Clone Repository

```bash
git clone https://github.com/<username>/knowledge-firewall-ai.git
cd knowledge-firewall-ai
```

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Launch Enterprise Framework

```bash
streamlit run enterprise_app.py
```

---

## Launch Secure RAG Assistant

```bash
streamlit run streamlit_app.py
```

---

## Run Command-Line Interface

```bash
python app.py
```

---

# 📈 Current Status

| Component | Status |
|------------|--------|
| Dataset Generation | ✅ Complete |
| Fingerprinting Engine | ✅ Complete |
| Knowledge Firewall | ✅ Complete |
| Trust Engine | ✅ Complete |
| Secure Retrieval | ✅ Complete |
| Secure RAG | ✅ Complete |
| Enterprise Dashboard | 🚧 In Progress |
| Knowledge Admission | 🚧 In Progress |
| Integrity Scanner | 🚧 Planned |
| Trust Analytics | 🚧 Planned |

---

# 🎓 Research Objectives

- Protect enterprise knowledge before retrieval.
- Detect corpus poisoning attacks.
- Detect re-poisoning attacks.
- Prevent prompt injection.
- Verify semantic integrity.
- Generate explainable trust scores.
- Secure enterprise RAG pipelines.

---

# 📄 License

This project is developed as an academic research project for demonstrating secure enterprise Retrieval-Augmented Generation systems.

---

# 👨‍💻 Authors

**VUPPALA VARSHITH**

Enterprise Knowledge Security Framework

Academic Major Project
