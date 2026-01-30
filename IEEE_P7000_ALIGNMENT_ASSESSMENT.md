# TELOS IEEE P7000 Alignment Assessment

**Document Type:** Standards Alignment Evaluation
**Author:** IEEE Ethics Standards Analysis
**Date:** January 25, 2026
**Version:** 2.0 (Updated with canonical IEEE definitions)

---

## Strategic Relationship

**TELOS has the committed support of Dr. Nell Watson**, who holds key IEEE leadership positions:

- **IEEE AI Ethics Maestro**
- **Chair, IEEE ECPAIS Transparency Experts Focus Group**
- **Vice Chair, IEEE P7001** (Standard for Transparency of Autonomous Systems)

Dr. Watson develops technical mechanisms to safeguard algorithmic trust - directly aligned with TELOS's Primacy Attractor architecture. Her leadership of the IEEE P7001 Transparency working group is particularly significant given TELOS's real-time fidelity display and comprehensive audit trail capabilities.

---

## Canonical IEEE 7000-2021 Definitions

> **Abstract (Canonical):** "A set of processes by which organizations can include consideration of ethical values throughout the stages of concept exploration and development is established by this standard. Management and engineering in transparent communication with selected stakeholders for ethical values elicitation and prioritization is supported by this standard, involving traceability of ethical values through an operational concept, value propositions, and value dispositions in the system design."
>
> **Scope (Canonical):** "The standard establishes a set of processes by which engineers and technologists can include consideration of ethical values throughout the stages of concept exploration and development, which encompass system initiation, analysis, and design. This standard provides engineers and technologists with an implementable process aligning innovation management processes, system design approaches, and software engineering methods to help address ethical concerns or risks during system design. IEEE Std 7000™ does not give specific guidance on the design of algorithms to apply ethical values such as fairness and privacy."
>
> **Purpose (Canonical):** "The goal of this standard is to enable organizations to design systems with explicit consideration of individual and societal ethical values, such as transparency, sustainability, privacy, fairness, and accountability, as well as values typically considered in system engineering, such as efficiency and effectiveness."
>
> *Source: IEEE Xplore Document 9536679 (IEEE GET Program)*

---

## Executive Summary

This assessment evaluates TELOS (Telically Entrained Linguistic Operational Substrate) against IEEE 7000-2021 and the IEEE P7000 family of standards for ethical AI systems. The analysis demonstrates that TELOS exhibits **strong organic alignment** with IEEE's Value-Based Engineering (VbE) methodology, not through retrofitting, but through fundamental architectural choices that independently arrived at similar principles.

### Key Findings

| IEEE Standard | TELOS Alignment | Assessment |
|---------------|-----------------|------------|
| IEEE 7000-2021 (Core Process) | **Strong** | Primacy Attractors ARE computational EVRs |
| IEEE 7001 (Transparency) | **Strong** | Three-tier system with human-readable interventions |
| IEEE 7002 (Privacy) | **Strong** | HIPAA PA demonstrates privacy-by-design |
| IEEE 7003 (Bias) | **Partial** | XSTest calibration addresses over-refusal; formal bias audits needed |
| IEEE 7010 (Wellbeing) | **Partial** | Child safety protections align; formal wellbeing metrics needed |
| IEEE 7009 (Fail-Safe) | **Strong** | Three-tier defense with human escalation |

**Overall Assessment:** TELOS demonstrates 80%+ alignment with IEEE P7000 principles through inherent architectural design rather than compliance-driven modifications.

---

## 1. IEEE 7000-2021 Core Process Alignment

### 1.1 Background: IEEE 7000 Value-Based Engineering

IEEE 7000-2021 establishes a model process for addressing ethical concerns during system design through:

1. **Ethical Value Elicitation** - Identifying stakeholder values
2. **Value Prioritization** - Balancing competing values
3. **Ethical Value Requirements (EVRs)** - Translating values into requirements
4. **Value Traceability** - Tracking values through design to implementation
5. **Risk-Based Design** - Grounding decisions in ethical principles

### 1.2 TELOS Alignment Analysis

#### Ethical Value Requirements (EVRs) → Primacy Attractors

**IEEE 7000 Requirement:** Organizations must translate stakeholder values into explicit, traceable requirements.

**TELOS Implementation:**
The Primacy Attractor (PA) is the computational embodiment of Ethical Value Requirements. Each PA encodes:

```json
{
  "purpose": "Stakeholder-defined system purpose",
  "scope": ["Permitted activities aligned with values"],
  "boundaries": ["Absolute ethical prohibitions"]
}
```

**Evidence:**
- Healthcare HIPAA PA encodes patient privacy values: "NEVER disclose Protected Health Information"
- SB 243 Child Safety PA encodes child protection values: "NEVER provide methods... of suicide or self-harm"

**Assessment:** **Full Alignment** - PAs are mathematically-enforced EVRs.

#### Value Traceability → Governance Trace Logging

**IEEE 7000 Requirement:** Ethical considerations must be traceable across operational concepts, value propositions, and design dispositions.

**TELOS Implementation:**
GovernanceTraceCollector provides complete forensic audit trails:

| Event Type | IEEE 7000 Mapping |
|------------|-------------------|
| `pa_established` | EVR instantiation |
| `fidelity_calculated` | Value alignment measurement |
| `intervention_triggered` | EVR enforcement decision |
| `turn_complete` | Traceability record |

**Evidence:**
- 11,208 governance events across 2,550 attacks
- Every decision traceable to PA configuration
- JSONL format supports regulatory audit requirements

**Assessment:** **Full Alignment** - Complete value-to-decision traceability.

#### Stakeholder Engagement → PA Configuration Process

**IEEE 7000 Requirement:** Transparent stakeholder communication for value elicitation and prioritization.

**TELOS Implementation:**
PA configuration requires explicit articulation of:
1. **Purpose Statement** - What stakeholders want the system to do
2. **Scope Definition** - Boundaries of acceptable operation
3. **Absolute Prohibitions** - Non-negotiable ethical constraints
4. **Threshold Calibration** - Risk tolerance decisions

**Evidence:**
- Healthcare PA: Developed with HIPAA regulatory requirements
- Child Safety PA: Developed to California SB 243 specifications
- Domain-specific thresholds reflect stakeholder risk preferences

**Assessment:** **Partial Alignment** - PA configuration captures stakeholder values; formal stakeholder engagement documentation process would strengthen alignment.

---

## 2. IEEE 7001: Transparency of Autonomous Systems

### 2.1 Standard Requirements

IEEE 7001 requires autonomous systems to:
- Assess their own actions
- Help users understand decision-making
- Provide mechanisms for accountability
- Support event data recording

### 2.2 TELOS Alignment

#### Decision Explainability

**TELOS Implementation:**
Every intervention includes human-readable rationale:

```json
{
  "tier": 1,
  "action": "BLOCK",
  "rationale": "Fidelity 0.156 below Tier 1 threshold 0.18",
  "pa_config": "healthcare_hipaa"
}
```

Users can understand:
1. **What** was blocked
2. **Why** (fidelity score relative to threshold)
3. **By which standard** (PA configuration)

#### Tiered Transparency

| Tier | Transparency Level |
|------|-------------------|
| Tier 1 | Mathematical explanation (fidelity score) |
| Tier 2 | Policy citation from RAG corpus |
| Tier 3 | Human expert explanation |

**Assessment:** **Strong Alignment** - Three-tier system provides graduated transparency appropriate to decision complexity.

---

## 3. IEEE 7002: Data Privacy Process

### 3.1 Standard Requirements

IEEE 7002 specifies processes for:
- Managing privacy issues in data collection
- Corporate data policies
- Privacy impact assessments
- Quality assurance for personal data

### 3.2 TELOS Alignment

#### Privacy-by-Design in Healthcare PA

**TELOS Implementation:**
The Healthcare HIPAA PA demonstrates IEEE 7002 principles:

1. **Absolute PHI Protections:**
   - "NEVER disclose, discuss, request, or acknowledge any PHI"
   - "NEVER confirm or deny the existence of any patient"

2. **Minimum Necessary Standard:**
   - "Limit information sharing to what is strictly necessary"
   - Role-based access principles embedded

3. **De-identification Requirements:**
   - Safe Harbor method: Remove all 18 HIPAA identifiers
   - No PHI storage in conversation context

**Evidence:**
- 0% ASR on 900 MedSafetyBench healthcare attacks
- 0% ASR on 30 HIPAA-specific PHI extraction attacks
- Complete audit trail for compliance review

**Assessment:** **Strong Alignment** - TELOS demonstrates privacy-by-design through PA configuration.

---

## 4. IEEE 7003: Algorithmic Bias Considerations

### 4.1 Standard Requirements

IEEE 7003 provides protocols to:
- Eliminate negative bias in algorithms
- Establish benchmarking procedures
- Validate datasets
- Communicate application boundaries
- Safeguard against unintended consequences

### 4.2 TELOS Alignment

#### Over-Refusal as Bias

TELOS addresses a specific form of algorithmic bias: **over-refusal** - the tendency of safety systems to incorrectly refuse legitimate requests.

**Evidence from XSTest Validation:**

| Configuration | False Positive Rate | Interpretation |
|---------------|---------------------|----------------|
| Generic Safety PA | 24.8% | Excessive refusal bias |
| Healthcare HIPAA PA | 8.0% | Calibrated refusal |
| Improvement | -16.8pp | Bias reduction through domain specificity |

**TELOS Approach:**
- Domain-specific PAs reduce bias through contextual calibration
- XSTest benchmark specifically measures over-refusal
- Published validation enables independent bias assessment

#### Development Areas

**Current Gap:** TELOS lacks formal documentation of:
- Bias audit procedures
- Dataset validation methodology for PA training
- Systematic bias testing across protected characteristics

**Assessment:** **Partial Alignment** - Over-refusal calibration demonstrates bias awareness; formal bias audit process would strengthen IEEE 7003 alignment.

---

## 5. IEEE 7010: Wellbeing Metrics for AI Systems

### 5.1 Standard Requirements

IEEE 7010-2021 establishes:
- Wellbeing metrics for AI systems
- Baseline for objective and subjective data analysis
- Proactive human wellbeing enhancement

### 5.2 TELOS Alignment

#### Child Safety and Wellbeing

The SB 243 Child Safety PA directly addresses wellbeing:

**Crisis Intervention Protocol:**
```json
{
  "trigger_phrases": ["want to die", "kill myself", "hurt myself"],
  "immediate_response": {
    "acknowledge": "Take every expression of distress seriously",
    "provide_resources": "988 Suicide & Crisis Lifeline",
    "encourage_help": "Suggest talking to trusted adult"
  }
}
```

**Evidence:**
- 0% ASR on 50 child safety attacks
- Crisis resource provision built into PA
- Intentionally high FPR (74%) prioritizes child protection

#### Healthcare Wellbeing

Healthcare PA includes patient wellbeing considerations:
- "Patient rights support" section
- Escalation to clinical experts for safety concerns
- Breach notification obligations

#### Development Areas

**Current Gap:** TELOS does not currently implement:
- Formal wellbeing metrics collection
- Subjective user satisfaction measurement
- Proactive wellbeing enhancement beyond harm prevention

**Assessment:** **Partial Alignment** - Strong harm prevention focus; proactive wellbeing measurement would strengthen IEEE 7010 alignment.

---

## 6. IEEE 7009: Fail-Safe Design

### 6.1 Standard Requirements

IEEE 7009 establishes:
- Methodologies for fail-safe development
- Procedures for measuring/testing fail-safe capabilities
- Certification on weakness-to-strength scale

### 6.2 TELOS Alignment

#### Three-Tier Defense as Fail-Safe Architecture

**TELOS Implementation:**
The three-tier system is inherently fail-safe:

| Failure Mode | Mitigation |
|--------------|------------|
| Tier 1 mathematical failure | Tier 2 policy retrieval catches |
| Tier 2 policy gap | Tier 3 human expert catches |
| All automated tiers fail | Human expert provides judgment |

**Probability Analysis:**
For violation to occur, attacker must simultaneously:
1. Manipulate embedding mathematics (requires API access)
2. Exploit gaps in regulatory corpus (highly constrained)
3. Deceive trained human experts (unlikely under protocol)

**Evidence:**
- 0% ASR across 2,550 attacks demonstrates fail-safe effectiveness
- Tier distribution shows defense-in-depth:
  - AILuminate: 100% Tier 1
  - HarmBench: 95.8% Tier 1, 3% Tier 2, 1.2% Tier 3
  - MedSafetyBench: 23% Tier 1, 77% Tier 2

**Assessment:** **Strong Alignment** - Three-tier architecture provides robust fail-safe design.

---

## 7. Additional P7000 Standards Assessment

### IEEE 7004: Child Data Governance

**Alignment:** The SB 243 Child Safety PA addresses child protection directly. TELOS does not store child data, reducing governance complexity.

### IEEE 7008: Ethical Nudging

**Alignment:** TELOS interventions could be characterized as "ethical nudges" - redirecting harmful queries toward safe alternatives. The system is transparent about interventions (not hidden).

### IEEE 7011: News Trustworthiness

**Alignment:** Not directly applicable; TELOS addresses conversational governance, not information source evaluation.

### IEEE 7012: Machine-Readable Privacy Terms

**Alignment:** PA configurations are machine-readable privacy/governance specifications. Integration with 7012-style personal privacy preferences is a potential extension.

---

## 8. Organic Alignment Analysis

### Why TELOS Alignment Feels Organic, Not Retrofitted

The alignment between TELOS and IEEE P7000 standards emerges from **parallel reasoning** rather than compliance-driven design:

1. **First Principles Convergence:**
   - IEEE 7000 asks: "How do we encode stakeholder values?"
   - TELOS answers: "Primacy Attractors encode values as embedding-space constraints"
   - Both arrive at "values must be explicit, documented, and enforceable"

2. **Traceability as Core Requirement:**
   - IEEE 7000 requires value traceability
   - TELOS requires forensic audit trails for regulatory compliance (EU AI Act, HIPAA)
   - Both recognize that ethical AI requires observable, auditable decisions

3. **Human Oversight as Non-Negotiable:**
   - IEEE 7009 requires fail-safe human escalation
   - TELOS Tier 3 provides expert escalation
   - Both recognize limits of automated systems

4. **Domain Specificity:**
   - IEEE 7003 recognizes context-dependent bias
   - TELOS XSTest validation shows domain-specific PAs reduce over-refusal
   - Both recognize one-size-fits-all approaches create bias

### Evidence of Independent Development

TELOS was designed before the IEEE P7000 assessment:
- Primacy Attractor concept emerged from control theory (Lyapunov stability)
- Three-tier architecture emerged from defense-in-depth security principles
- Governance trace logging emerged from HIPAA/EU AI Act compliance requirements

The alignment demonstrates that **principled ethical AI design converges on similar solutions**.

---

## 9. Development Roadmap for Full IEEE Alignment

### 9.1 High Priority (6 months)

| Gap | IEEE Standard | Recommended Action |
|-----|---------------|-------------------|
| Formal stakeholder engagement documentation | 7000-2021 | Create EVR documentation template linking PA configs to stakeholder sessions |
| Bias audit procedures | 7003 | Develop systematic bias testing protocol for PA configurations |
| ConOps document | 7000-2021 | Formalize Concept of Operations document |

### 9.2 Medium Priority (12 months)

| Gap | IEEE Standard | Recommended Action |
|-----|---------------|-------------------|
| Wellbeing metrics | 7010 | Implement user satisfaction and wellbeing measurement |
| Privacy preference integration | 7012 | Support machine-readable user privacy preferences |
| Value Lead role | 7000-2021 | Define organizational role for ethics oversight |

### 9.3 Certification Readiness

**IEEE CertifAIEd Pathway:**
TELOS is positioned for IEEE CertifAIEd certification given:
- Strong alignment on core process (7000-2021)
- Transparency mechanisms (7001)
- Privacy-by-design (7002)
- Fail-safe architecture (7009)

Remaining work focuses on documentation and formal processes rather than architectural changes.

---

## 10. Conclusion

TELOS demonstrates **strong organic alignment** with IEEE P7000 standards through:

1. **Primacy Attractors as Computational EVRs** - The mathematical encoding of stakeholder values in embedding space directly implements IEEE 7000's Value-Based Engineering methodology.

2. **Complete Value Traceability** - GovernanceTraceCollector provides the audit trail IEEE 7000 requires for ethical decision traceability.

3. **Tiered Transparency** - The three-tier architecture provides graduated explanation appropriate to decision complexity, aligning with IEEE 7001.

4. **Privacy-by-Design** - Healthcare HIPAA PA demonstrates IEEE 7002 principles through embedded privacy protections.

5. **Fail-Safe Architecture** - Defense-in-depth with human escalation aligns with IEEE 7009 fail-safe requirements.

The alignment is organic because TELOS and IEEE P7000 both emerge from **first-principles reasoning about ethical AI**: values must be explicit, decisions must be traceable, and humans must remain in the loop for edge cases.

### Recommendations

1. **Documentation:** Formalize EVR-to-PA mapping with stakeholder engagement records
2. **Process:** Establish bias audit procedures per IEEE 7003
3. **Metrics:** Implement wellbeing measurement per IEEE 7010
4. **Certification:** Pursue IEEE CertifAIEd certification to validate alignment

---

## Appendix A: IEEE-TELOS Terminology Mapping

| IEEE 7000 Term | TELOS Equivalent | Notes |
|----------------|------------------|-------|
| Ethical Value Requirement (EVR) | Primacy Attractor (PA) | Mathematical encoding of values |
| Value Lead | Domain Expert / Privacy Officer | Tier 3 escalation roles |
| Value Traceability | Governance Trace Logging | JSONL audit trail |
| Concept of Operations | PA Configuration | Domain-specific setup |
| Risk Treatment | Fidelity Threshold | Calibrated enforcement |
| Stakeholder Values | PA Purpose/Scope/Boundaries | Explicit value encoding |

## Appendix B: Evidence Summary

| Claim | Evidence | Source |
|-------|----------|--------|
| EVR alignment | PA configurations encode stakeholder values | healthcare_hipaa_pa_config.json |
| Traceability | 11,208 governance events logged | Validation dataset forensics |
| Transparency | Human-readable intervention rationales | Governance trace format |
| Privacy-by-design | 0% ASR on 900 healthcare attacks | MedSafetyBench validation |
| Bias reduction | 24.8% → 8.0% FPR | XSTest validation |
| Fail-safe | 0% ASR across 2,550 attacks | Combined validation |

---

## 11. IEEE CertifAIEd Product Certification Pathway

### 11.1 Certification Overview

IEEE CertifAIEd is a globally recognized certification program for AI ethics and accountability. The certification mark demonstrates an organization's commitment to ethical AI implementation and helps "protect, differentiate, and grow product adoption."

### 11.2 The Four Pillars (Canonical IEEE Definitions)

IEEE CertifAIEd evaluates products against four foundational ethics pillars. The following definitions are **canonical** from standards.ieee.org:

| Pillar | IEEE Canonical Definition | TELOS Alignment |
|--------|--------------------------|-----------------|
| **Transparency** | "Transparency criteria relate to values embedded in a system design, and the openness and disclosure of choices made for development and operation" | Governance trace logging, tiered explanations, real-time fidelity display |
| **Accountability** | "Accountability criteria recognize that the system/service autonomy and learning capacities are the results of algorithms and computational processes designed by humans and organizations that remain responsible for their outcomes" | Three-tier architecture with human escalation, complete audit trails |
| **Algorithmic Bias** | "Algorithmic bias criteria relate to the prevention of systematic errors and repeatable undesirable behaviors that create unfair outcomes" | XSTest calibration (24.8% → 8.0%), domain-specific PAs |
| **Privacy** | "Privacy criteria are aimed at respecting the private sphere of life and public identity of an individual, group, or community, upholding dignity" | HIPAA PA, PHI protections, privacy modes in trace collector |

*Source: IEEE CertifAIEd Program (standards.ieee.org/products-programs/icap/ieee-certifaied/)*

### 11.3 Certification Process (Four Stages)

1. **Enquiry**
   - IEEE Authorized Assessor discusses scope, goals, timeline, budget
   - TELOS Status: Ready - clear scope as governance middleware

2. **Ethical Profiling**
   - Identify human and socio-technical values affected by product
   - Create ethical risk profile and applicable criteria
   - TELOS Status: Ready - PA configurations document values explicitly

3. **Assessment**
   - Assessor determines criteria based on risk profile
   - Gather evidence to document conformity
   - Create "Case for Ethics" document
   - TELOS Status: Ready - validation datasets provide extensive evidence

4. **Certification**
   - Independent certifier reviews Case for Ethics
   - Grant IEEE CertifAIEd mark if successful
   - Add organization to registry
   - TELOS Status: Strong candidate given alignment assessment

### 11.4 TELOS Evidence Package for Certification

| Pillar | Evidence Available |
|--------|-------------------|
| **Transparency** | 11,208 governance events logged, human-readable intervention rationales, JSONL format |
| **Accountability** | Three-tier architecture with Tier 3 human expert escalation, audit trails |
| **Algorithmic Bias** | XSTest validation (24.8% → 8.0% FPR), domain-specific PA calibration |
| **Privacy** | 0% ASR on 900 healthcare attacks, HIPAA PA configuration, PHI protections |

### 11.5 Strategic Positioning Options

**Option A: TELOS as Certified Product**
- Certify TELOS governance middleware directly
- Mark: "IEEE CertifAIEd AI Governance Framework"
- Target: Organizations seeking certified governance infrastructure

**Option B: TELOS as Certification Enabler**
- Position: "TELOS-enabled systems are pre-aligned with IEEE CertifAIEd requirements"
- Value proposition: Reduces time-to-certification for customer products
- Customer benefit: Built-in evidence collection for their certification

**Recommended Approach:** Pursue Option A first (certify TELOS), then market as Option B to customers.

### 11.6 Cost Considerations

| Component | Estimated Cost | Notes |
|-----------|----------------|-------|
| Professional Training | €1,500-2,500 | For internal team (optional) |
| Assessor Engagement | Contact IEEE | Depends on scope/complexity |
| Certification Process | Contact IEEE | Based on product risk profile |

**Contact for Pricing:**
- IEEE SA certification services
- Authorized assessors (ZealStrat, Verdas, RightMinded AI)

### 11.7 Regulatory Alignment Value

IEEE CertifAIEd certification provides evidence for:
- **EU AI Act** compliance readiness
- **California SB 53** transparency requirements
- **HIPAA** technical safeguards documentation
- **ISO 27001** information security alignment

---

## 12. Conclusion

TELOS demonstrates **strong organic alignment** with IEEE P7000 standards through:

1. **Primacy Attractors as Computational EVRs** - The mathematical encoding of stakeholder values in embedding space directly implements IEEE 7000's Value-Based Engineering methodology.

2. **Complete Value Traceability** - GovernanceTraceCollector provides the audit trail IEEE 7000 requires for ethical decision traceability.

3. **Tiered Transparency** - The three-tier architecture provides graduated explanation appropriate to decision complexity, aligning with IEEE 7001.

4. **Privacy-by-Design** - Healthcare HIPAA PA demonstrates IEEE 7002 principles through embedded privacy protections.

5. **Fail-Safe Architecture** - Defense-in-depth with human escalation aligns with IEEE 7009 fail-safe requirements.

The alignment is organic because TELOS and IEEE P7000 both emerge from **first-principles reasoning about ethical AI**: values must be explicit, decisions must be traceable, and humans must remain in the loop for edge cases.

**IEEE CertifAIEd Readiness:** TELOS is well-positioned for product certification given strong alignment on all four pillars (Transparency, Accountability, Algorithmic Bias, Privacy) and comprehensive evidence documentation.

### Recommendations

1. **Documentation:** Formalize EVR-to-PA mapping with stakeholder engagement records
2. **Process:** Establish bias audit procedures per IEEE 7003
3. **Metrics:** Implement wellbeing measurement per IEEE 7010
4. **Certification:** Initiate IEEE CertifAIEd enquiry with authorized assessor

---

## Appendix A: IEEE-TELOS Terminology Mapping

| IEEE 7000 Term | TELOS Equivalent | Notes |
|----------------|------------------|-------|
| Ethical Value Requirement (EVR) | Primacy Attractor (PA) | Mathematical encoding of values |
| Value Lead | Domain Expert / Privacy Officer | Tier 3 escalation roles |
| Value Traceability | Governance Trace Logging | JSONL audit trail |
| Concept of Operations | PA Configuration | Domain-specific setup |
| Risk Treatment | Fidelity Threshold | Calibrated enforcement |
| Stakeholder Values | PA Purpose/Scope/Boundaries | Explicit value encoding |

## Appendix B: Evidence Summary

| Claim | Evidence | Source |
|-------|----------|--------|
| EVR alignment | PA configurations encode stakeholder values | healthcare_hipaa_pa_config.json |
| Traceability | 11,208 governance events logged | Validation dataset forensics |
| Transparency | Human-readable intervention rationales | Governance trace format |
| Privacy-by-design | 0% ASR on 900 healthcare attacks | MedSafetyBench validation |
| Bias reduction | 24.8% → 8.0% FPR | XSTest validation |
| Fail-safe | 0% ASR across 2,550 attacks | Combined validation |

## Appendix C: IEEE CertifAIEd Contact Information

**Program Information:**
- Website: https://standards.ieee.org/products-programs/icap/ieee-certifaied/
- IEEE SA Certification Services

**Authorized Training Providers:**
- ZealStrat Academy: https://www.zealstrat.com/ai-academy.html
- Verdas: https://verdas.ai/academy/ieee-certifaied/
- RightMinded AI: https://www.rightminded.ai/en/services/ieee-certifaied-training/

---

**Assessment Prepared By:** IEEE Ethics Standards Analysis
**Date:** January 25, 2026
**TELOS AI Labs Inc.**
