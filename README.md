# NAVCO Forensic Audit: The Collapse of the 3.5% Rule

## Project Overview
This repository contains a Python-based forensic audit of the **"3.5% Rule"**—the widely cited claim that no nonviolent campaign has failed after reaching a 3.5% participation threshold. This audit reverse-engineers the data across four versions of the NAVCO project to identify exactly when and how this "rule" became obsolete in the 21st century.

## Data Sources & Links
All data used in this audit is sourced from the **Nonviolent and Violent Campaigns and Outcomes (NAVCO) Data Project**.

* **NAVCO 1.1:** [EricaChenoweth.com](https://www.ericachenoweth.com/research) / [Harvard Dataverse (doi:10.7910/DVN/07IDW)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YLLHEE)
* **NAVCO 1.2:** [Harvard Dataverse (doi:10.7910/DVN/0UZOTX)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/0UZOTX)
* **NAVCO 1.3:** [Harvard Dataverse (doi:10.7910/DVN/MHOXDV)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ON9XND)
* **NAVCO 2.1:** [Harvard Dataverse (doi:10.7910/DVN/MHOXDV)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MHOXDV)

## Dataset Observations

| Version | Period | Participation Variable | Recorded Highest Failure |
| :--- | :--- | :--- | :--- |
| **NAVCO 1.1** | 1900–2006 | Calculated (Membership/Pop) | **3.4530%** (1987 Intifada) |
| **NAVCO 1.2** | 1945–2013 | Pre-calculated Column | **6.3816%** (Bahrain, 2011) |
| **NAVCO 2.1** | 1945–2014 | Categorical (1-5 Scale) | **Size Category 2** (Bahrain, 2011) |
| **NAVCO 1.3** | 1900–2019 | None Provided in List | **Success: 0** (Hong Kong, 2014) |



## ⚠️ Critical Forensic Findings

### The 1.3 Data Gap
While `NAVCO 1.3 List.xlsx` is the official outcome ledger through 2019, it represents a "forensic dead-end" for the participation-based theory.
* **Finding:** The 1.3 file confirms massive modern movements like **Hong Kong (2014)** were failures (`SUCCESS=0`), but the participation variables used to calculate the 3.5% rule in versions 1.1 and 1.2 were omitted from this specific summary list.

### The 2.1 Coding Shift
In the annual disaggregated data (**NAVCO 2.1**), the audit identifies a shift in how high-participation failures are classified.
* **Finding:** The Bahrain 2011 campaign, recorded at **6.3816%** in v1.2, is recorded in v2.1 (Chenoweth & Shay, 2019) as **Size Category 2** (representing 1,001 - 10,000 participants). 

## ⚖️ Domain Application & Methodology Warning

**The NAVCO dataset identifies success ONLY within the goals of a "Maximalist Campaign."**

As defined in the official **NAVCO Codebook (p. 2)**, a maximalist campaign is strictly limited to:
1.  **Regime Change** (Overthrowing the existing government/constitution)
2.  **Anti-Occupation** (Expelling a foreign military)
3.  **Secession** (Breaking away to form a new state)



### The Warning
When public figures promote the "3.5% Rule" in the United States, they are citing a manual for **regime change**. Because the dataset excludes all non-maximalist movements (policy reform/protest), using this rule in the U.S. carries a factual implication of **overthrowing the government**. As this audit demonstrates, 21st-century state capacity has evolved to successfully defend against maximalist pressure, rendering the 20th-century "3.5% guarantee" obsolete.

## Citations
* **NAVCO 1.1 - 1.3:** Chenoweth, Erica, and Maria J. Stephan. 2011. *Why Civil Resistance Works: The Strategic Logic of Nonviolent Conflict*. New York: Columbia University Press.
* **NAVCO 2.1:** Chenoweth, Erica, and Christopher Wiley Shay. 2019. *NAVCO 2.1 Dataset*. Harvard Dataverse.

## Usage
1. Place `NAVCO 1.1.dta`, `NAVCO 1.2 Updated.xlsx`, `NAVCO 1.3 List.xlsx`, and `NAVCO2-1_ForPublication.xls` in the root folder.
2. Run `python app.py`.
