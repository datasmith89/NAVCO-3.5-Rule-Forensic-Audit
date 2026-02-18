import pandas as pd
import numpy as np
import os
import sys

# --- CONFIGURATION ---
FILES = {
    "1.1": ["NAVCO 1.1.dta"],
    "1.2": ["NAVCO 1.2 Updated.xlsx", "NAVCO 1.2 Updated.csv"],
    "1.3": ["NAVCO 1.3 List.xlsx", "NAVCO 1.3 List.csv", "NAVCO 1.3 List.xlsx - Sheet1.csv"]
}

def banner(text):
    print(f"\n{'='*70}\n{text.center(70)}\n{'='*70}")

def load_file(version):
    for fname in FILES[version]:
        if os.path.exists(fname):
            print(f"[{version}] Found: {fname}")
            try:
                if fname.endswith('.dta'): return pd.read_stata(fname)
                if fname.endswith('.xlsx'): return pd.read_excel(fname)
                if fname.endswith('.csv'): return pd.read_csv(fname)
            except Exception as e:
                print(f"Error: {e}")
    return None

def analyze_1_1(df):
    """
    NAVCO 1.1 (1900-2006)
    Has precise participation numbers (peakmembership).
    """
    banner("NAVCO 1.1 (1900-2006)")
    
    # Calculate Participation %
    if 'peakmembership' in df.columns and 'lnpop' in df.columns:
        df['pop_cal'] = np.exp(df['lnpop']) * 1000
        df['part_pct'] = df['peakmembership'] / df['pop_cal']
        
        # Find biggest NONVIOLENT FAILURE
        fails = df[(df['nonviol'] == 1) & (df['success'] == 0)]
        
        if not fails.empty:
            max_fail = fails.loc[fails['part_pct'].idxmax()]
            print(f"Highest Failure: {max_fail['campaign']} ({max_fail['byear']})")
            print(f"Participation:   {max_fail['part_pct']:.2%} (Limit: 3.5%)")
            
            if max_fail['part_pct'] < 0.035:
                print("VERDICT:         RULE HOLDS (Max failure < 3.5%)")
            else:
                print("VERDICT:         RULE BROKEN")
        else:
            print("No nonviolent failures found.")
    else:
        print("Error: Missing 'peakmembership' or 'lnpop' columns.")

def analyze_1_2(df):
    """
    NAVCO 1.2 (1945-2013)
    Has pre-calculated percentage column.
    """
    banner("NAVCO 1.2 (1945-2013)")
    df.columns = [c.upper().strip() for c in df.columns]
    
    pct_col = 'PERCENTAGE POPULAR PARTICIPATION'
    if pct_col in df.columns:
        # Find biggest NONVIOLENT FAILURE
        nv_col = 'NONVIOL' if 'NONVIOL' in df.columns else 'PRIM_METHOD'
        fails = df[(df[nv_col] == 1) & (df['SUCCESS'] == 0)].copy()
        
        if not fails.empty:
            top_fail = fails.sort_values(by=pct_col, ascending=False).iloc[0]
            val = top_fail[pct_col]
            threshold = 3.5 if val > 1.0 else 0.035
            
            print(f"Highest Failure: {top_fail.get('CAMPAIGN')} ({top_fail.get('BYEAR')})")
            print(f"Participation:   {val:.2%} (Limit: {threshold:.1%})")
            
            if val > threshold:
                print("VERDICT:         RULE BROKEN")
            else:
                print("VERDICT:         RULE HOLDS")
        else:
            print("No nonviolent failures found.")
    else:
        print(f"Error: Column '{pct_col}' not found.")

def analyze_1_3(df):
    """
    NAVCO 1.3 (1900-2019)
    Forensic Check: Does it even HAVE the numbers?
    """
    banner("NAVCO 1.3 (1900-2019)")
    df.columns = [c.upper().strip() for c in df.columns]
    
    # 1. Check for Participation Data
    part_keywords = ['MEMBERSHIP', 'PARTICIPATION', 'SIZE', 'PCT', 'PERCENT']
    found_cols = [c for c in df.columns if any(k in c for k in part_keywords)]
    
    if found_cols:
        print(f"Data columns found: {found_cols}")
        # If found, we would run the logic here.
        # But based on your file, we expect NONE.
    else:
        print("CRITICAL FINDING: Participation data is MISSING in this dataset.")
        print("Analysis: NAVCO 1.3 covers the Hong Kong/Modern era (2019),")
        print("          but the 'participation' variable was removed from this specific file.")
        
        # 2. Check for Hong Kong Outcome
        # We can at least prove Hong Kong FAILED in this dataset.
        hk = df[df['LOCATION'].str.contains('Hong Kong', case=False, na=False) | 
                df['LOCATION'].str.contains('China', case=False, na=False)]
        
        hk_fails = hk[(hk['CAMPAIGN'].str.contains('Hong Kong', case=False, na=False)) & 
                      (hk['SUCCESS'] == 0) & 
                      (hk['NONVIOL'] == 1)]
        
        if not hk_fails.empty:
            print("\nConfirmed Outcomes in 1.3:")
            for _, row in hk_fails.iterrows():
                print(f" -> {row['CAMPAIGN']} ({row['BYEAR']}): FAILED")
            print("\nImplication: We have the failure (Success=0) but the '3.5%' math is impossible")
            print("             to run because the participation column was dropped.")
        else:
            print("Hong Kong failure not explicitly found in text search.")

def main():
    df1 = load_file("1.1")
    if df1 is not None: analyze_1_1(df1)
    
    df2 = load_file("1.2")
    if df2 is not None: analyze_1_2(df2)
    
    df3 = load_file("1.3")
    if df3 is not None: analyze_1_3(df3)

if __name__ == "__main__":
    main()