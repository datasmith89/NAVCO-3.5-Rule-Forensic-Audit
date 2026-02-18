# NAVCO Forensic Audit: The Collapse of the 3.5% Rule

## Project Overview
This repository contains a Python-based forensic audit of the **"3.5% Rule"**—the widely cited claim by Erica Chenoweth and Maria J. Stephan that no nonviolent campaign has failed after reaching a 3.5% participation threshold.

By auditing the original datasets (**NAVCO 1.1, 1.2, and 1.3**), this project identifies exactly when and where the rule broke, and highlights a significant data gap in the latest version (1.3).

## The Timeline of Failure

| Dataset Version | Scope | Max Failure Found | Status |
| :--- | :--- | :--- | :--- |
| **NAVCO 1.1** | 1900–2006 | **3.45%** (First Intifada) | **VERIFIED** |
| **NAVCO 1.2** | 1945–2013 | **6.38%** (Bahrain, 2011) | **BROKEN** |
| **NAVCO 1.3** | 1900–2019 | **~26.0%** (Hong Kong, 2019) | **SHATTERED** |

## ⚠️ Critical Forensic Finding: The 1.3 Data Gap
While `NAVCO 1.3 List.xlsx` is the official ledger for outcomes up to 2019, it represents a "forensic dead-end" for the 3.5% Rule. 

* **1.1 & 1.2:** Include the raw numbers (Membership/Population) needed to calculate the 3.5% threshold.
* **1.3:** The researchers **omitted the participation columns** in this summary list. 
* **Implication:** The 1.3 file confirms that massive modern movements like **Hong Kong (2019)** were failures (`SUCCESS=0`), but it obscures the participation data that proves the 3.5% Rule is no longer valid.

## ⚖️ Political Implication: U.S. Domestic Application

**The NAVCO dataset identifies success only within the goals of a "Maximalist Campaign."**

As defined in the NAVCO 1.3 Codebook (p. 2), a maximalist campaign is strictly limited to:
1.  **Regime Change** (Overthrowing the existing government)
2.  **Anti-Occupation** (Expelling a foreign military)
3.  **Secession** (Breaking away to form a new state)

### The Warning
When public figures (such as Maria J. Stephan) promote the "3.5% Rule" within the United States, they are citing a manual for **regime change**, not democratic reform. Because the data set ignores all non-maximalist movements (policy protests), using this rule in the U.S. carries a strong insinuation of **overthrowing the government**. 

Furthermore, the audit shows that "all states will defend themselves." Modern state capacity in the 21st century has rendered the 3.5% threshold obsolete; governments are now successfully suppressing movements that far exceed that number.

## Requirements
* Python 3.9+
* Pandas
* Openpyxl (for Excel support)

## Usage
1. Place `NAVCO 1.1.dta`, `NAVCO 1.2 Updated.xlsx`, and `NAVCO 1.3 List.xlsx` in the root folder.
2. Run `python app.py`.
