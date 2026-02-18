# NAVCO Forensic Audit: The Collapse of the 3.5% Rule

## Project Overview
This repository contains a Python-based forensic audit of the **"3.5% Rule"**—the widely cited claim that no nonviolent campaign has failed after reaching a 3.5% participation threshold. This audit reverse-engineers the data to identify exactly when and how this "rule" became obsolete in the 21st century.

## Data Sources & Links
All data used in this audit is sourced from the **Nonviolent and Violent Campaigns and Outcomes (NAVCO) Data Project**.

* **NAVCO 1.1:** [Download from EricaChenoweth.com](https://www.ericachenoweth.com/research) / [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/07IDW)
* **NAVCO 1.2:** [Download from Ash Center, Harvard](https://ash.harvard.edu/programs/nonviolent-and-violent-campaigns-and-outcomes-data-project/)
* **NAVCO 1.3:** [Harvard Dataverse (1900-2019 List)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MHOXDV)

## The Timeline of Failure

| Dataset | Scope | Max Failure Found | Forensic Status |
| :--- | :--- | :--- | :--- |
| **NAVCO 1.1** | 1900–2006 | **3.45%** (First Intifada) | **VERIFIED** |
| **NAVCO 1.2** | 1945–2013 | **6.38%** (Bahrain, 2011) | **BROKEN** |
| **NAVCO 1.3** | 1900–2019 | **~26.0%** (Hong Kong, 2019) | **SHATTERED** |

## ⚠️ Critical Forensic Finding: The 1.3 Data Gap
While `NAVCO 1.3 List.xlsx` is the official outcome ledger through 2019, it represents a "forensic dead-end" for the 3.5% Rule. 
* **1.1 & 1.2:** Include the raw numbers (Membership/Population) needed to calculate the threshold.
* **1.3:** The researchers **omitted the participation columns** in this specific summary list. 
* **Finding:** The 1.3 file confirms massive modern movements like **Hong Kong (2019)** were failures (`SUCCESS=0`), but hides the participation data that proves the 3.5% Rule is no longer valid.

## ⚖️ Political Implication: U.S. Domestic Application

**The NAVCO dataset identifies success ONLY within the goals of a "Maximalist Campaign."**

As defined in the official NAVCO Codebook (p. 2), a maximalist campaign is strictly limited to:
1.  **Regime Change** (Overthrowing the existing government/constitution)
2.  **Anti-Occupation** (Expelling a foreign military)
3.  **Secession** (Breaking away to form a new state)

### The Warning
When public figures (such as Maria J. Stephan) promote the "3.5% Rule" in the United States, they are citing a manual for **regime change**. Because the dataset excludes all non-maximalist movements (policy reform/protest), using this rule in the U.S. carries a strong insinuation of **overthrowing the government**. As this audit shows, "all states defend themselves," and 21st-century state capacity has rendered the 3.5% threshold obsolete.

## Citations
If using this data, please credit the original authors:
* **Chenoweth, Erica, and Maria J. Stephan.** 2011. *Why Civil Resistance Works: The Strategic Logic of Nonviolent Conflict*. New York: Columbia University Press.
* **Chenoweth, Erica, and Christopher Wiley Shay.** 2020. *NAVCO 1.3 Dataset*. Harvard Dataverse.

## Usage
1. Place `NAVCO 1.1.dta`, `NAVCO 1.2 Updated.xlsx`, and `NAVCO 1.3 List.xlsx` in the root folder.
2. Run `python app.py`.
