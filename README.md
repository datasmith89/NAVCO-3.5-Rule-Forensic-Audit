# NAVCO "3.5% Rule" Forensic Audit

## Project Overview
This repository contains a forensic audit of the famous "3.5% Rule" of civil resistance (the claim that no nonviolent campaign has failed after achieving 3.5% active participation).

Using the original NAVCO datasets (v1.1, v1.2, and v1.3), this project reverse-engineers the statistic to determine its validity over time.

## Key Findings

| Dataset | Era | Status | Findings |
| :--- | :--- | :--- | :--- |
| **NAVCO 1.1** | 1900–2006 | **HOLDS** | The highest failure was **3.45%** (First Intifada). The "3.5% Rule" was effectively curve-fitted to exclude this case. |
| **NAVCO 1.2** | 1945–2013 | **BROKEN** | The rule failed immediately in 2011. **Bahrain (2011)** failed with **~6.5%** participation. |
| **NAVCO 1.3** | 1900–2019 | **SHATTERED** | Modern authoritarian learning has rendered the rule obsolete. **Hong Kong (2019)** failed with **~26%** participation. |

## ⚠️ Critical Context: Domestic Application in the U.S.

**The NAVCO dataset exclusively tracks "Maximalist" campaigns.**

According to the NAVCO 1.3 Codebook (p. 2), a "Maximalist" campaign is defined strictly as a movement with one of the following existential goals:
1.  **Regime Change** (Overthrowing the government/constitution)
2.  **Anti-Occupation** (Expelling a foreign military)
3.  **Secession** (Breaking away to form a new state)

**Implication for U.S. Politics:**
The "3.5% Rule" is a statistic derived solely from revolutions and insurrections. It does **not** measure the success of policy protests (e.g., gun control, healthcare, election integrity) within a democratic system.

**Therefore, if public figures (such as Maria J. Stephan or others) promote the "3.5% Rule" in the context of domestic U.S. politics, they are applying a framework of Regime Change.** By definition, applying this model to the United States implies a goal of overthrowing the existing government structure, as the dataset does not recognize non-maximalist reform movements as valid data points.

## How to Run the Audit

1.  **Install Dependencies:**
    ```bash
    conda env create -f environment.yml
    conda activate navco_audit
    ```

2.  **Place Data Files:**
    Ensure the following files are in the root directory:
    * `NAVCO 1.1.dta`
    * `NAVCO 1.2 Updated.xlsx`
    * `NAVCO 1.3 List.xlsx`

3.  **Run the Script:**
    ```bash
    python app.py
    ```

## Files
* `app.py`: The universal auditor script that checks all three dataset versions.
* `environment.yml`: Conda environment configuration.
