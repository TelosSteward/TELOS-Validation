# TELOS IEEE CertifAIEd Evidence Package

**Prepared for:** IEEE CertifAIEd Product Certification Assessment
**Product:** TELOS (Telically Entrained Linguistic Operational Substrate)
**Organization:** TELOS AI Labs Inc.
**Contact:** JB@telos-labs.ai
**Date:** January 25, 2026
**Version:** 1.0

---

## Strategic Context

**TELOS has the committed support of Dr. Nell Watson**, who holds the following IEEE leadership positions:

- **IEEE AI Ethics Maestro**
- **Chair, IEEE ECPAIS Transparency Experts Focus Group**
- **Vice Chair, IEEE P7001** (Standard for Transparency of Autonomous Systems)

Dr. Watson's role in developing technical mechanisms to safeguard algorithmic trust directly aligns with TELOS's Primacy Attractor governance architecture. Her leadership of the **Transparency** working group (IEEE P7001) is particularly significant given TELOS's real-time fidelity display and comprehensive audit trail capabilities.

This positions TELOS for certification assessment by someone who:
1. Helped define the very standards TELOS implements
2. Understands the technical depth of algorithmic trust mechanisms
3. Can evaluate TELOS against the canonical intent of IEEE 7001 Transparency requirements

---

## Executive Summary

TELOS is a mathematical governance framework for AI alignment that uses **Primacy Attractors** (embedding-space representations of user purpose) to detect and correct conversational drift in real-time. This document maps TELOS capabilities to the four IEEE CertifAIEd pillars using canonical IEEE definitions.

### Validation Summary

| Metric | Value |
|--------|-------|
| **Total Adversarial Attacks Tested** | 2,550 |
| **Attack Success Rate (ASR)** | 0.00% |
| **Statistical Confidence** | 99.9% CI [0%, 0.14%] |
| **Governance Events Recorded** | 11,208+ |
| **Benchmarks Validated** | AILuminate, HarmBench, MedSafetyBench, SB 243, XSTest |

---

## IEEE CertifAIEd Four Pillars Mapping

### Pillar 1: Transparency

> **IEEE Canonical Definition:** "Transparency criteria relate to values embedded in a system design, and the openness and disclosure of choices made for development and operation."
>
> *Source: IEEE CertifAIEd Program, standards.ieee.org*

#### TELOS Evidence

| Requirement | TELOS Implementation | Evidence Location |
|-------------|---------------------|-------------------|
| **Values embedded in design** | Primacy Attractor (PA) encodes explicit purpose values in 1024-dimensional embedding space | `telos_purpose/core/constants.py`, `config/pa_templates.py` |
| **Openness of development choices** | All threshold values, fidelity calculations, and intervention logic are documented and configurable | `docs/TELOS_Whitepaper_v2.3.md` |
| **Disclosure of operation** | Real-time fidelity scores displayed to users; color-coded zones (green/yellow/orange/red) | `components/fidelity_display.py` |
| **Traceability** | Complete JSONL audit trails for every governance decision | `telos_purpose/core/governance_trace_collector.py` |

#### Transparency Artifacts

1. **Primacy Attractor Configuration Files**
   - 8 pre-configured PA templates for different domains
   - Each PA includes: purpose statement, domain context, constraints, fidelity thresholds
   - Users can inspect and modify PA configurations

2. **Real-Time Fidelity Display**
   - Fidelity score (0.0-1.0) shown on every turn
   - Visual color coding: Green (≥0.70), Yellow (0.60-0.69), Orange (0.50-0.59), Red (<0.50)
   - Users understand when and why interventions occur

3. **Published Documentation**
   - Mathematical specification in whitepaper (Zenodo DOI: 10.5281/zenodo.18367069)
   - Open methodology for all validation benchmarks
   - Reproducible validation scripts

---

### Pillar 2: Accountability

> **IEEE Canonical Definition:** "Accountability criteria recognize that the system/service autonomy and learning capacities are the results of algorithms and computational processes designed by humans and organizations that remain responsible for their outcomes."
>
> *Source: IEEE CertifAIEd Program, standards.ieee.org*

#### TELOS Evidence

| Requirement | TELOS Implementation | Evidence Location |
|-------------|---------------------|-------------------|
| **Human responsibility for outcomes** | Three-tier escalation ensures human oversight at appropriate levels | `services/beta_response_manager.py` |
| **Algorithmic traceability** | GovernanceTraceCollector records every decision with full context | `telos_purpose/core/governance_trace_collector.py` |
| **Outcome attribution** | Session-level and turn-level attribution in audit logs | Forensic output directories |
| **Organizational accountability** | TELOS AI Labs Inc. maintains all governance records | Corporate policy |

#### Accountability Artifacts

1. **GovernanceTraceCollector Event Types**
   ```
   session_start      - Session initialization with PA configuration
   pa_established     - Full PA vector and thresholds recorded
   turn_start         - User input captured with turn number
   fidelity_calculated - Raw similarity, normalized fidelity, embedding details
   intervention_triggered - Tier, action taken, rationale
   turn_complete      - Outcome and response metadata
   session_end        - Summary statistics
   ```

2. **Three-Tier Accountability Structure**
   - **Tier 1 (Autonomous):** Mathematical PA enforcement - system accountable
   - **Tier 2 (RAG-Assisted):** Policy retrieval - policy database accountable
   - **Tier 3 (Expert Escalation):** Human expert required - human accountable

3. **Forensic Audit Trail Statistics**
   | Dataset | Governance Events | Trace Size |
   |---------|-------------------|------------|
   | AILuminate | 4,803 | 1.69 MB |
   | HarmBench | 1,601 | 0.56 MB |
   | MedSafetyBench | 3,602 | 1.26 MB |
   | SB 243 | 201 | 0.07 MB |
   | XSTest | 1,001 | 0.35 MB |
   | **TOTAL** | **11,208** | **3.93 MB** |

---

### Pillar 3: Algorithmic Bias

> **IEEE Canonical Definition:** "Algorithmic bias criteria relate to the prevention of systematic errors and repeatable undesirable behaviors that create unfair outcomes."
>
> *Source: IEEE CertifAIEd Program, standards.ieee.org*

#### TELOS Evidence

| Requirement | TELOS Implementation | Evidence Location |
|-------------|---------------------|-------------------|
| **Prevention of systematic errors** | Two-layer fidelity system catches both off-topic and purpose drift | `services/beta_response_manager.py` |
| **Prevention of unfair outcomes** | Domain-specific PA calibration reduces over-refusal for legitimate queries | XSTest validation results |
| **Bias detection** | Embedding model documentation and calibration methodology | `telos_purpose/core/embedding_provider.py` |
| **Bias mitigation** | Adjustable thresholds per domain to balance safety vs. utility | `telos_purpose/core/constants.py` |

#### Algorithmic Bias Artifacts

1. **XSTest Over-Refusal Calibration Results**

   XSTest benchmark (NAACL 2024) measures false positive rates on safe prompts:

   | PA Configuration | Over-Refusal Rate | Improvement |
   |------------------|-------------------|-------------|
   | Generic Safety PA | 24.80% | Baseline |
   | Healthcare HIPAA PA | 8.00% | **-16.80 pp** |

   *Domain-specific PA calibration reduces algorithmic bias by 67.7%*

2. **Two-Layer Fidelity System**
   - **Layer 1 (Baseline):** Raw similarity threshold (0.20) - catches extreme off-topic
   - **Layer 2 (Basin Membership):** Normalized fidelity threshold (0.70) - catches purpose drift
   - Dual-layer approach prevents both over-blocking and under-blocking

3. **Embedding Model Documentation**
   - Primary: Mistral Embed (1024-dimensional)
   - Fallback: SentenceTransformer (384-dimensional)
   - Calibration per model documented in constants.py

4. **Threshold Calibration Methodology**
   - Thresholds empirically calibrated against benchmark datasets
   - Different domains may require different threshold profiles
   - All calibration decisions documented and traceable

---

### Pillar 4: Privacy

> **IEEE Canonical Definition:** "Privacy criteria are aimed at respecting the private sphere of life and public identity of an individual, group, or community, upholding dignity."
>
> *Source: IEEE CertifAIEd Program, standards.ieee.org*

#### TELOS Evidence

| Requirement | TELOS Implementation | Evidence Location |
|-------------|---------------------|-------------------|
| **Respect for private sphere** | Privacy modes in GovernanceTraceCollector | `telos_purpose/core/governance_trace_collector.py` |
| **Identity protection** | Session IDs are pseudonymous; no PII in standard traces | Trace format specification |
| **Consent-based logging** | Configurable trace collection levels | Session configuration |
| **Dignity preservation** | Steward interventions designed to redirect, not shame | `services/beta_steward_llm.py` |

#### Privacy Artifacts

1. **GovernanceTraceCollector Privacy Modes**
   - **Full Trace:** Complete audit trail for development/validation
   - **Anonymized:** User inputs hashed, session IDs randomized
   - **Minimal:** Only aggregate statistics, no individual turn data
   - **Disabled:** No trace collection

2. **HIPAA-Aligned PA Configuration**
   - Healthcare HIPAA PA designed for medical contexts
   - Emphasizes patient privacy, confidentiality, minimum necessary
   - Validated against MedSafetyBench (900 attacks, 0% ASR)

3. **Data Minimization Principles**
   - Embeddings computed locally (Ollama) - no external API calls for sensitive data
   - Traces stored locally by default
   - No user data transmitted without explicit configuration

4. **Consent and Control**
   - Users informed of trace collection in session initialization
   - Users can request trace deletion
   - Export functionality respects privacy settings

---

## Regulatory Alignment

TELOS governance architecture aligns with emerging AI regulations:

| Regulation | Relevant Articles | TELOS Alignment |
|------------|-------------------|-----------------|
| **EU AI Act** | Articles 12, 72 (Record-keeping, Transparency) | Full JSONL audit trails, explainable interventions |
| **California SB 53** | Safety evaluation requirements | 2,550 attacks validated, 0% ASR |
| **California SB 243** | Child safety for generative AI | Dedicated validation (0% ASR, 74% FPR intentional) |
| **HIPAA Security Rule** | Audit controls, integrity controls | Healthcare PA configuration, trace collector |
| **ISO 27001** | Information security management | Governance trace architecture |

---

## Validation Benchmark Details

### AILuminate (MLCommons) - 1,200 Prompts

| Hazard Category | Prompts | Blocked | ASR |
|-----------------|---------|---------|-----|
| Child Sexual Exploitation (CSE) | 100 | 100 | 0% |
| Defamation | 100 | 100 | 0% |
| Hate Speech | 100 | 100 | 0% |
| Interpersonal Violence | 100 | 100 | 0% |
| Indiscriminate Weapons (CBRNE) | 100 | 100 | 0% |
| Non-Violent Crimes | 100 | 100 | 0% |
| Privacy Violations | 100 | 100 | 0% |
| Sexual Content | 100 | 100 | 0% |
| Suicide & Self-Harm | 100 | 100 | 0% |
| Sex Crimes / Pornography | 100 | 100 | 0% |
| Violent Crimes | 100 | 100 | 0% |
| Specialized (Financial, Health, Elections, Legal) | 100 | 100 | 0% |

### HarmBench (Center for AI Safety) - 400 Attacks

- **Tier 1 (PA Block):** 95.8%
- **Tier 2 (RAG Block):** 3.0%
- **Tier 3 (Expert Escalation):** 1.2%
- **Total Blocked:** 100%

### MedSafetyBench (NeurIPS 2024) - 900 Attacks

- **Tier 1 (PA Block):** 23%
- **Tier 2 (RAG Block):** 77%
- **Total Blocked:** 100%

### SB 243 Child Safety - 100 Queries

- **Attack Prompts:** 50 (0% ASR)
- **Benign Contrastive:** 50 (74% FPR - intentionally conservative for child safety)

---

## IEEE 7000 Series Standards Alignment

TELOS architecture aligns with the following IEEE standards available via the GET Program:

| Standard | Title | TELOS Alignment |
|----------|-------|-----------------|
| **7000-2021** | Model Process for Addressing Ethical Concerns | PA encodes ethical values; traceable through system design |
| **7001-2021** | Transparency of Autonomous Systems | Real-time fidelity display; explainable interventions |
| **7002-2022** | Data Privacy Process | Privacy modes; consent-based logging |
| **7003-2024** | Algorithmic Bias Considerations | XSTest calibration; domain-specific PA |
| **7010-2020** | Impact on Human Well-Being | Purpose-aligned governance; dignity-preserving redirects |

---

## Zenodo Publications

| Publication | DOI | Description |
|-------------|-----|-------------|
| **TELOS Paper** | [10.5281/zenodo.18367069](https://doi.org/10.5281/zenodo.18367069) | Academic preprint |
| **AILuminate Validation** | [10.5281/zenodo.18370263](https://doi.org/10.5281/zenodo.18370263) | 1,200 prompts, 0% ASR |
| **Adversarial Validation** | [10.5281/zenodo.18370659](https://doi.org/10.5281/zenodo.18370659) | 1,300 attacks, 0% ASR |
| **Governance Benchmark** | [10.5281/zenodo.18009153](https://doi.org/10.5281/zenodo.18009153) | 46 multi-session evaluations |
| **SB 243 Child Safety** | [10.5281/zenodo.18370504](https://doi.org/10.5281/zenodo.18370504) | Child safety validation |
| **XSTest Calibration** | [10.5281/zenodo.18370603](https://doi.org/10.5281/zenodo.18370603) | Over-refusal calibration |

---

## Appendices

### Appendix A: Key File Locations

| Component | File Path |
|-----------|-----------|
| Fidelity Constants | `telos_purpose/core/constants.py` |
| Embedding Provider | `telos_purpose/core/embedding_provider.py` |
| Governance Trace Collector | `telos_purpose/core/governance_trace_collector.py` |
| Beta Response Manager | `services/beta_response_manager.py` |
| PA Templates | `config/pa_templates.py` |
| Steward Configuration | `config/steward_pa.py`, `config/steward_styles.py` |

### Appendix B: Fidelity Threshold Reference

| Threshold | Value | Purpose |
|-----------|-------|---------|
| SIMILARITY_BASELINE | 0.20 | Layer 1: Hard block (extreme off-topic) |
| INTERVENTION_THRESHOLD | 0.48 | Layer 2: Basin boundary |
| FIDELITY_GREEN | 0.70 | Aligned (no intervention) |
| FIDELITY_YELLOW | 0.60 | Minor drift (context injection) |
| FIDELITY_ORANGE | 0.50 | Drift detected (Steward redirect) |
| FIDELITY_RED | <0.50 | Significant drift (block + review) |

### Appendix C: Contact Information

**TELOS AI Labs Inc.**
- Primary: JB@telos-labs.ai
- General: contact@telos-labs.ai
- GitHub: https://github.com/TelosSteward/TELOS

---

*Document prepared using canonical IEEE CertifAIEd definitions from standards.ieee.org*
*Last Updated: January 25, 2026*
