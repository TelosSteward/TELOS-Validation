# TELOS Validation Dataset

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17702890.svg)](https://doi.org/10.5281/zenodo.17702890)
[![Governance DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18009153.svg)](https://doi.org/10.5281/zenodo.18009153)
[![Attacks](https://img.shields.io/badge/attacks-4%2C428-blue)](https://github.com/TelosSteward/TELOS-Validation)
[![ASR](https://img.shields.io/badge/attack%20success%20rate-0%25-brightgreen)](https://github.com/TelosSteward/TELOS-Validation)
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-orange)](https://creativecommons.org/licenses/by/4.0/)

Official validation data for TELOS AI governance framework.

---

## Results Summary

- **Total Attacks**: 4,428
- **Attack Success Rate**: 0.00%
- **Statistical Confidence**: 99.9% CI [0%, 0.07%]
- **Autonomous Blocking**: 100% (All layers)

---

## Validation Domains

### Healthcare Safety Validation ✅
- **Total Attacks**: 1,586
- **Benchmarks**: MedSafetyBench, HarmBench, AgentHarm, HIPAA scenarios
- **Result**: 0% ASR - No harmful medical outputs
- **Master Signature**: `HC-7a4f982b6c1e3d92`

### Privacy Protection Validation ✅
- **Total Attacks**: 2,842
- **Categories**: 55 PII types across 7 major categories
  - Names (400), Identifiers (560), Financial (480)
  - Contact (400), Addresses (480), Health (480), Biometric (42)
- **Attack Types**: 8 sophisticated attack patterns
- **Result**: 0% ASR - No PII leakage
- **PA Signature**: `b0245fca86d7cd92`

---

## Benchmarks

### MedSafetyBench (NeurIPS 2024)
- **Attacks**: 900
- **Blocked**: 900 (100%)
- **Source**: [AI4LIFE-GROUP/med-safety-bench](https://github.com/AI4LIFE-GROUP/med-safety-bench)

### HarmBench (Center for AI Safety)
- **Attacks**: 400
- **Blocked**: 400 (100%)
- **Source**: [centerforaisafety/HarmBench](https://github.com/centerforaisafety/HarmBench)

### AgentHarm
- **Attacks**: 286
- **Blocked**: 286 (100%)

### Privacy Attack Suite (PIIBench)
- **Attacks**: 2,842
- **Blocked**: 2,842 (100%)
- **Attack Types**: Template injection, in-context learning, soft prompt training, multi-party confusion, credential extraction, memorization probing, side-channel, social engineering

---

## Files

- **`telos_complete_validation_dataset.json`** - Complete validation summary with statistical analysis
- **`medsafetybench_validation_results.json`** - Detailed MedSafetyBench results (900 attacks)
- **`harmbench_validation_results_summary.json`** - HarmBench aggregate results (400 attacks)
- **`privacy_validation_results.json`** - Privacy protection results (2,842 attacks)

---

## Full Dataset

Complete dataset with documentation available on Zenodo:

| Dataset | DOI | Description |
|---------|-----|-------------|
| **Adversarial Validation** | [10.5281/zenodo.17702890](https://doi.org/10.5281/zenodo.17702890) | 4,428 attacks, 0% ASR |
| **Governance Benchmark** | [10.5281/zenodo.18009153](https://doi.org/10.5281/zenodo.18009153) | 46 sessions, dual PA validation |

---

## Verification

Verify all validation results using the turnkey verification tool:

```bash
python VERIFY_ALL_TELOS_VALIDATIONS.py
```

**Expected Output**:
```
✅ Healthcare Validation: 1,586 attacks, 0% ASR (HC-7a4f982b6c1e3d92)
✅ Privacy Validation: 2,842 attacks, 0% ASR (b0245fca86d7cd92)
✅ Master Verification Hash: 7cd553c59913e2dc
✅ All TELOS validations verified successfully
```

---

## Related Repositories

- **[TELOS Observatory](https://github.com/TelosSteward/Observatory)** - Main TELOS framework with reproduction scripts and documentation

---

## Citation

For the adversarial validation dataset:

```bibtex
@dataset{brunner_2025_telos_adversarial,
  author       = {Brunner, Jeffrey},
  title        = {{TELOS Adversarial Validation Dataset}},
  month        = nov,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {2.0},
  doi          = {10.5281/zenodo.17702890},
  url          = {https://doi.org/10.5281/zenodo.17702890},
  note         = {4,428 adversarial attacks, 0\% ASR}
}
```

For the governance benchmark dataset:

```bibtex
@dataset{brunner_2025_telos_governance,
  author       = {Brunner, Jeffrey},
  title        = {{TELOS Governance Benchmark Dataset}},
  month        = dec,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.18009153},
  url          = {https://doi.org/10.5281/zenodo.18009153}
}
```

---

## License

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

---

**Last Updated**: December 21, 2025
**Dataset Version**: 2.0
