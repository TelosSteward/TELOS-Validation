# TELOS Validation Dataset

[![Paper DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18367069.svg)](https://doi.org/10.5281/zenodo.18367069)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18013104.svg)](https://doi.org/10.5281/zenodo.18013104)
[![Governance DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18009153.svg)](https://doi.org/10.5281/zenodo.18009153)
[![SB 243 DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18027446.svg)](https://doi.org/10.5281/zenodo.18027446)
[![XSTest DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18368390.svg)](https://doi.org/10.5281/zenodo.18368390)
[![Attacks](https://img.shields.io/badge/attacks-1%2C300-blue)](https://github.com/TelosSteward/TELOS-Validation)
[![ASR](https://img.shields.io/badge/attack%20success%20rate-0%25-brightgreen)](https://github.com/TelosSteward/TELOS-Validation)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](https://www.apache.org/licenses/LICENSE-2.0)

Official validation data for TELOS AI governance framework.

---

## Results Summary

- **Total Attacks**: 1,300
- **Attack Success Rate**: 0.00%
- **Statistical Confidence**: 99.9% CI [0%, 0.28%]
- **Autonomous Blocking**: 95.8% (Tier 1)

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

### SB 243 Child Safety (California Regulation)
- **Attacks**: 50 (suicide, self-harm, sexual content, eating disorders)
- **Benign Contrastive**: 50 (helper/educational queries)
- **Attack Success Rate**: 0.00%
- **False Positive Rate**: 74.00%
- **Note**: High FPR is intentional for child safety contexts

### XSTest Over-Refusal Calibration (NAACL 2024)
- **Safe Prompts**: 250 (benign queries that should be allowed)
- **Generic Safety PA**: 24.80% over-refusal rate
- **Healthcare HIPAA PA**: 8.00% over-refusal rate
- **Calibration Improvement**: 16.80 percentage points
- **Source**: [paul-rottger/exaggerated-safety](https://github.com/paul-rottger/exaggerated-safety)
- **Note**: Demonstrates domain-specific PA calibration reduces false positives

---

## Files

- **`telos_complete_validation_dataset.json`** - Complete validation summary with statistical analysis
- **`medsafetybench_validation_results.json`** - Detailed MedSafetyBench results (900 attacks)
- **`harmbench_validation_results_summary.json`** - HarmBench aggregate results (400 attacks)
- **`sb243_validation_results.json`** - SB 243 attack validation results (50 attacks)
- **`sb243_false_positive_results.json`** - SB 243 false positive analysis (50 benign queries)

---

## Zenodo Publications

| Publication | DOI | Description |
|-------------|-----|-------------|
| **TELOS Paper** | [10.5281/zenodo.18367069](https://doi.org/10.5281/zenodo.18367069) | Academic preprint: TELOS governance framework |
| **Adversarial Validation** | [10.5281/zenodo.18013104](https://doi.org/10.5281/zenodo.18013104) | 1,300 adversarial attacks, 0% ASR |
| **Governance Benchmark** | [10.5281/zenodo.18009153](https://doi.org/10.5281/zenodo.18009153) | 46 multi-session governance evaluations |
| **SB 243 Child Safety** | [10.5281/zenodo.18027446](https://doi.org/10.5281/zenodo.18027446) | CA SB 243 child safety validation (0% ASR, 74% FPR) |
| **XSTest Calibration** | [10.5281/zenodo.18368390](https://doi.org/10.5281/zenodo.18368390) | Over-refusal calibration (24.8% → 8.0% with domain PA) |

---

## Related Repositories

- **[TELOS](https://github.com/TelosSteward/TELOS)** - Main TELOS framework with reproduction scripts and documentation

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
  version      = {1.0},
  doi          = {10.5281/zenodo.18013104},
  url          = {https://doi.org/10.5281/zenodo.18013104}
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

For the SB 243 child safety validation:

```bibtex
@dataset{brunner_2025_telos_sb243,
  author       = {Brunner, Jeffrey},
  title        = {{TELOS SB 243 Child Safety Validation Dataset}},
  month        = dec,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.18027446},
  url          = {https://doi.org/10.5281/zenodo.18027446}
}
```

For the XSTest over-refusal calibration:

```bibtex
@dataset{brunner_2026_telos_xstest,
  author       = {Brunner, Jeffrey},
  title        = {{TELOS XSTest Over-Refusal Calibration Dataset}},
  month        = jan,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.18368390},
  url          = {https://doi.org/10.5281/zenodo.18368390}
}
```

---

## License

**Apache License 2.0**

---

**Last Updated**: January 25, 2026
**Dataset Version**: 1.2
