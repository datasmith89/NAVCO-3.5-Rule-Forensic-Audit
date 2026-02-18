import pandas as pd
import numpy as np
import os


FILES = {
    "1.1": "NAVCO 1.1.dta",
    "1.2": "NAVCO 1.2 Updated.xlsx",
    "1.3": "NAVCO 1.3 List.xlsx",
    "2.1": "NAVCO2-1_ForPublication.xls"
}

def print_intro():
    banner("NAVCO PROJECT FORENSIC AUDIT: DATASET-DRIVEN COMPARISON")
    print("""
This script performs a longitudinal audit of the '3.5% Rule' across four 
generations of the NAVCO research project. 

OBJECTIVES:
1. Identify the 20th-century 'failure ceiling' used to establish the 3.5% rule.
2. Cross-reference 21st-century failures (Bahrain) across different versions.
3. Verify the presence of participation data in modern summary lists (v1.3).

METHODOLOGY:
The script relies exclusively on internal variables (peakmembership, lnpop, 
CAMP_SIZE_CAT, and SUCCESS) to track how failure outcomes are recorded.
    """)

def banner(text):
    print(f"\n{'='*80}\n{text.center(80)}\n{'='*80}")

def run_neutral_audit():
    print_intro()
    
    # 1. NAVCO 1.1 Analysis
    if os.path.exists(FILES["1.1"]):
        report_section = "NAVCO 1.1 (Data Range: 1900-2006)"
        banner(report_section)
        df = pd.read_stata(FILES["1.1"])
        # Calculating % from raw population and membership
        df['pop_cal'] = np.exp(df['lnpop']) * 1000
        df['part_pct'] = df['peakmembership'] / df['pop_cal']
        
        nv_fails = df[(df['nonviol'] == 1) & (df['success'] == 0)]
        if not nv_fails.empty:
            max_f = nv_fails.loc[nv_fails['part_pct'].idxmax()]
            print(f"Finding: Highest failure participation recorded: {max_f['part_pct']:.4%}")
            print(f"Campaign: {max_f['campaign']} ({max_f['byear']})")

    # 2. NAVCO 1.2 Analysis
    if os.path.exists(FILES["1.2"]):
        banner("NAVCO 1.2 (Data Range: 1945-2013)")
        df = pd.read_excel(FILES["1.2"])
        df.columns = [str(c).strip().upper() for c in df.columns]
        pct_col = 'PERCENTAGE POPULAR PARTICIPATION'
        
        if pct_col in df.columns:
            nv_fails = df[(df['NONVIOL'] == 1) & (df['SUCCESS'] == 0)]
            if not nv_fails.empty:
                max_f = nv_fails.sort_values(by=pct_col, ascending=False).iloc[0]
                print(f"Finding: Highest failure participation recorded: {max_f[pct_col]:.4%}")
                print(f"Campaign: {max_f.get('CAMPAIGN')} ({max_f.get('BYEAR')})")

    # 3. NAVCO 2.1 Analysis (Citation: Chenoweth & Shay, 2019)
    if os.path.exists(FILES["2.1"]):
        banner("NAVCO 2.1 (Annual Data - Chenoweth & Shay, 2019)")
        df = pd.read_excel(FILES["2.1"])
        df.columns = [str(c).strip().upper() for c in df.columns]
        
        target_case = df[(df['LOCATION'].str.contains('Bahrain', na=False)) & (df['YEAR'] == 2011)]
        if not target_case.empty:
            row = target_case.iloc[0]
            print(f"Case Study: {row.get('CAMP_NAME')} ({row.get('YEAR')})")
            print(f"Recorded Size Category (CAMP_SIZE_CAT): {row.get('CAMP_SIZE_CAT')}")
            print(f"Recorded Success (SUCCESS): {row.get('SUCCESS')}")
            print("Note: Size Category 2 represents a range of 1,001 - 10,000 participants.")

    # 4. NAVCO 1.3 Analysis
    if os.path.exists(FILES["1.3"]):
        banner("NAVCO 1.3 (Data Range: 1900-2019)")
        df = pd.read_excel(FILES["1.3"])
        df.columns = [str(c).strip().upper() for c in df.columns]
        
        part_keywords = ['PARTICIPATION', 'MEMBERSHIP', 'PERCENTAGE', 'PCT']
        found_cols = [c for c in df.columns if any(k in c for k in part_keywords)]
        
        print(f"Participation variables found in v1.3 summary list: {found_cols if found_cols else 'None'}")
        
        hk_case = df[df['CAMPAIGN'].str.contains('Hong Kong', case=False, na=False)]
        if not hk_case.empty:
            for _, row in hk_case.iterrows():
                print(f"Outcome Check: {row['CAMPAIGN']} ({row['BYEAR']}) | Success: {row['SUCCESS']}")

if __name__ == "__main__":
    run_neutral_audit()
